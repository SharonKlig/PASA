import subprocess
import xml.etree.ElementTree as ET
from shutil import copyfile
import regex as re
import os.path
from os.path import isfile, join
from xml.etree.ElementTree import Element, SubElement, Comment, tostring



def create_xml_config_file(config_folder, params, numThreads, config_sample_folder):

    sample_config = config_sample_folder + 'mqpar_template.xml'
    config_file = config_folder + 'mqpar.xml'
    #copyfile(sample_config, config_file)

    tree = ET.parse(sample_config)
    # root = tree.getroot()
    root = tree.getroot()


    # raw files
    rawFilesobj = root.find('filePaths')
    rawFilesobj2 = rawFilesobj.findall('string')
    experiments = root.find('experiments')
    experiments2 = experiments.findall('string')
    for file_name, exp_name, i in zip([params[0], params[1], params[2]], ['a', 'b', 'c'], [0, 1, 2]):
         create_raw_file(file_name, rawFilesobj2, exp_name, experiments, i)


    #db files
    fasta_db = root.find('fastaFiles')
    db_files = [join(params[3], file) for file in os.listdir(params[3])]
    for file in db_files:
        create_fasta_db_file(file, fasta_db)

    root.find('parameterGroups/parameterGroup/enzymes/string').text = params[4]

    root.find('numThreads').text = str(numThreads)

    create_directories(params[5], root)

    tree.write(config_file)
    #new_tree = ET.tostringlist(tree, encoding="us-ascii", method="xml")
    #new_tree.write(config_file)


def create_raw_file(file_name, rawFilesobj, exp_name, experiments, i):
        rawFilesobj[i].text = file_name
        experiments[i].text = exp_name



def create_fasta_db_file(fasta_file, fasta_db):
    fastaFileInfo = ET.SubElement(fasta_db, "FastaFileInfo")
    d1 = ET.SubElement(fastaFileInfo, "fastaFilePath")
    d1.text = fasta_file
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
    ET.dump(fasta_db)




def create_directories(directory, root):
    root.find('pluginFolder').text = directory
    root.find('tempFolder').text = directory
    root.find('fixedSearchFolder').text = directory
    root.find('fixedCombinedFolder').text = directory






def running_maxquant_through_cmd (config_path):
    config_file = config_path + 'mqpar.xml'
    maxquant_exe_path = '/share/apps/maxquant/maxquant-1.6.3.4/bin/MaxQuantCmd.exe'
    #subprocess.call(['module load maxquant/maxquant-1.6.3.4'])      #remove when using cgi
    subprocess.run(['mono', maxquant_exe_path, config_file])
    #args = maxquant_exe_path + config_path
    #subprocess.run(['maxquant', config_path])
    #subprocess.call(args, stdout=NULL, stderr=NULL, shell=False)
    #os.system(maxquant_exe_path + config_path)

