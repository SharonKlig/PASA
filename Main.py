import logging
import argparse
import FilterExcelFile as fe
import DB_analysis as dbf
import Statistics_and_Plots as sp
import pickle
import os
import MaxQuantRun as mq
from Files_and_Contants import *

try:
    file = open(logs + 'main.log', 'r')
except IOError:
    file = open(logs + 'main.log', 'w')
logging.basicConfig(filename=logs + 'main.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')


if __name__ == '__main__':


    print("running maxquant (elution)\n")
    logging.info("running maxquant (elution)")
    params_e = [raw_files_e_1,raw_files_e_2, raw_files_e_3, db_folder, enzyme, path_input_e]
    mq.create_xml_config_file(config_folder_e, params_e, numThreads, config_sample_folder)
    mq.running_maxquant_through_cmd(config_folder_e)

    print("running maxquant (flowthrough)\n")
    logging.info("running maxquant (flowthrough)")
    params_f = [raw_files_f_1,raw_files_f_2, raw_files_f_3, db_folder, enzyme, path_input_f]
    mq.create_xml_config_file(config_folder_f, params_f, numThreads, config_sample_folder)
    mq.running_maxquant_through_cmd(config_folder_f)

    print("loading and parsing day0 (elution)\n")
    logging.info("loading and parsing day0 (elution)")
    try:
        days0, peptides_dict_0 = pickle.load(open(pickle_file_e, "rb"))
    except (OSError, IOError, EOFError):
        days0, peptides_dict_0 = fe.pre_process_on_file(day0_file)
        pickle.dump((days0, peptides_dict_0), open(pickle_file_e, "wb"))

    print("loading and parsing day10 (flowthrough)\n")
    logging.info("loading and parsing day10 (flowthrough)")
    try:
        days10, peptides_dict_10 = pickle.load(open(pickle_file_f, "rb"))
    except (OSError, IOError, EOFError):
        days10, peptides_dict_10 = fe.pre_process_on_file(day10_file)
        pickle.dump((days10, peptides_dict_10), open(pickle_file_f, "wb"))


    print("check if peptid appears in flowthrow and not elution \n")
    logging.info("check if peptid appears in flowthrow and not elution")
    try:
        peptides_list = pickle.load(open(pickle_file_p, "rb"))
    except (OSError, IOError, EOFError):
        peptides_list = fe.check_if_appears_in_flow_through(peptides_dict_0, peptides_dict_10, Y)
        pickle.dump(peptides_list, open(pickle_file_p, "wb"))

    print("create filtered peptid file\n")
    logging.info("create filtered peptid file")
    fe.create_new_filtered_file(peptides_list, output)

    print("loading and parsing DB\n")
    logging.info("loading and parsing DB")
    try:
       db = pickle.load(open(pickle_file_db, "rb"))
    except (OSError, IOError, EOFError):
        db = dbf.load_db(db_folder)
        pickle.dump(db, open(pickle_file_db, "wb"))


    print("create filtered peptides files according to cdr3\n")
    logging.info("create filtered peptides files according to cdr3")
    try:
        non_info = pickle.load(open(pickle_file_non_info, 'rb'))
        info = pickle.load(open(pickle_file_info, 'rb'))
        CDR3_info = pickle.load(open(pickle_file_cdr3, 'rb'))
    except (OSError, IOError, EOFError):
        non_info, info, CDR3_info, db_peptides = dbf.create_filtered_peptides_files_according_to_cdr3(output_files + 'non_informative_peptides.tsv',\
                                                        output_files + 'informative_peptides.tsv',\
                                                        output_files + 'informative_CDR3_peptides.tsv',\
                                                         db, peptides_list)

        pickle._dump(non_info , open(pickle_file_non_info, 'wb'))
        pickle._dump(info , open(pickle_file_info, 'wb'))
        pickle._dump(CDR3_info , open(pickle_file_cdr3, 'wb'))



    print("create cdr3 analysis\n")
    logging.info("create cdr3 analysis")
    sp.analyze_cdr3(CDR3_info, pictures_folder)

    print("create peptid plots\n")
    logging.info("create peptid plots")
    sp.plot_peptid_records(peptides_list, peptides_dict_0, db_peptides, pictures_folder+ 'plot.png')


    print('done')
    logging.info("done")