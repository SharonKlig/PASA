import logging
import os
import os.path
from os.path import isfile, join
import csv
import DB_record as dbr
import re
import time

logger = logging.getLogger('Logs/PASA_pipeline.log')

current_milli_time = lambda: int(round(time.time() * 1000))


def load_db (folder):
    '''
    :param folder: folder which the db files are located
    :return: a dictionary with all seqs as keys and values are DB_record class (includes all header fields + db number)
    '''
    counter = 0

    files = [join(folder, file) for file in os.listdir(folder)]
    db_dict = {}
    for file, label in zip(files, range(1,len(files)+1)):
        if (isfile(file)) == False:
            logger.error("ERROR, missing file " + str(file))
            continue
        file = open(file, 'r')
        lines = file.readlines()
        flag = False    #in sp/tr section
        first = True

        for line in lines:
            if re.search('>', line):
                if (re.search('sp', line) or re.search('tr', line)):
                    continue
                else:
                    if (re.search('IBD', line)):       #for the old db might appear only IGH- check
                        if first == False:
                            db_rec.seq = seq
                            cdr3_start, cdr3_end = get_substring_indexes(seq, cdr3)
                            db_rec.cdr3_start, db_rec.cdr3_end = cdr3_start, cdr3_end
                            db_dict[seq] = db_rec
                            counter += 1
                            if (counter % 50000 == 0):
                                print(str(counter) + ' already loaded, db num: '+ str(db_rec.db_num))
                        else:
                            first = False
                        seq = ''
                        flag = True #in IGH section(old db)
                        line1 = line.split('|')
                        cdr3 = line1[3]

                        try:
                            db_rec = dbr.DB_record(label, "", line1[0], line1[1], line1[2], cdr3, line1[4],
                                                   line1[5], line1[6], line1[7], line1[8].rstrip('\n'))
                        except:
                            db_rec = dbr.DB_record(label, "", line1[0], line1[1], line1[2], cdr3, line1[4],
                                                   line1[5], line1[6], line1[7].rstrip('\n'))
                        continue
                    else:
                        print('check')

            if flag == True:
                seq = seq+ line.rstrip('\n')

        db_rec.seq = seq    #the last one
        cdr3_start, cdr3_end = get_substring_indexes(seq, cdr3)
        db_rec.cdr3_start, db_rec.cdr3_end = cdr3_start, cdr3_end
        db_dict[seq] = db_rec
        counter += 1

    print(str(counter) + ' already loaded, db num: ' + str(db_rec.db_num)+ '\n')
    return db_dict


def check_if_peptide_in_db (db_dict, peptides_list):
    #check if peptid is in db, create a list per peptid with all db records that contain the peptid
    non_info = []
    new_peptide_dict = {}
    peptides_len = str(len(peptides_list))
    start = current_milli_time()
    peptids_counter = 0

    for peptide in peptides_list:
        new_peptide_dict[peptide] = [[],[]] #for each peptid, value[0]=db records, value[1]=start&end index of peptid on db records and also the specific permutation that match the record

    for peptide in new_peptide_dict.keys():
        peptids_counter += 1
        records_counter = 0
        in_db_flag = False

        peptide_combinations = create_all_I_L_combination(peptide)

        for key_db, value_db in db_dict.items():
            records_counter += 1
            if (records_counter % 100000 == 0):
                print('peptide ' + str(peptids_counter) + '/' + peptides_len + ' : ' + str(records_counter) + ' records were already checked')

            is_peptide_in_seq, start_index, end_index, chosen_combination = check_all_combinations_similarity(peptide_combinations, key_db, 100)
            if is_peptide_in_seq == True:
                (new_peptide_dict[peptide])[0].append(value_db)
                (new_peptide_dict[peptide])[1].append([start_index, end_index, chosen_combination])
                in_db_flag = True

        two_or_more_maps = check_if_there_is_more_than_one_combinations_fit(new_peptide_dict[peptide])

        if in_db_flag == False or two_or_more_maps == True:
            non_info.append(peptide)

    new_filtered_peptide_dict = {peptide: value_peptide for peptide, value_peptide in new_peptide_dict.items()\
                                 if peptide not in non_info }

    end = current_milli_time()
    print (str((end - start)/1000/60) + ' minutes')
    return new_filtered_peptide_dict , non_info


def check_if_cdr3_is_common (new_peptide_dict, non_info):
    #for all peptides that are in db, check if cdr3 is common
    info = []
    CDR3_info = []
    records_counter = 0
    counter_CDR3 = 0
    counter_info = 0

    for peptide, value_p in new_peptide_dict.items():
        records_counter += 1
        if (records_counter % 10000 == 0):
            print('10,000 \ ' + str(len(new_peptide_dict)) + 'peptides were already checked')
        is_there_different_cdr3 = False

        for i in range(len((value_p)[0])-1):
            if value_p[0][i].cdr3 != value_p[0][i+1].cdr3:
                non_info.append(peptide)
                is_there_different_cdr3 = True
                break

        if is_there_different_cdr3 == False:   #there is a common cdr3 for all seqs contain peptid

            is_there_overlap = True
            for i in range(len((value_p)[0])):
                peptide_start, peptide_end, cdr3_start, cdr3_end = value_p[1][i][0], value_p[1][i][1], value_p[0][i].cdr3_start, \
                                                     value_p[0][i].cdr3_end
                if is_there_overlap_bigger_than_threshold (peptide_start, peptide_end, cdr3_start, cdr3_end, 1):   #when overlap is at least 1aa
                    continue
                else:
                    is_there_overlap = False
            if is_there_overlap == True:
                counter_CDR3 += 1
                for i in range(len(value_p)-1):
                    CDR3_info.append([peptide, value_p[0][i].seq , value_p[0][i].db_num, value_p[0][i].ibd, value_p[0][i].cdr3, \
                                      value_p[0][i].IGHV, value_p[0][i].IGHD, value_p[0][i].IGHJ,\
                                      value_p[0][i].iso_type, value_p[0][i].chain_type, value_p[0][i].avg_counts])

            else:
                counter_info += 1
                info.append([peptide, value_p[0][i].seq , value_p[0][i].db_num, value_p[0][i].ibd, value_p[0][i].cdr3, \
                             value_p[0][i].IGHV, value_p[0][i].IGHD, value_p[0][i].IGHJ,\
                                      value_p[0][i].iso_type, value_p[0][i].chain_type, value_p[0][i].avg_counts])

    print( 'counter_CDR3: '+ str(counter_CDR3) +', counter_info: '+ str(counter_info)+ ', counter_non_info: '+ str(len(non_info))+\
           ', sum: '+ str(counter_CDR3 + counter_info + len(non_info))+ ', num_peptides: '+ str(len(new_peptide_dict)))
    logger.info( 'counter_CDR3: '+ str(counter_CDR3) +', counter_info: '+ str(counter_info)+ ', counter_non_info: '+ str(len(non_info))+\
           ', sum: '+ str(counter_CDR3 + counter_info + len(non_info))+ ', num_peptides: '+ str(len(new_peptide_dict)))

    return non_info, info, CDR3_info


def create_files (non_info,  info, CDR3_info, non_info_file, info_file, CDR3_info_file, peptides_dict_eb, peptides_dict_ft ):

    for item, file in zip([non_info, info, CDR3_info ] , [non_info_file, info_file, CDR3_info_file ]):

        with open(file, 'wt' , newline='') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            if item == non_info:
                tsv_writer.writerow(['Peptide_sequence'])
                for x in item:
                    tsv_writer.writerow([x])

            else:
                if item == info:
                    tsv_writer.writerow(
                        ['Peptide_sequence', 'db_Sequence', 'sequence_header', 'CDR3', 'V_family', 'D_family',
                         'J family', 'isotype', 'chain_type', 'avg_counts'])

                    for x in item:
                        tsv_writer.writerow([x[0], x[1], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10]])

                else:
                    tsv_writer.writerow(
                        ['Peptide_sequence', 'db_Sequence', 'sequence_header', 'CDR3', 'V_family', 'D_family',
                         'J family', 'isotype', 'chain_type', 'avg_counts', 'frequency_elution', 'frequency_flowthrough'])
                    for x in item:
                        pep = x[0]
                        eb = peptides_dict_eb.get(pep)
                        ft = peptides_dict_ft.get(pep)
                        if ft == None:
                            ft = ['0', '0']
                        tsv_writer.writerow([x[0], x[1], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], eb[1], ft[1]])


def similarity(seq, sub_seq):
    start_of_substring, end_of_substring = get_substring_indexes(seq, sub_seq)
    return (start_of_substring != -1, start_of_substring, end_of_substring)

def is_there_overlap_bigger_than_threshold (segment1_start, segment1_end, segment2_start, segment2_end, threshold):
    overlap = max(0, min(segment1_end, segment2_end) - max(segment1_start, segment2_start) + 1)
    return overlap >= threshold

# def similarity2(seq, sub_seq, threshold):
#     if threshold == 100:
#         return sub_seq.upper() in seq.upper()
#     else:
#         match = SequenceMatcher(None, seq, sub_seq).find_longest_match(0, len(seq), 0, len(sub_seq))
#         longest_common_string = seq[match.a: match.a + match.size]
#         rate = (float(len(longest_common_string))/float(len(sub_seq)))*100
#         return rate >= threshold


def check_all_combinations_similarity(peptide_combinations, db_seq, threshold):
    for combination in peptide_combinations:
        is_there_similiraity, start_of_substring, end_of_substring = similarity(db_seq, combination)
        if is_there_similiraity:
            return (True, start_of_substring, end_of_substring, combination)
    return (False, -1, -1, '')


def check_if_there_is_more_than_one_combinations_fit(records):
    if len(records[1]) == 1:
        return False
    for i in range(len((records)[0]) - 1):
        if (records[1][i][2] != records[1][i + 1][2]):
            return True
    return False


def create_all_I_L_combination(peptide):
    '''
    create all combinations of the peptid replacing L with I (and vice versa)
    '''
    sum_I_L = peptide.count('I') + peptide.count('L')
    list = []
    for i in range(2**sum_I_L ):
        perm = ('{:0{}b}'.format(i, sum_I_L))
        list.append(perm.replace(str(0), 'I').replace(str(1), 'L'))

    new_str = '#' + peptide.replace('I', '$').replace('L', '$') + '#'
    new_list = []
    for perm in list:
        new_str1 = new_str
        for char in perm:
            new_str1 = new_str1.replace('$', char, 1)
        new_word = new_str1.replace('#', '')
        new_list.append(new_word)

    return new_list


def get_substring_indexes (str, sub_str):
    start_index = str.upper().find(sub_str.upper())
    end_index = start_index + len(sub_str) - 1
    return (start_index, end_index)









