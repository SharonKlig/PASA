import logging
import pandas as pd
from openpyxl import Workbook
import xlrd
import csv
import os
import os.path
from pathlib import Path



def read_from_excel(file):
    '''
    This funcation fits to excel file with multi sheets
    :param file: xlsx file
    :return: res- array with cell for each sheet.
    '''
    if(os.path.isfile(file)) == False:
        logging.error("ERROR, missing file" + file)
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


def filter_plus (line):
    if ((line['Reverse'] != '+') and (line['Potential contaminant'] != '+')):
        return True
    else:
        return False

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
        logging.error("line is not valid. peptid: " + line['Sequence']+"\n" )
        return False
    try:
        rep1, rep2, rep2 = line['Intensity A'],line['Intensity B'], line['Intensity C']
    except:
        rep1, rep2, rep2 = line['Intensity D'], line['Intensity E'], line['Intensity F']
    cnt = 0
    for rep in [rep1, rep2, rep2]:
        if not(isinstance(rep, float)):
            logging.error("line is not valid. peptid: " + line['Sequence'] + " intensity: " + str(line['Intensity'])+"\n")
            continue
        if rep != 0 :
            cnt += 1
    if cnt >= 2:
        sum_intensity = rep1 + rep2 + rep2
        #calculate mean intensity for each peptid
        mean_intensity = sum_intensity / cnt
        peptid_dict[line['Sequence']] = [mean_intensity, None]
        sum_mean_intensity_all_peptides[0] += mean_intensity
        return True
    else:
        return False


def pre_process_on_file (file):

    data =  read_from_excel(file)
    peptid_dict = {}
    parsed_data = []
    sum_mean_intensity_all_peptides = [0]
    for sheet in data:
        new_list = [line for line in sheet if (filter_plus (line) and is_present_in_2_replicates (line, peptid_dict, sum_mean_intensity_all_peptides))]
        parsed_data.append(new_list)
    for key, value in peptid_dict.items():
        value[1] = value[0] / sum_mean_intensity_all_peptides[0]

    return parsed_data, peptid_dict

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


def create_new_filtered_file (list, file):
    file = open(file, 'w')
    for item in list:
        file.write(item +"\n")
    file.close()







