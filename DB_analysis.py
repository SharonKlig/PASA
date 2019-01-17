import logging
import regex as re
import os
import os.path
from os.path import isfile, join
from difflib import SequenceMatcher
import csv
import DB_record as dbr
import timeit
import re
import time
#from Files_and_Constants import log_file

logger = logging.getLogger('Logs/PASA_pipeline.log')


current_milli_time = lambda: int(round(time.time() * 1000))
#import magic
import zipfile


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
                            #db_dict[seq] = [cdr3 , label]
                            db_rec.seq = seq
                            db_dict[seq] = db_rec
                            counter += 1
                            if (counter % 50000 == 0):
                                print(str(counter) + ' already loaded, db num: '+ str(db_rec.db_num))
                        else:
                            first = False
                        seq = ''
                        flag = True #in IGH section(old db)
                        line1 = line.split('|')
                        #cdr3 = line1[3]

                        try:
                            db_rec = dbr.DB_record(label, "", line1[0], line1[1], line1[2], line1[3], line1[4],
                                                   line1[5], line1[6], line1[7], line1[8].rstrip('\n'))
                        except:
                            db_rec = dbr.DB_record(label, "", line1[0], line1[1], line1[2], line1[3], line1[4],
                                                   line1[5], line1[6], line1[7].rstrip('\n'))
                        continue
                    else:
                        print('check')

            if flag == True:
                seq = seq+ line.rstrip('\n')

        #db_dict[seq] = [cdr3 , label]  #the last one
        db_rec.seq = seq    #the last one
        db_dict[seq] = db_rec
        counter += 1

    print(str(counter) + ' already loaded, db num: ' + str(db_rec.db_num)+ '\n')
    return db_dict


def create_filtered_peptides_files_according_to_cdr3 (non_info_file, info_file, CDR3_info_file, db_dict, peptides_list):
    new_peptid_dict = {}
    info = []
    non_info = []
    CDR3_info = []

    #for key_p, value_p in peptides_dict.items():
     #   new_p_dict [key_p] = [value_p, []]
    for peptid in peptides_list:
       new_peptid_dict [peptid] = []

    new_peptid_dict, non_info = check_if_peptid_in_db (db_dict, new_peptid_dict, non_info)
    non_info, info, CDR3_info = check_if_cdr3_is_common (new_peptid_dict, non_info , info , CDR3_info)
    create_files(non_info, info, CDR3_info, non_info_file, info_file, CDR3_info_file)

    return (non_info, info, CDR3_info, new_peptid_dict)


def check_if_peptid_in_db (db_dict, new_peptid_dict, non_info):
    #check if peptid is in db, create a list per peptid with all db records that contain the peptid
    peptids_len = str(len(new_peptid_dict))
    start = current_milli_time()
    peptids_counter = 0
    for peptid in new_peptid_dict.keys():
        peptids_counter += 1
        records_counter = 0
        in_db_flag = False

        peptid_permutations = create_all_I_L_combination(peptid)

        for key_db, value_db in db_dict.items():
            records_counter += 1
            if (records_counter % 100000 == 0):
                print('peptid ' + str(peptids_counter) + '/' + peptids_len + ' : ' + str(records_counter) + ' peptides were already checked')
            if (check_all_combinations_similarity(peptid_permutations, key_db, 100)):
                new_peptid_dict[peptid].append(value_db)
                in_db_flag = True
        if in_db_flag == False:
            non_info.append(peptid)

    new_filtered_peptid_dict = {peptid: value_peptid for peptid, value_peptid in new_peptid_dict.items() if value_peptid != []}

    end = current_milli_time()
    print ( (end - start) / 1000 / 60)
    return new_filtered_peptid_dict , non_info

'''
def check_if_peptid_in_db (db_dict, new_peptid_dict, non_info):
    #check if peptid is in db, create a list per peptid with all db records that contain the peptid
    records_counter = 0
    for key_db, value_db in db_dict.items():
        records_counter += 1
        if (records_counter % 100000 == 0):
            print('10,000 \ ' + str(len(db_dict)) + ' records were already checked')
        for peptid, value_p in new_peptid_dict.items():
            if similarity(key_db, peptid , 100):
                new_peptid_dict[peptid].append(value_db)

    for peptid, value_p in new_peptid_dict.items():
        if value_p == []:
            non_info.append(peptid)

    return new_peptid_dict , non_info
    '''

def check_if_cdr3_is_common (new_peptid_dict, non_info , info , CDR3_info):
    #for all peptides that are in db, check if cdr3 is common
    print('now checking CDR3\n')
    logger.info('now checking CDR3')
    records_counter = 0
    counter_CDR3 = 0
    counter_info = 0
    for peptid, value_p in new_peptid_dict.items():
        records_counter += 1
        if (records_counter % 10000 == 0):
            print('10,000 \ ' + str(len(new_peptid_dict)) + 'peptides were already checked')
        flag = False

        for i in range(len(value_p)-1):
            if value_p[i].cdr3 != value_p[i+1].cdr3:
                non_info.append(peptid)
                flag = True
                break

        if flag == False:   #there is a common cdr3 for all seqs contain peptid
            #if similarity(value_p[0].cdr3, peptid, 1):
            all_peptid_permutations = create_all_I_L_combination(peptid)

            if (check_all_combinations_similarity(all_peptid_permutations, value_p[0].cdr3, 1)):

                counter_CDR3 += 1
                #CDR3_info.append([peptid , value_p[0][0] , [value_p[x][1] for x in range (len(value_p))]])
                for i in range(len(value_p)-1):
                    CDR3_info.append([peptid, value_p[i].seq , value_p[i].db_num, value_p[i].ibd, value_p[i].cdr3, \
                                      value_p[i].IGHV, value_p[i].IGHD, value_p[i].IGHJ,\
                                      value_p[i].randomletter, value_p[i].ig_x, value_p[i].num1])

            else:
                counter_info += 1
                #info.append([peptid , value_p[0][0], [value_p[x][1] for x in range (len(value_p))] ])
                info.append([peptid, value_p[i].seq , value_p[i].db_num, value_p[i].ibd, value_p[i].cdr3, \
                                      value_p[i].IGHV, value_p[i].IGHD, value_p[i].IGHJ,\
                                      value_p[i].randomletter, value_p[i].ig_x, value_p[i].num1])

    print( 'counter_CDR3: ' , counter_CDR3 ,', counter_info: ', counter_info, ', counter_non_info: ',len(non_info) ,\
           ', sum: ', counter_CDR3 + counter_info + len(non_info), ', num_peptides: ','571')

    return non_info, info, CDR3_info


def create_files (non_info,  info, CDR3_info, non_info_file, info_file, CDR3_info_file ):

    for item, file in zip([non_info, info, CDR3_info ] , [non_info_file, info_file, CDR3_info_file ]):
        with open(file, 'wt') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            if item == non_info:
                tsv_writer.writerow(['Peptid name'])
                for x in item:
                    tsv_writer.writerow(x) #????????????????????????

            tsv_writer.writerow(['Peptid name', 'Sequence', 'db number', 'ibd', 'CDR3', 'IGHV', 'IGHD' , 'IGHJ', '?????', '???????', '??????'])
            for x in item:
                tsv_writer.writerow(x)


def similarity(seq, sub_seq, threshold):
    if threshold == 100:
        return sub_seq.upper() in seq.upper()          #check
    else:
        match = SequenceMatcher(None, seq, sub_seq).find_longest_match(0, len(seq), 0, len(sub_seq))
        longest_common_string = seq[match.a: match.a + match.size]
        rate = (float(len(longest_common_string))/float(len(sub_seq)))*100
        return rate >= threshold

# def create_all_I_L_combination(peptid, other_seq, threshold):
#     '''
#     create all combinations of the peptis replacing L with I (and vice versa)
#     :param: peptid
#     :return:
#     '''
#
#     sum_I_L = peptid.count('I') + peptid.count('L')
#     list = []
#     for i in range(2**sum_I_L ):
#         perm = ('{:0{}b}'.format(i, sum_I_L))
#         list.append(perm.replace(str(0), 'I').replace(str(1), 'L'))
#
#     new_str = '#' + peptid.replace('I' , '$').replace('L', '$') + '#'
#     #splitted_str = new_str.split('$')
#     new_list = []
#     for perm in list:
#         new_str1 = new_str
#         for char in perm:
#             new_str1 = new_str1.replace('$', char, 1)
#         new_word = new_str1.replace('#', '')
#         new_list.append(new_word)
#
#     if threshold == 100:
#         for per in new_list:
#             if similarity(other_seq, per, threshold):
#                 return True
#
#         return False
#
#     else:
#         for per in new_list:
#             if similarity(other_seq, per, threshold):
#                 return True
#
#         return False

def check_all_combinations_similarity(peptid_permutations, other_seq, threshold):
    for per in peptid_permutations:
        if similarity(other_seq, per, threshold):
            return True

    return False

def create_all_I_L_combination(peptid):
    '''
    create all combinations of the peptid replacing L with I (and vice versa)
    '''

    sum_I_L = peptid.count('I') + peptid.count('L')
    list = []
    for i in range(2**sum_I_L ):
        perm = ('{:0{}b}'.format(i, sum_I_L))
        list.append(perm.replace(str(0), 'I').replace(str(1), 'L'))

    new_str = '#' + peptid.replace('I' , '$').replace('L', '$') + '#'
    #splitted_str = new_str.split('$')
    new_list = []
    for perm in list:
        new_str1 = new_str
        for char in perm:
            new_str1 = new_str1.replace('$', char, 1)
        new_word = new_str1.replace('#', '')
        new_list.append(new_word)

    return new_list









