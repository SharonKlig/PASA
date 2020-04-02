import logging
import pandas as pd
from openpyxl import Workbook
import xlrd
import csv
import os
import os.path
from pathlib import Path
import sys
from Files_and_Constants import log_file
import numpy as np

logger = logging.getLogger('Logs/PASA_pipeline.log')


def read_from_excel(file):
    if (os.path.isfile(file)) == False:
        logger.error("ERROR, missing file" + file)
    csv.field_size_limit(100000000)
    data =[]
    with open(file, newline='') as f:
        f_reader = csv.DictReader(f, delimiter='\t')#, quoting=csv.QUOTE_NONE)
        for raw in f_reader:
            data.append(dict(raw))
    return (data)


def filter_plus (line):
    return ((line['Reverse'] != '+') and (line['Potential contaminant'] != '+'))


def is_present_in_2_replicates (line, peptide_dict, sum_mean_intensity_all_peptides):      #not fit to csv with sheets
    if line['Sequence'] == "":
        return False
    if not(isinstance(line['Sequence'], str)) :
        logger.error("line is not valid. peptid: " + line['Sequence']+"\n" )
        return False
    try:
        rep1, rep2, rep3 = line['Intensity a'],line['Intensity b'], line['Intensity c']
    except: #only for debugging (old files had these fields)
        try:
            rep1, rep2, rep3 = line['Intensity A'], line['Intensity B'], line['Intensity C']
        except:
            rep1, rep2, rep3 = line['Intensity D'], line['Intensity E'], line['Intensity F']

    try:
        rep1, rep2, rep3 = float(rep1), float(rep2), float(rep3)
    except:
        pass
    cnt = 0
    for rep in [rep1, rep2, rep3]:
        if not (isinstance(rep, float)):
            logger.error("line is not valid. peptid: " + line['Sequence'] + " intensity: " + str(line['Intensity']) + "\n")
            continue
        if rep != 0 :
            cnt += 1
    if cnt >= 2:
        sum_intensity = rep1 + rep2 + rep3
        #calculate mean intensity for each peptid
        mean_intensity = sum_intensity / cnt
        peptide_dict[line['Sequence']] = [mean_intensity, None, sum_intensity]
        sum_mean_intensity_all_peptides[0] += mean_intensity
        return True
    else:
        return False


def pre_process_on_file (file):

    data = read_from_excel(file)
    peptide_dict = {}
    sum_mean_intensity_all_peptides = [0]  #it's a list to update it by refernce

    new_list = [line for line in data if (filter_plus(line) and is_present_in_2_replicates(line, peptide_dict,\
                                                                                    sum_mean_intensity_all_peptides))]

    for key, value in peptide_dict.items():
        value[1] = value[0] / sum_mean_intensity_all_peptides[0] #value[1] is the frequency = "relative intensity out of intensities",
                                                                 # value[0] = mean intensity for each peptide (sum intensity\#replicates)

    return new_list, peptide_dict


def check_if_appears_in_flow_through (peptides_dict_0, peptides_dict_10 , frequency_threshold):
    #0 = eb, 10= ft
    new_data = []
    for key, value in peptides_dict_0.items():
        if not(key in peptides_dict_10):
            new_data.append(key)
        else:
            eb = value[1]
            ft = (peptides_dict_10.get(key))[1]
            frequency_ratio = eb / ft
            if frequency_ratio > frequency_threshold:
                new_data.append(key)
    return (new_data)


def create_new_filtered_file (list, file, peptides_dict_eb, peptides_dict_ft):
    file = open(file, 'wt', newline='')
    tsv_writer = csv.writer(file, delimiter='\t')
    head = ['Peptide_name', 'Average_intensity_elution', 'Average frequency_elution', 'Average_intensity_flowthrough', \
           'Average frequency_flowthrough']
    tsv_writer.writerow(head)
    for item in list:
        eb = peptides_dict_eb.get(item)
        ft =  peptides_dict_ft.get(item)
        if ft == None:
            ft = ['0', '0']
        row = str(item)+'\t'+ str(eb[0])+'\t'+ str(eb[1])+'\t'+ str(ft[0])+'\t'+ str(ft[1])
        file.write(row +"\n")
    file.close()



