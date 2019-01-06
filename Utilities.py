import logging
import sys, argparse
import os
import zipfile
#from pyunpack import Archive
import gzip
import tarfile
from shutil import copyfile
#import patoolib
from distutils.dir_util import copy_tree
import pickle




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



def read_or_new_pickle(path, default):
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
        sub_folder = input.split('/')[-1].replace('.tar.gz' , '')
        copy_tree(db_folder + sub_folder, db_folder)
    #elif input.endswith('.rar'):
     #   patoolib.extract_archive(input, outdir=db_folder)
    elif input.endswith('.fasta'):
        copyfile(input, db_folder + input.split('/')[-1])
    else:
        print("invalid format")




#

