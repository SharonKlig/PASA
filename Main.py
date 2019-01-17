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

    html_path = os.path.join(FC.wd, 'output.html')
    run_number = FC.wd.split('/')[-2]

    if (run_number == 'example'):
        he.edit_success_html(html_path, FC.output_files, run_number, CONSTS, FC.file_output_names,
                          FC.strs_to_show_on_html)

    else:


        try:
            if not(os.path.exists(FC.eb_file)):      #peptides.txt was created from previous session
                print("running maxquant (elution)\n")
                logger.info("running maxquant (elution)")
                params_e = [FC.raw_files_e_1,FC.raw_files_e_2, FC.raw_files_e_3, FC.db_folder, FC.enzyme, FC.path_input_eb]
                mq.create_xml_config_file(FC.config_folder_eb, params_e, FC.numThreads, FC.config_sample_folder)
                mq.running_maxquant_through_cmd(FC.config_folder_eb)

            if not(os.path.exists(FC.ft_file)):     #peptides.txt was created from previous session
                print("running maxquant (flowthrough)\n")
                logger.info("running maxquant (flowthrough)")
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
            fe.create_new_filtered_file(peptides_list, FC.filtered_peptides_file)


            print("loading and parsing DB\n")
            logger.info("loading and parsing DB")
            db = util.read_or_new_pickle(FC.IsDebug, path=FC.pickle_file_db, default = dbf.load_db(FC.db_folder))
            #db = pickle.load(open(pickle_file_db, 'rb'))



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


            print("create cdr3 analysis\n")
            logger.info("create cdr3 analysis")
            sp.analyze_cdr3(CDR3_info, FC.pictures_folder)

            print("create peptid plot\n")
            logger.info("create peptid plot")
            sp.plot_peptid_records(peptides_dict_eb, db_peptides, FC.pictures_folder+ 'proteomics_vs_genetics.png')

            status = 'is done'



        except Exception:

            status = 'was failed'
            msg = 'PASA failed :( '
            he.edit_failure_html(html_path, run_number, msg, CONSTS)


        msg = f'PASA pipeline {status}'



        he.edit_success_html(html_path, FC.output_files, run_number, CONSTS, FC.file_output_names,
                             FC.strs_to_show_on_html)

        send_email('mxout.tau.ac.il', 'TAU BioSequence <bioSequence@tauex.tau.ac.il>', FC.user_email,
                   subject=f'PASA {status}.', content=msg)

        logger.info('PASA is DONE!!')
