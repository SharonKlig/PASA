import regex as re



def load_db (file):
    file = open(file, 'r')
    lines = file.readlines()
    flag = False    #in sp/tr section
    first = True
    db_dict = {}

    for line in lines:
        if re.search('>', line):
            if (re.search('sp', line) or re.search('tr', line)):
                continue
            else:
                if (re.search('IGH', line)) or (re.search('IBD', line)):
                    if first == False:
                        db_dict[seq] = cdr3
                    else:
                        first = False
                    seq = ''
                    flag = True #in IGH section
                    line1 = line.split('|')
                    cdr3 = line1[3]
                    continue
                else:
                    print('check')

        if flag == True:
            seq = seq+ line.rstrip('\n')

    return db_dict


def create_filtered_peptides_files_according_to_cdr3 (non_info_file, info_file, CDR3_info_file, db_dict, peptides_dict):
    new_p_dict = {}
    info = []
    non_info = []
    CDR3_info = []

    for key_p, value_p in peptides_dict.items():
        new_p_dict [key_p] = [value_p, []]

    for key_p, value_p in new_p_dict.items():
        in_db_flag = False
        for key_db, value_db in db_dict.items():
            if similarity(key_db , key_p, 100):         #change to persentage of similarity
                new_p_dict[key_p][1].append(value_db)
                in_db_flag = True
        if in_db_flag == False:
            non_info.append((key_p, value_p[0]))



    for key_p, value_p in new_p_dict.items():
        if value_p[1] == []:
            continue
        flag = False
        for i in range(len(value_p[1])-1):
            if value_p[1][i] != value_p[1][i+1]:
                non_info.append((key_p, value_p[0]))
                flag = True
                break
        if flag == False:
            if similarity(key_p ,value_p[1][0] ,100):
                CDR3_info.append((key_p, value_p[0]))
            else:
                info.append((key_p, value_p[0]))

    for item, file in zip([non_info, info, CDR3_info ] , [non_info_file, info_file, CDR3_info_file ]):
        file = open(file, 'w')
        for x in item:
            file.write(str(x[0]) + "\t" + str(x[1]) + "\n")


def similarity(seq, sub_seq, num):
    if sub_seq.upper() in seq.upper():          #check
        return True
    else:
        return False


