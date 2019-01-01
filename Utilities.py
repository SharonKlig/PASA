import logging
import sys, argparse
import os
import zipfile
from pyunpack import Archive
import gzip
import tarfile
from shutil import copyfile



logging.basicConfig(filename='Logs/main.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')

#pickles files (debugging)
pickle_folder = 'Pickles/'
pickle_file_e = pickle_folder + "pickle_file_e.pkl"
pickle_file_f = pickle_folder + "pickle_file_f.pkl"
pickle_file_p = pickle_folder + "pickle_file_p.pkl"
pickle_file_db = pickle_folder + "pickle_file_db.pkl"
pickle_file_non_info = pickle_folder + "pickle_file_non_info.pkl"
pickle_file_info = pickle_folder + "pickle_file_info.pkl"
pickle_file_cdr3 = pickle_folder + "pickle_file_cdr3.pkl"


def parse_parameters():

    parser = argparse.ArgumentParser()
    parser.add_argument('raw_files_elution_1', help='full psth of raw file #1 of elution')
    parser.add_argument('raw_files_elution_2', help='full psth of raw file #2 of elution')
    parser.add_argument('raw_files_elution_3', help='full psth of raw file #3 of elution')

    parser.add_argument('raw_files_flowthrough_1', help='full psth of raw file #1 of flowthrough')
    parser.add_argument('raw_files_flowthrough_2', help='full psth of raw file #2 of flowthrough')
    parser.add_argument('raw_files_flowthrough_3', help='full psth of raw file #3 of flowthrough')

    parser.add_argument('db_file', help='file or zip file of db ')
    parser.add_argument('digestion_enzyme', help='digestion_enzyme')
    parser.add_argument('work_folder', help='work directory path')

    args = parser.parse_args()
    return args


def check_if_zip_file (input):
    db_folder = 'DB_files/'
    try:
        os.mkdir(db_folder)
    except FileExistsError:
        logging.info("Directory ", db_folder, " already exists")
    if input.endswith('.zip'):
        f_zip = zipfile.ZipFile(input)
        f_zip.extractall(db_folder)
        f_zip.close()
    elif input.endswith('.gz'):
        tar = tarfile.open(input)
        tar.extractall(db_folder)
        tar.close()
    elif input.endswith('.rar'):
        Archive('a.zip').extractall(db_folder)
    else:
        copyfile(input, db_folder + input.split('/')[-1])


