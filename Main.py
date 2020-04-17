import logging
import argparse
import FilterExcelFile as fe
import DB_analysis as dbf
import Statistics_and_Plots as sp
import pickle
import os
import MaxQuantRun as mq
import Files_and_Constants as FC
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
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    filename=FC.log_file)
logger = logging.getLogger(FC.log_file)
logger.info('...pipeline begins...')



if __name__ == '__main__':

    output_url = os.path.join(CONSTS.WEBSERVER_RESULTS_URL, FC.wd, 'output.html')

    job_title = 'NO_JOB_TITLE'
    if os.path.exists(FC.job_title_file):
        with open(FC.job_title_file) as f:
            job_title = f.read().rstrip()

    msg = f'job number = {job_title}.\n'
    logger.info("job jumber is: " + job_title)

    user_email = 'NO_EMAIL'
    if os.path.exists(FC.user_email_file):
        with open(FC.user_email_file) as f:
            user_email = f.read().rstrip()
    logger.info("user email is: " + user_email)


    try:
        if not(os.path.exists(FC.eb_file)):      #checks if peptides.txt was created from previous session
            for file, name in zip([FC.raw_files_e_1,FC.raw_files_e_2, FC.raw_files_e_3], ['elution_data_1','elution_data_2','elution_data_3']):
                if FC.remote_run:
                    raw_file_new_name = os.path.join(FC.path_input_eb, name + '.raw')
                    subprocess.call(["mv", file, raw_file_new_name])
                    logger.info("raw files (elution) were moved to: " + raw_file_new_name)
                else:
                    shutil.move(file, os.path.join(FC.path_input_eb, name+'.raw'))
            FC.raw_files_e_1, FC.raw_files_e_2, FC.raw_files_e_3 = os.path.join(FC.path_input_eb, 'elution_data_1.raw'), \
                                                                   os.path.join(FC.path_input_eb, 'elution_data_2.raw'), \
                                                                   os.path.join(FC.path_input_eb, 'elution_data_3.raw')
            params_e = [FC.raw_files_e_1,FC.raw_files_e_2, FC.raw_files_e_3, FC.db_folder, FC.enzyme, FC.path_input_eb]
            mq.create_xml_config_file(FC.config_folder_eb, params_e, FC.numThreads, FC.config_sample_folder)
            logger.info("mqpar file was created (elution)")
            print("running maxquant (elution)\n")
            logger.info("running maxquant (elution)")
            mq.running_maxquant_through_cmd(FC.config_folder_eb)


        if not(os.path.exists(FC.ft_file)):     #checks if peptides.txt was created from previous session
            for file, name in zip([FC.raw_files_f_1,FC.raw_files_f_2, FC.raw_files_f_3], ['flowthrough_data_1','flowthrough_data_2','flowthrough_data_3']):
                if FC.remote_run:
                    raw_file_new_name = os\
                        .path.join(FC.path_input_ft, name + '.raw')
                    subprocess.call(["mv", file, raw_file_new_name])
                    logger.info("raw files (flowthrough) were moved to: " + raw_file_new_name)
                else:
                    shutil.move(file, os.path.join(FC.path_input_ft, name+'.raw'))
            FC.raw_files_f_1, FC.raw_files_f_2, FC.raw_files_f_3 = os.path.join(FC.path_input_ft, 'flowthrough_data_1.raw'), \
                                                                   os.path.join(FC.path_input_ft, 'flowthrough_data_2.raw'), \
                                                                   os.path.join(FC.path_input_ft, 'flowthrough_data_3.raw')
            params_f = [FC.raw_files_f_1,FC.raw_files_f_2, FC.raw_files_f_3, FC.db_folder, FC.enzyme, FC.path_input_ft]
            mq.create_xml_config_file(FC.config_folder_ft, params_f, FC.numThreads, FC.config_sample_folder)
            logger.info("mqpar file was created (flowthrough)")
            print("running maxquant (flowthrough)\n")
            logger.info("running maxquant (flowthrough)")
            mq.running_maxquant_through_cmd(FC.config_folder_ft)


        print("loading and parsing elution file\n")
        logger.info("loading and parsing elution file")
        eb_data, peptides_dict_eb = util.read_or_new_pickle (FC.IsDebug, path = FC.pickle_file_eb,\
                                                             default = fe.pre_process_on_file(FC.eb_file))


        print("loading and parsing flowthrough file\n")
        logger.info("loading and parsing flowthrough file")
        ft_data, peptides_dict_ft = util.read_or_new_pickle(FC.IsDebug, path = FC.pickle_file_ft,\
                                                            default= fe.pre_process_on_file(FC.ft_file))


        print("check if peptide appears in flowthrow and not elution \n")
        logger.info("check if peptide appears in flowthrow and not elution")
        peptides_list = util.read_or_new_pickle(FC.IsDebug, path = FC.pickle_file_peptides,\
                                                default= fe.check_if_appears_in_flow_through\
                                                    (peptides_dict_eb, peptides_dict_ft, FC.frequency_threshold))


        print("create filtered peptide file\n")
        logger.info("create filtered peptide file")
        fe.create_new_filtered_file(peptides_list, FC.filtered_peptides_file, peptides_dict_eb, peptides_dict_ft)


        print("loading and parsing DB\n")
        logger.info("loading and parsing DB")
        db = util.read_or_new_pickle(FC.IsDebug, path=FC.pickle_file_db, default = dbf.load_db(FC.db_folder))
        #TODO: check why this pickle doesn't work



        print("check if peptide is in DB \n")    #TODO: create a better pickle
        logger.info("check if peptide is in DB ")
        # db_peptides, non_info  = util.read_or_new_pickle(FC.IsDebug, path=FC.pickle_file_db_peptides, \
        #                                         default= dbf.check_if_peptide_in_db \
        #                                         (db, peptides_list))
        if FC.IsDebug == True:
            try:
                non_info = pickle.load(open(FC.pickle_file_non_info, 'rb'))
                db_peptides = pickle.load(open(FC.pickle_file_db_peptides, 'rb'))
            except (OSError, IOError, EOFError):
                db_peptides, non_info = dbf.check_if_peptide_in_db (db, peptides_list)
                pickle._dump(db_peptides, open(FC.pickle_file_db_peptides, 'wb'))
                pickle._dump(non_info, open(FC.pickle_file_non_info, 'wb'))
        else:
            db_peptides, non_info = dbf.check_if_peptide_in_db(db, peptides_list)



        print("creating filtered peptides files according to cdr3\n")   #TODO: create a better pickle
        logger.info("creating filtered peptides files according to cdr3")
        # non_info, info, CDR3_info = util.read_or_new_pickle(FC.IsDebug, path= FC.pickle_file_non_info, \
        #                                                     FC.pickle_file_info, FC.pickle_file_cdr3, \
        #                                                     default= dbf.check_if_cdr3_is_common(db_peptides, non_info))
        if FC.IsDebug == True:
            try:
                non_info = pickle.load(open(FC.pickle_file_non_info, 'rb'))
                info = pickle.load(open(FC.pickle_file_info, 'rb'))
                CDR3_info = pickle.load(open(FC.pickle_file_cdr3, 'rb'))
            except (OSError, IOError, EOFError):
                non_info, info, CDR3_info = dbf.check_if_cdr3_is_common(db_peptides, non_info, FC.overlap_threshold)
                pickle._dump(non_info, open(FC.pickle_file_non_info, 'wb'))
                pickle._dump(info, open(FC.pickle_file_info, 'wb'))
                pickle._dump(CDR3_info, open(FC.pickle_file_cdr3, 'wb'))
        else:
            non_info, info, CDR3_info = dbf.check_if_cdr3_is_common(db_peptides, non_info, FC.overlap_threshold)


        print("creating non info, info and cdr3 info files\n")
        logger.info("creating non info, info and cdr3 info files")
        dbf.create_files(non_info, info, CDR3_info, FC.output_files + 'non_informative_peptides.tsv', \
                                                         FC.output_files + 'informative_peptides.tsv', \
                                                         FC.output_files + 'informative_CDR3_peptides.tsv', \
                                                         peptides_dict_eb, peptides_dict_ft )


        print("create cdr3 analysis\n")
        logger.info("create cdr3 analysis")
        sp.analyze_cdr3(CDR3_info, FC.pictures_folder)

        print("create isotypes distribution\n")
        logger.info("create isotypes distribution")
        sp.generate_alignment_report_pie_chart(FC.pictures_folder + 'Isotypes_distribution.png', CDR3_info)

        print("create peptide plot\n")
        logger.info("create peptide plot")
        sp.plot_peptide_records(CDR3_info, peptides_dict_eb, db_peptides, len(db), FC.pictures_folder + 'proteomics_vs_genetics.png')

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

    if user_email != 'NO_EMAIL':
        send_email('mxout.tau.ac.il', 'TAU BioSequence <bioSequence@tauex.tau.ac.il>', user_email,
                   subject = f'PASA {status}.', content = msg)

    logger.info('PASA is DONE!!')
