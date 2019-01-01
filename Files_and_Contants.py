import Utilities as util
import logging
import os

#hard coded folders
bin = '/groups/pupko/kligsberg/FinalProject/' #so the HOME env variable will be ignored
logs = bin + 'Logs/'
db_folder = bin + 'DB_files/'
pickle_folder = bin + 'Pickles/'
config_sample_folder = bin


#pickles files (debugging)
pickle_file_e = pickle_folder + "pickle_file_e.pkl"
pickle_file_f = pickle_folder + "pickle_file_f.pkl"
pickle_file_p = pickle_folder + "pickle_file_p.pkl"
pickle_file_db = pickle_folder + "pickle_file_db.pkl"
pickle_file_non_info = pickle_folder + "pickle_file_non_info.pkl"
pickle_file_info = pickle_folder + "pickle_file_info.pkl"
pickle_file_cdr3 = pickle_folder + "pickle_file_cdr3.pkl"


args = util.parse_parameters()
raw_files_e_1, raw_files_e_2, raw_files_e_3 = args.raw_files_elution_1, args.raw_files_elution_2, args.raw_files_elution_3
raw_files_f_1, raw_files_f_2, raw_files_f_3 = args.raw_files_flowthrough_1, args.raw_files_flowthrough_2, args.raw_files_flowthrough_3
db_file = args.db_file
enzyme = args.digestion_enzyme
wd = args.work_folder

path_input_e = wd + "/elution_files/"
path_input_f = wd + "/flowthrough_files/"

try:
    os.mkdir (path_input_e)
except FileExistsError:
    logging.info("Directory ", path_input_e, " already exists")
try:
    os.mkdir (path_input_f)
except FileExistsError:
    logging.info("Directory ", path_input_f, " already exists")


maxquant_output_e_folder = path_input_e + "combined/txt/"
maxquant_output_f_folder = path_input_f + "combined/txt/"
day0_file = maxquant_output_e_folder + 'peptides.txt'
day10_file = maxquant_output_f_folder + 'peptides.txt'

config_folder_e = path_input_e
config_folder_f = path_input_f
sample_config = wd

util.check_if_zip_file (db_file, db_folder)

output_files = wd + "output_files/"
pictures_folder = output_files + "pics/"

output = output_files + 'filtered_peptides.txt'

if False: #old paths, without maxquant
    db_folder = 'DB_files/'
    input_folder = 'input_files/'
    output_files = "output_files/"
    day0_file = input_folder + 'elution.xlsx'
    day10_file = input_folder + 'flowthrough.xlsx'
    pictures_folder = output_files + "pics/"
    output = output_files + 'filtered_peptides.txt'

#CONTANTS
Y = 10
numThreads = 8