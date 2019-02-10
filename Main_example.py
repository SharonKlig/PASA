import logging
import argparse
import os
import Utilities as util
import html_editor as he
import sys
import time
import Files_and_Constants as FC



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
logger.info('...example pipeline begins...')



if __name__ == '__main__':

    msg = f'job number = {FC.job_title}.\n'

    try:

        output_url = os.path.join(CONSTS.WEBSERVER_RESULTS_URL, 'example', 'output.html')

        file_output_names, strs_to_show_on_html = [], []
        for i, file in enumerate(FC.all_file_output_names):
            if os.path.isfile(os.path.join(FC.output_files , file)):
                file_output_names.append(file)
                strs_to_show_on_html.append(FC.all_strs_to_show_on_html[i])

        status = 'is done'
        msg += f'PASA pipeline {status}.\n'
        time.sleep(1)
        he.edit_success_html(FC.html_path, FC.output_files, FC.run_number, CONSTS, file_output_names,\
                          strs_to_show_on_html)


    except Exception:

        status = 'was failed :('
        time.sleep(1)
        msg += f'PASA pipeline {status}.\n'
        he.edit_failure_html(FC.html_path, FC.run_number, msg, CONSTS)


    if status == 'is done':
        results_location = output_url if FC.remote_run else FC.wd
        msg += f' Results can be found at {results_location}.'



    send_email('mxout.tau.ac.il', 'TAU BioSequence <bioSequence@tauex.tau.ac.il>', FC.user_email,
               subject=f'PASA {status}.', content=msg)

    logger.info('PASA is DONE!!')
