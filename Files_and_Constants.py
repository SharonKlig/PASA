import Utilities as util
import logging
import os
import os.path


#CONTANTS and PARAMETERS
IsDebug = False
numThreads = 8

remote_run = True if (os.path.exists('/bioseq/PASA')) else False
src_folder = '/bioseq/PASA/' if (remote_run == True) else ''

maxquant_exe_path = '/share/apps/maxquant/maxquant-1.6.3.4/bin/MaxQuantCmd.exe'
maxquant_version = '1.6.3.4'

#src_folder = '/groups/pupko/kligsberg/pasa_src/'       #debugging

pickle_folder = src_folder + 'Pickles/'
config_sample_folder = src_folder

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
frequency_threshold = float(args.frequency_threshold)
wd = args.work_folder
#user_email = args.user_email
#job_title = args.job_title

run_number = wd.split('/')[-2]
html_path = os.path.join(wd, 'output.html')
user_email_file = os.path.join(wd, 'user_email.txt')
job_title_file = os.path.join(wd, 'job_title.txt')

logs = os.path.join(wd , "Logs/")
db_folder = os.path.join(wd , 'DB_files/')

util.create_dir(logs)
util.create_dir(db_folder)
util.create_dir(pickle_folder)

log_file =logs + 'PASA_pipeline.log'

path_input_eb = os.path.join(wd , "elution_files")
path_input_ft = os.path.join(wd , "flowthrough_files")
output_files = os.path.join(wd , "output_files/")
pictures_folder = output_files + "pics/"

util.create_dir(path_input_eb)
util.create_dir(path_input_ft)
util.create_dir(output_files)
util.create_dir(pictures_folder)

maxquant_output_eb_folder = os.path.join(path_input_eb ,"combined", "txt")
maxquant_output_ft_folder = os.path.join(path_input_ft ,"combined", "txt")
eb_file = os.path.join(maxquant_output_eb_folder , 'peptides.txt')
ft_file = os.path.join(maxquant_output_ft_folder , 'peptides.txt')

config_folder_eb = path_input_eb
config_folder_ft = path_input_ft
sample_config = src_folder

util.check_if_zip_file (db_file, db_folder)

filtered_peptides_file = output_files + 'filtered_peptides.txt'

all_file_output_names = ['filtered_peptides.txt', 'informative_CDR3_peptides.tsv',
                  'informative_peptides.tsv', 'non_informative_peptides.tsv',
                  'pics/cdr3_IGH_length_distributions.png', 'pics/cdr3_IGL_length_distributions.png',
                  'pics/cdr3_IGK_length_distributions.png', 'pics/IGH_D_counts.png',
                  'pics/IGH_V_counts.png', 'pics/IGH_J_counts.png',
                  'pics/IGH_VD_counts.png', 'pics/IGH_VJ_counts.png',
                  'pics/IGH_DJ_counts.png', 'pics/IGH_VDJ_counts.png',
                  'pics/IGK_V_counts.png', 'pics/IGK_J_counts.png',
                  'pics/IGK_VJ_counts.png', 'pics/IGL_V_counts.png',
                  'pics/IGL_J_counts.png', 'pics/IGL_VJ_counts.png',
                  'pics/Isotypes_distribution.png',
                  'pics/proteomics_vs_genetics.png']

all_strs_to_show_on_html = ['List of curated peptides', 'List of informative CDR3 peptides',
                        'List of informative NON-CDR3 peptides', 'List of NON informative peptides',
                        'CDR3 IGH length distribution', 'CDR3 IGL length distribution',
                         'CDR3 IGK length distribution' ,'IGH D family subgroup distribution',
                        'IGH V family subgroup distribution', 'IGH J family subgroup distribution',
                        'IGH VD family subgroup distribution', 'IGH VJ family subgroup distribution',
                        'IGH DJ family subgroup distribution', 'IGH VDJ family subgroup distribution',
                        'IGK V family subgroup distribution', 'IGK J family subgroup distribution',
                        'IGK VJ family subgroup distribution', 'IGL V family subgroup distribution',
                        'IGL J family subgroup distribution', 'IGL VJ family subgroup distribution',
                        'Isotypes distribution', 'Proteomics VS Genetics']






