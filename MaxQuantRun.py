import subprocess
import xml.etree.cElementTree as ET
from shutil import copyfile
import regex as re
import os.path
from os.path import isfile, join
from xml.etree.ElementTree import Element, SubElement, Comment, tostring



def create_xml_config_file (config_folder, params, numThreads, config_sample_folder):

    sample_config = config_sample_folder + 'mqpar_template.xml'
    config_file = config_folder + 'mqpar.xml'
    copyfile(sample_config , config_file)

    tree = ET.parse(sample_config)
    #root = tree.getroot()
    root = tree.getroot ()

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
    enz.attrib = params[4]

    thre = ET.SubElement(root, 'numThreads')
    thre.attrib = numThreads

    create_directories(params[5], root)

    tree.write(config_file)


def create_raw_file(raw_file, raw, exp_name, experiment):
    raw_file_obj = ET.SubElement(raw, "string")
    raw_file_obj.attrib = raw_file
    exp_obj = ET.SubElement(experiment, "string")
    exp_obj.attrib = exp_name


def create_fasta_db_file (fasta_file, fasta_db):
    fastaFileInfo = ET.SubElement(fasta_db, "FastaFileInfo")
    d1 = ET.SubElement(fastaFileInfo, "fastaFilePath")
    d1.attrib =  fasta_file
    d2 = ET.SubElement(fastaFileInfo, "identifierParseRule")
    d2.attrib = '([^\s]*)'
    d3 = ET.SubElement(fastaFileInfo, "descriptionParseRule")
    d3.attrib = "(.*)"
    d4 = ET.SubElement(fastaFileInfo, "taxonomyParseRule")
    d4.attrib = ""
    d5 = ET.SubElement(fastaFileInfo, "variationParseRule")
    d5.attrib = ""
    d6 = ET.SubElement(fastaFileInfo, "modificationParseRule")
    d6.attrib = ""
    d7 = ET.SubElement(fastaFileInfo, "taxonomyId")
    d7.attrib = ""



def create_directories(directory, root):
    d1 = ET.SubElement(root, "pluginFolder")
    d1.attrib = directory
    d2 = ET.SubElement(root, "tempFolder")
    d2.attrib = directory
    d3 = ET.SubElement(root, "fixedSearchFolder")
    d3.attrib = directory
    d4 = ET.SubElement(root, "fixedCombinedFolder")
    d4.attrib = directory






def running_maxquant_through_cmd (config_path):
    config_file = config_path + 'mqpar.xml'
    maxquant_exe_path = '/share/apps/maxquant/maxquant-1.6.3.4/bin/MaxQuantCmd.exe'
    #subprocess.call(['module load maxquant/maxquant-1.6.3.4'])      #remove when using cgi
    subprocess.run(['mono', maxquant_exe_path, config_file])
    #args = maxquant_exe_path + config_path
    #subprocess.run(['maxquant', config_path])
    #subprocess.call(args, stdout=NULL, stderr=NULL, shell=False)
    #os.system(maxquant_exe_path + config_path)

