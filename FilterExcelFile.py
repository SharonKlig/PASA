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



def read_from_excel_with_sheets(file):
    '''
    This funcation fits to excel file with multi sheets
    :param file: xlsx file
    :return: res- array with cell for each sheet.
    '''
    if(os.path.isfile(file)) == False:
        logger.error("ERROR, missing file" + file)
    wb = xlrd.open_workbook(file , on_demand=True)
    sheets = wb.sheet_names()
    res = []
    for sheet in sheets:
        worksheet = wb.sheet_by_name(sheet)
        first_row = []
        for col in range(worksheet.ncols):
            first_row.append(worksheet.cell_value(0, col))
        data = []
        for row in range(1, worksheet.nrows):
            record = {}
            for col in range(worksheet.ncols):
                if isinstance(worksheet.cell_value(row, col), str):
                    record[first_row[col]] = worksheet.cell_value(row, col).strip()
                else:
                    record[first_row[col]] = worksheet.cell_value(row, col)
            data.append(record)
        res.append(data)
    return res


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


'''
def filter_confidence_PSM (data):
    new_data = []
    for sheet in data:
        new_list = [line for line in sheet if line['Percolator PEP'] < 1]
        new_data.append(new_list)
    return new_data


def rank_PSM (data):
    new_data = []
    for sheet in data:
        new_list = [line for line in sheet if ((line['XCorr'] > 0.5) and \
                                               (line['Percolator PEP'] < 1) and\
                                               (line['Percolator q-Value'] < 0.9))]
        new_data.append(new_list)
    return new_data
'''

'''
def create_names_dict (data, mode):
    
    ''
    :param data:
    :return:
    mode 1 - in_how_many_sheets_appears_dict - counts in how many sheets (replicates) each peptide appears
    mode 2 - total_names_dict - dict of peptide : how many times appears (sum of all replicates)
    mode 3 - names_dict_per_sheet - for each sheet (replicate), count how many times each peptide appears
    ''
    
    in_how_many_sheets_appears_dict = {}
    total_names_dict = {}
    names_dict_per_sheet = []

    for sheet in data:
        new_names_dict = {}
        for line in sheet:
            name = line.get('Annotated Sequence')
            if name in new_names_dict:
                new_names_dict[name] += 1
                total_names_dict[name] += 1
            else:
                new_names_dict[name] = 1
                if name in total_names_dict:
                    total_names_dict[name] += 1
                else:
                    total_names_dict[name] = 1
                if name in in_how_many_sheets_appears_dict:
                    in_how_many_sheets_appears_dict [name] += 1
                else:
                    in_how_many_sheets_appears_dict [name] = 1
        names_dict_per_sheet.append(new_names_dict)

    if mode == 1:
        return (in_how_many_sheets_appears_dict)
    elif mode == 2:
        return (total_names_dict)
    else :
        return (names_dict_per_sheet)
'''

'''
def is_present_in_2_replicates (data):
    new_data = []
    total_names_dict = create_names_dict(data, 1)

    for sheet in data:
        new_list = [line for line in sheet if (total_names_dict[line.get('Annotated Sequence')] >= 2)]
        new_data.append(new_list)
    return new_data
'''


def is_present_in_2_replicates (line, peptid_dict, sum_mean_intensity_all_peptides):      #not fit to csv with sheets
    if line['Sequence'] == "":
        return False
    if not(isinstance(line['Sequence'], str)) :
        logger.error("line is not valid. peptid: " + line['Sequence']+"\n" )
        return False
    try:
        rep1, rep2, rep3 = line['Intensity A'],line['Intensity B'], line['Intensity C']
    except:
        rep1, rep2, rep3 = line['Intensity a'], line['Intensity b'], line['Intensity c']
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
        peptid_dict[line['Sequence']] = [mean_intensity, None, sum_intensity]
        sum_mean_intensity_all_peptides[0] += mean_intensity
        return True
    else:
        return False


def pre_process_on_file (file):

    data = read_from_excel(file)
    peptid_dict = {}
    #parsed_data = []
    sum_mean_intensity_all_peptides = [0]  #it's a list to update it by refernce
    # for sheet in data:            #if there are multi sheets in excel
    #     new_list = [line for line in sheet if (filter_plus (line) and is_present_in_2_replicates (line, peptid_dict, sum_mean_intensity_all_peptides))]
    #     parsed_data.append(new_list)
    new_list = [line for line in data if (filter_plus(line) and is_present_in_2_replicates(line, peptid_dict, sum_mean_intensity_all_peptides))]
    #parsed_data.append(new_list)

    for key, value in peptid_dict.items():
        value[1] = value[0] / sum_mean_intensity_all_peptides[0]         #value[1] is the "relative intensity out of intensities", value[0] = mean intensity for each peptid (sum intensity\#replicates)

    return new_list, peptid_dict

'''
def check_if_appears_in_flow_through (days0, days10):
    new_data = []
    names_dict1 = create_names_dict(first, 2)
    names_dict2 = create_names_dict(second, 2)
    new_dict = {}
    for key, value in names_dict2.items():
        if not(key in names_dict1):
            new_dict[key] = value
    for sheet in second:
        new_list = [line for line in sheet if line.get('Annotated Sequence') in new_dict]
        new_data.append(new_list)
    return (new_data, new_dict)
'''

def check_if_appears_in_flow_through (peptides_dict_0, peptides_dict_10 , Y):
    #0 = eb, 10= ft
    new_data = []
    for key, value in peptides_dict_0.items():
        if not(key in peptides_dict_10):
            new_data.append(key)
        else:
            eb = value[1]
            ft = (peptides_dict_10.get(key))[1]
            if eb / ft > Y:
                new_data.append(key)

    return (new_data)


def create_new_filtered_file (list, file, peptides_dict_eb, peptides_dict_ft):
    file = open(file, 'wt', newline='')
    tsv_writer = csv.writer(file, delimiter='\t')
    head = ['Peptid_name', 'Average_intensity_elution', 'Average frequency_elution', 'Average_intensity_flowthrough', 'Average frequency_flowthrough']
    #file.write( head + "\n")
    tsv_writer.writerow(head)
    for item in list:
        eb = peptides_dict_eb.get(item)
        ft =  peptides_dict_ft.get(item)
        if ft == None:
            ft = ['0', '0']
        row = str(item)+'\t'+ str(eb[0])+'\t'+ str(eb[1])+'\t'+ str(ft[0])+'\t'+ str(ft[1])
        #tsv_writer.writerow(row)
        file.write(row +"\n")
    file.close()



