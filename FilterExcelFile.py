import pandas as pd
from openpyxl import Workbook
import xlrd
import csv
import os.path
from pathlib import Path


def read_from_excel(file):
    if(os.path.isfile(file)) == False:
        print("ERROR, missing file")
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


def create_names_dict (data, mode):
    '''

    :param data:
    :return:
    mode 1 - in_how_many_sheets_appears_dict - counts in how many sheets (replicates) each peptide appears
    mode 2 - total_names_dict - dict of peptide : how many times appears (sum of all replicates)
    mode 3 - names_dict_per_sheet - for each sheet (replicate), count how many times each peptide appears
    '''
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


def is_present_in_2_replicates (data):
    new_data = []
    total_names_dict = create_names_dict(data, 1)

    for sheet in data:
        new_list = [line for line in sheet if (total_names_dict[line.get('Annotated Sequence')] >= 2)]
        new_data.append(new_list)
    return new_data


def pre_process_on_file (file):
    data1 =  read_from_excel(file)
    data2 = filter_confidence_PSM(data1)
    data3 = rank_PSM (data2)
    data4 = is_present_in_2_replicates (data3)
    return data1            #change to data4 (this mode only for test)


def check_if_appears_in_flow_through (first, second):
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


def create_new_filtered_file (dict, file):
    file = open(file, 'w')
    for key, value in dict.items():
        file.write(str(key)+ "\t" + str(value) +"\n")
    file.close()







