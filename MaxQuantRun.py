import subprocess
import xml.etree.cElementTree as ET
from shutil import copyfile
import regex as re
import os.path
from os.path import isfile, join
from xml.etree.ElementTree import Element, SubElement, Comment, tostring


config_sample_folder = ''

def create_xml_config_file (config_folder, params, numThreads):

    config_file = config_folder + 'mqpar.xml'
    copyfile(config_sample_folder + 'mqpar_template.xml', config_file)

    tree = ET.parse(config_folder + 'mqpar.xml',)
    #root = tree.getroot()
    root = ET.Element ('root')

    #raw files
    raw = ET.SubElement(root,'filePaths')
    experiments = ET.SubElement(root,'experiments')
    for file, exp_name  in zip ([params[0], params[1],params[2]] , ['a', 'b', 'c']):
        create_raw_file(file, raw, exp_name , experiments)

    # db files
    fasta_db = ET.SubElement(root, "fastaFiles")
    db_files = [join(params[3], file) for file in os.listdir(params[3])]
    for file in db_files:
        create_fasta_db_file(file, fasta_db)

    enz = ET.SubElement(root, 'enzymes')
    enz.text = params[4]

    thre = ET.SubElement(root, 'numThreads')
    thre.text = numThreads

    create_directories(params[5], root)

    tree.write(open(config_file, 'wb'))


def create_raw_file(raw_file, raw, exp_name, experiment):
    raw_file_obj = ET.SubElement(raw, "string")
    raw_file_obj.text = raw_file
    exp_obj = ET.SubElement(experiment, "string")
    exp_obj.text = exp_name


def create_fasta_db_file (fasta_file, fasta_db):
    fastaFileInfo = ET.SubElement(fasta_db, "FastaFileInfo")
    d1 = ET.SubElement(fastaFileInfo, "fastaFilePath")
    d1.text =  fasta_file
    d2 = ET.SubElement(fastaFileInfo, "identifierParseRule")
    d2.text = '([^\s]*)'
    d3 = ET.SubElement(fastaFileInfo, "descriptionParseRule")
    d3.text = "(.*)"
    d4 = ET.SubElement(fastaFileInfo, "taxonomyParseRule")
    d4.text = ""
    d5 = ET.SubElement(fastaFileInfo, "variationParseRule")
    d5.text = ""
    d6 = ET.SubElement(fastaFileInfo, "modificationParseRule")
    d6.text = ""
    d7 = ET.SubElement(fastaFileInfo, "taxonomyId")
    d7.text = ""



def create_directories(directory, root):
    d1 = ET.SubElement(root, "pluginFolder")
    d1.text = directory
    d2 = ET.SubElement(root, "tempFolder")
    d2.text = directory
    d3 = ET.SubElement(root, "fixedSearchFolder")
    d3.text = directory
    d4 = ET.SubElement(root, "fixedCombinedFolder")
    d4.text = directory






def running_maxquant_through_cmd (config_path):
    maxquant_exe_path = 'mono ' + '/share/apps/maxquant/maxquant-1.6.3.4/bin/MaxQuantCmd.exe'
    #subprocess.call(['module load maxquant/maxquant-1.6.3.4'])      #remove when using cgi
    subprocess.call([maxquant_exe_path, config_path])
    #subprocess.run
    #mono --$maxquant --version
    # MaxQuantCmd 1.6.3.4


