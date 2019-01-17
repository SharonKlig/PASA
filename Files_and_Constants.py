import Utilities as util
import logging
import os
import os.path


#CONTANTS and PARAMETERS
Y = 10 #this parameter used when checking the frequencing ratio EB/FT
numThreads = 1
IsDebug = False

remote_run = True if (os.path.exists('/bioseq/PASA')) else False
src_folder = '/bioseq/PASA/' if (remote_run == True) else ''

maxquant_exe_path = '/share/apps/maxquant/maxquant-1.6.3.4/bin/MaxQuantCmd.exe'

#src_folder = '/groups/pupko/kligsberg/pasa_src/'
logs = src_folder + 'Logs/'
db_folder = src_folder + 'DB_files/'
pickle_folder = src_folder + 'Pickles/'
config_sample_folder = src_folder

util.create_dir2(logs)
util.remove_content_dir_or_create(db_folder)
util.create_dir2(pickle_folder)

log_file =logs + 'PASA_pipeline.log'

#pickles files (debugging)
pickle_file_eb = pickle_folder + "pickle_file_eb.pkl"
pickle_file_ft = pickle_folder + "pickle_file_ft.pkl"
pickle_file_peptides = pickle_folder + "pickle_file_peptides.pkl"
pickle_file_db = pickle_folder + "pickle_file_db.pkl"
pickle_file_non_info = pickle_folder + "pickle_file_non_info.pkl"
pickle_file_info = pickle_folder + "pickle_file_info.pkl"
pickle_file_cdr3 = pickle_folder + "pickle_file_cdr3.pkl"
pickle_file_db_peptides = pickle_folder + "pickle_file_db_peptides.pkl"


args = util.parse_parameters()
raw_files_e_1, raw_files_e_2, raw_files_e_3 = args.raw_files_elution_1, args.raw_files_elution_2, args.raw_files_elution_3
raw_files_f_1, raw_files_f_2, raw_files_f_3 = args.raw_files_flowthrough_1, args.raw_files_flowthrough_2, args.raw_files_flowthrough_3
db_file = args.db_file
enzyme = args.digestion_enzyme
wd = args.work_folder
user_email = args.user_email

path_input_eb = os.path.join(wd , "elution_files/")
path_input_ft = os.path.join(wd , "flowthrough_files/")
output_files = os.path.join(wd , "output_files/")
pictures_folder = output_files + "pics/"

util.create_dir2(path_input_eb)
util.create_dir2(path_input_ft)
util.create_dir2(output_files)
util.create_dir2(pictures_folder)

maxquant_output_eb_folder = path_input_eb + "combined/txt/"
maxquant_output_ft_folder = path_input_ft + "combined/txt/"
eb_file = maxquant_output_eb_folder + 'peptides.txt'
ft_file = maxquant_output_ft_folder + 'peptides.txt'

config_folder_eb = path_input_eb
config_folder_ft = path_input_ft
sample_config = src_folder

util.check_if_zip_file (db_file, db_folder)

filtered_peptides_file = output_files + 'filtered_peptides.txt'

file_output_names = ['filtered_peptides.txt', 'informative_CDR3_peptides.tsv',
                  'informative_peptides.tsv', 'non_informative_peptides.tsv',
                  'pics/cdr3_length_distributions.png', 'pics/IGH_D_counts.png',
                  'pics/IGH_V_counts.png', 'pics/IGH_J_counts.png',
                  'pics/IGH_VD_counts.png', 'pics/IGH_VJ_counts.png',
                  'pics/IGH_DJ_counts.png', 'pics/IGH_VDJ_counts.png',
                  'pics/proteomics_vs_genetics.png']

strs_to_show_on_html = ['List of curated peptides', 'List of informative CDR3 peptides',
                        'List of informative NON-CDR3 peptides', 'List of NON informative peptides',
                        'CDR3 length distribution', 'V family subgroup distribution',
                        'D family subgroup distribution', 'J family subgroup distribution',
                        'VD family subgroup distribution', 'VJ family subgroup distribution',
                        'DJ family subgroup distribution', 'VDJ family subgroup distribution',
                        'Proteomics VS Genetics']






