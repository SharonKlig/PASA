import logging
import argparse
import FilterExcelFile as fe
import DB_analysis as dbf
import Statistics_and_Plots as sp
import pickle
import os
import MaxQuantRun as mq
import Files_and_Constants as FC
#from Files_test import *
import Utilities as util
import html_editor as he
import sys
import subprocess
import shutil



if FC.remote_run == True:
    sys.path.append('/bioseq/PASA/cgi/')
    sys.path.append('/bioseq/bioSequence_scripts_and_constants/')
sys.path.append('cgi/')

import WEBSERVER_CONSTANTS as CONSTS
from email_sender import send_email

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    filename=FC.log_file)
logger = logging.getLogger(FC.log_file)
logger.info('...pipeline begins...')



if __name__ == '__main__':

    output_url = os.path.join(CONSTS.WEBSERVER_RESULTS_URL, FC.wd, 'output.html')
    msg = f'job number = {FC.job_title}.\n'


    try:
        if not(os.path.exists(FC.eb_file)):      #peptides.txt was created from previous session
            print("running maxquant (elution)\n")
            logger.info("running maxquant (elution)")
            for file, name in zip([FC.raw_files_e_1,FC.raw_files_e_2, FC.raw_files_e_3], ['raw_files_e_1','raw_files_e_2','raw_files_e_3']):
                if FC.remote_run:
                    subprocess.call(["mv", file, os.path.join(FC.path_input_eb, name+'.raw')])
                else:
                    shutil.move(file, os.path.join(FC.path_input_eb, name+'.raw'))
            FC.raw_files_e_1, FC.raw_files_e_2, FC.raw_files_e_3 = os.path.join(FC.path_input_eb, 'raw_files_e_1.raw'), \
                                                                   os.path.join(FC.path_input_eb, 'raw_files_e_2.raw'), \
                                                                   os.path.join(FC.path_input_eb, 'raw_files_e_3.raw')
            params_e = [FC.raw_files_e_1,FC.raw_files_e_2, FC.raw_files_e_3, FC.db_folder, FC.enzyme, FC.path_input_eb]
            mq.create_xml_config_file(FC.config_folder_eb, params_e, FC.numThreads, FC.config_sample_folder)
            mq.running_maxquant_through_cmd(FC.config_folder_eb)

        if not(os.path.exists(FC.ft_file)):     #peptides.txt was created from previous session
            print("running maxquant (flowthrough)\n")
            logger.info("running maxquant (flowthrough)")
            for file, name in zip([FC.raw_files_f_1,FC.raw_files_f_2, FC.raw_files_f_3], ['raw_files_f_1','raw_files_f_2','raw_files_f_3']):
                if FC.remote_run:
                    subprocess.call(["mv", file, os.path.join(FC.path_input_ft, name+'.raw')])
                else:
                    shutil.move(file, os.path.join(FC.path_input_ft, name+'.raw'))
            FC.raw_files_f_1, FC.raw_files_f_2, FC.raw_files_f_3 = os.path.join(FC.path_input_ft, 'raw_files_f_1.raw'), \
                                                                   os.path.join(FC.path_input_ft, 'raw_files_f_2.raw'), \
                                                                   os.path.join(FC.path_input_ft, 'raw_files_f_3.raw')
            params_f = [FC.raw_files_f_1,FC.raw_files_f_2, FC.raw_files_f_3, FC.db_folder, FC.enzyme, FC.path_input_ft]
            mq.create_xml_config_file(FC.config_folder_ft, params_f, FC.numThreads, FC.config_sample_folder)
            mq.running_maxquant_through_cmd(FC.config_folder_ft)


        print("loading and parsing elution file\n")
        logger.info("loading and parsing elution file")
        eb_data, peptides_dict_eb = util.read_or_new_pickle (FC.IsDebug, path = FC.pickle_file_eb,\
                                                             default = fe.pre_process_on_file(FC.eb_file))


        print("loading and parsing flowthrough file\n")
        logger.info("loading and parsing flowthrough file")
        ft_data, peptides_dict_ft = util.read_or_new_pickle(FC.IsDebug, path = FC.pickle_file_ft,\
                                                            default= fe.pre_process_on_file(FC.ft_file))


        print("check if peptid appears in flowthrow and not elution \n")
        logger.info("check if peptid appears in flowthrow and not elution")
        peptides_list = util.read_or_new_pickle(FC.IsDebug, path = FC.pickle_file_peptides,\
                                                default= fe.check_if_appears_in_flow_through\
                                                    (peptides_dict_eb, peptides_dict_ft, FC.Y))


        print("create filtered peptid file\n")
        logger.info("create filtered peptid file")
        fe.create_new_filtered_file(peptides_list, FC.filtered_peptides_file, peptides_dict_eb, peptides_dict_ft)


        print("loading and parsing DB\n")
        logger.info("loading and parsing DB")
        #db = util.read_or_new_pickle(FC.IsDebug, path=FC.pickle_file_db, default = dbf.load_db(FC.db_folder))
        db = pickle.load(open(FC.pickle_file_db, 'rb')) #TODO: check why pickle doesn't work (prev line should stay, delete this one)

        '''
        print("create filtered peptides files according to cdr3\n")
        logger.info("create filtered peptides files according to cdr3")
        if FC.IsDebug == True:
            try:
                non_info = pickle.load(open(FC.pickle_file_non_info, 'rb'))
                info = pickle.load(open(FC.pickle_file_info, 'rb'))
                CDR3_info = pickle.load(open(FC.pickle_file_cdr3, 'rb'))
                db_peptides = pickle.load(open(FC.pickle_file_db_peptides, 'rb'))
            except (OSError, IOError, EOFError):
                non_info, info, CDR3_info, db_peptides = dbf.create_filtered_peptides_files_according_to_cdr3\
                                                        (FC.output_files + 'non_informative_peptides.tsv', \
                                                         FC.output_files + 'informative_peptides.tsv', \
                                                         FC.output_files + 'informative_CDR3_peptides.tsv',\
                                                         db, peptides_list)

                pickle._dump(non_info , open(FC.pickle_file_non_info, 'wb'))
                pickle._dump(info , open(FC.pickle_file_info, 'wb'))
                pickle._dump(CDR3_info , open(FC.pickle_file_cdr3, 'wb'))
                pickle._dump(db_peptides , open(FC.pickle_file_db_peptides, 'wb'))

        else:
            non_info, info, CDR3_info, db_peptides = dbf.create_filtered_peptides_files_according_to_cdr3\
                                                        (FC.output_files + 'non_informative_peptides.tsv', \
                                                         FC.output_files + 'informative_peptides.tsv', \
                                                         FC.output_files + 'informative_CDR3_peptides.tsv',\
                                                         db, peptides_list)

        '''

        print("check if peptid is in DB \n")    #TODO
        logger.info("check if peptid is in DB ")
        # db_peptides, non_info  = util.read_or_new_pickle(FC.IsDebug, path=FC.pickle_file_db_peptides, \
        #                                         default= dbf.check_if_peptid_in_db \
        #                                         (db, peptides_list))
        if FC.IsDebug == True:
            try:
                non_info = pickle.load(open(FC.pickle_file_non_info, 'rb'))
                db_peptides = pickle.load(open(FC.pickle_file_db_peptides, 'rb'))
            except (OSError, IOError, EOFError):
                db_peptides, non_info = dbf.check_if_peptid_in_db (db, peptides_list)
                pickle._dump(db_peptides, open(FC.pickle_file_db_peptides, 'wb'))
                pickle._dump(non_info, open(FC.pickle_file_non_info, 'wb'))
        else:
            db_peptides, non_info = dbf.check_if_peptid_in_db(db, peptides_list)




        print("creating filtered peptides files according to cdr3\n")   #TODO
        logger.info("creating filtered peptides files according to cdr3")
        # non_info, info, CDR3_info = util.read_or_new_pickle(FC.IsDebug, path= FC.pickle_file_non_info, \
        #                                                     FC.pickle_file_info, FC.pickle_file_cdr3, \
        #                                                     default= dbf.check_if_cdr3_is_common(db_peptides, non_info))
        if FC.IsDebug == True:
            try:
                info = pickle.load(open(FC.pickle_file_info, 'rb'))
                CDR3_info = pickle.load(open(FC.pickle_file_cdr3, 'rb'))
            except (OSError, IOError, EOFError):
                non_info, info, CDR3_info = dbf.check_if_cdr3_is_common(db_peptides, non_info)
                pickle._dump(non_info, open(FC.pickle_file_non_info, 'wb'))
                pickle._dump(info, open(FC.pickle_file_info, 'wb'))
                pickle._dump(CDR3_info, open(FC.pickle_file_cdr3, 'wb'))
        else:
            non_info, info, CDR3_info = dbf.check_if_cdr3_is_common(db_peptides, non_info)


        print("creating non info, info and cdr3 info files\n")
        logger.info("creating non info, info and cdr3 info files")
        dbf.create_files(non_info, info, CDR3_info, FC.output_files + 'non_informative_peptides.tsv', \
                                                         FC.output_files + 'informative_peptides.tsv', \
                                                         FC.output_files + 'informative_CDR3_peptides.tsv')



        print("create cdr3 analysis\n")
        logger.info("create cdr3 analysis")
        sp.analyze_cdr3(CDR3_info, FC.pictures_folder)

        print("create isotypes distribution\n")
        logger.info("create isotypes distribution")
        sp.generate_alignment_report_pie_chart(FC.pictures_folder + 'Isotypes_distribution.png', CDR3_info)


        print("create peptid plot\n")
        logger.info("create peptid plot")
        sp.plot_peptid_records(CDR3_info, peptides_dict_eb, db_peptides, FC.pictures_folder + 'proteomics_vs_genetics.png')


        file_output_names, strs_to_show_on_html = [], []
        for i, file in enumerate(FC.all_file_output_names):
            if os.path.isfile(file):
                file_output_names.append(file)
                strs_to_show_on_html.append(FC.all_strs_to_show_on_html[i])



        status = 'is done'
        msg += f'PASA pipeline {status}.'
        he.edit_success_html(FC.html_path, FC.output_files, FC.run_number, CONSTS, file_output_names,
                             strs_to_show_on_html)





    except Exception as e:

        logger.info(e)
        status = 'was failed'
        msg += f'PASA pipeline {status}.'
        he.edit_failure_html(FC.html_path, FC.run_number, msg, CONSTS)



    if status == 'is done':
        results_location = FC.wd
        msg += f' Results can be found at {results_location}.'

    send_email('mxout.tau.ac.il', 'TAU BioSequence <bioSequence@tauex.tau.ac.il>', FC.user_email,
               subject = f'PASA {status}.', content = msg)

    logger.info('PASA is DONE!!')
