import logging
import sys, argparse
import os
import zipfile
#from pyunpack import Archive
import gzip
import tarfile
from shutil import copyfile
import patoolib
from distutils.dir_util import copy_tree
import pickle
import shutil
import csv
import openpyxl
import scipy as sp
#from Files_and_Constants import log_file

logger = logging.getLogger('Logs/PASA_pipeline.log')



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
    parser.add_argument('user_email', help='user email')

    args = parser.parse_args()
    return args



def read_or_new_pickle(IsDebug, path, default):
    '''
    if dubug mode is off, dont ever use pickles.
    if dubug mode is on, check if pickle is available and load it or create a new one if not.
    '''
    if IsDebug == False:
        return default
    else:
        if os.path.isfile(path):
            with open(path, "rb") as f:
                try:
                    return pickle.load(f)
                except Exception:
                    pass
        with open(path, "wb") as f:
            pickle.dump(default, f)
        return default




def check_if_zip_file (input, db_folder):

    if input.endswith('.zip'):
        f_zip = zipfile.ZipFile(input)
        f_zip.extractall(db_folder)
        f_zip.close()
    elif input.endswith('.gz') or input.endswith('.tar.gz'):
        tar = tarfile.open(input)
        tar.extractall(db_folder)
        tar.close()
        try: #if there is a sub folder inside the folder
            sub_folder = input.split('/')[-1].replace('.tar.gz' , '')
            copy_tree(db_folder + sub_folder, db_folder)
        except:
            pass
    elif input.endswith('.rar'):
        patoolib.extract_archive(input, outdir=db_folder)
    elif input.endswith('.fasta'):
        copyfile(input, db_folder + input.split('/')[-1])
    else:
        print("invalid format")



def create_dir1(path):
    try:
        os.makedirs(path)
        logger.info(f'Creating directory: {path}')
    except OSError as exception:
        logger.info(f'Directory already exists: {path}')


def create_dir2(path):
    if os.path.exists(path):
        logger.info(f'Directory already exists: {path}')
    else:
        logger.info(f'Creating directory: {path}')
        os.makedirs(path)


def remove_content_dir_or_create(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

