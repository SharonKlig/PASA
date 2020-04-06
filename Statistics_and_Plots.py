import logging
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas
from collections import Counter
import seaborn as sns
#from Files_and_Constants import *

logger = logging.getLogger('Logs/PASA_pipeline.log')



def analyze_cdr3(CDR3_info, pictures_folder):

    plot_cdr3_length_distributions(CDR3_info , pictures_folder)
    plot_cdr3_combination_distributions(CDR3_info,  pictures_folder)


def plot_cdr3_length_distributions(CDR3_info, output_folder):

    length = len(CDR3_info)
    CDR3_IGH_list = [len(item[4]) for item in CDR3_info if item[9] == 'IGH']
    CDR3_IGK_list = [len(item[4]) for item in CDR3_info if item[9] == 'IGK']
    CDR3_IGL_list = [len(item[4]) for item in CDR3_info if item[9] == 'IGL']

    if (len(CDR3_IGH_list) + len(CDR3_IGK_list) +len(CDR3_IGL_list) != length):
        print('something is wrong. check')

    cdr3_distr_igh_f, cdr3_distr_igk_f, cdr3_distr_igl_f = output_folder + 'cdr3_IGH_length_distributions.png', \
                                                           output_folder + 'cdr3_IGK_length_distributions.png', \
                                                           output_folder + 'cdr3_IGL_length_distributions.png'

    for list, file_name in zip([CDR3_IGH_list ,CDR3_IGK_list ,CDR3_IGL_list] , [cdr3_distr_igh_f, cdr3_distr_igk_f, cdr3_distr_igl_f]):
        if len(list) == 0:
            continue
        type = ((os.path.split(file_name)[1]).split("_"))[1]
        hist = create_hist(list)
        title = 'cdr3_length_' + type + '_distributions'
        x_label, y_label = '\nLength of CDR3 (AA level)', 'Frequency (%)\n'
        rotation = 90
        plot_distributions(hist, file_name, x_label, y_label, rotation)


def plot_cdr3_combination_distributions(CDR3_info, output_folder):

    CDR3_IGH_list = [item for item in CDR3_info if item[9] == 'IGH']
    CDR3_IGK_list = [item for item in CDR3_info if item[9] == 'IGK']
    CDR3_IGL_list = [item for item in CDR3_info if item[9] == 'IGL']

    for list, chain_type in zip ([CDR3_IGH_list, CDR3_IGK_list, CDR3_IGL_list] , ['IGH', 'IGK', 'IGL']):

        length = len(list)
        if length == 0:
            continue

        V_list = [item[5] for item in list]
        J_list = [item[7] for item in list]
        if chain_type == 'IGH':
            D_list = [item[6] for item in list]

        V_hist, J_hist  = create_hist(V_list), create_hist(J_list)
        if chain_type == 'IGH':
            D_hist = create_hist(D_list)

        VJ_combination = [(V_list[i], J_list[i]) for i in range(length)]
        if chain_type == 'IGH':
            VD_combination = [(V_list[i], D_list[i]) for i in range(length)]
            DJ_combination = [(D_list[i], J_list[i]) for i in range(length)]

        VJ_hist= create_hist(create_hist(create_combintion_of_2(VJ_combination)))

        if chain_type == 'IGH':
            VD_hist, DJ_hist = create_hist(create_combintion_of_2(VD_combination)), create_hist(create_combintion_of_2(DJ_combination))
            VDJ_combination = [(V_list[i], D_list[i], J_list[i]) for i in range(length)]
            VDJ_hist = create_hist(create_combintion_of_3(VDJ_combination))

        IGx_V_counts_file, IGx_D_counts_file, IGx_J_counts_file, IGx_VD_counts_file, IGx_VJ_counts_file, \
        IGx_DJ_counts_file, IGx_VDJ_counts_file = output_folder + chain_type + '_V_counts.png', \
                                                  output_folder + chain_type + '_D_counts.png', \
                                                  output_folder + chain_type + '_J_counts.png', \
                                                  output_folder + chain_type + '_VD_counts.png', \
                                                  output_folder + chain_type + '_VJ_counts.png', \
                                                  output_folder + chain_type + '_DJ_counts.png', \
                                                  output_folder + chain_type + '_VDJ_counts.png'

        if chain_type == 'IGH':
            for item, file in zip([V_hist, D_hist, J_hist, VD_hist, VJ_hist, DJ_hist, VDJ_hist],\
                                [IGx_V_counts_file, IGx_D_counts_file, IGx_J_counts_file, IGx_VD_counts_file, IGx_VJ_counts_file, \
                                IGx_DJ_counts_file, IGx_VDJ_counts_file]):

                type = ((os.path.split(file)[1]).split("_"))[1]
                x_label = (type + ' subgroups combination')
                y_label = ('Frequency (%)')
                plot_distributions(item, file, x_label, y_label, 90)

        else:
            for item, file in zip([V_hist, J_hist, VJ_hist], \
                                  [IGx_V_counts_file,IGx_J_counts_file,IGx_VJ_counts_file]):
                type = ((os.path.split(file)[1]).split("_"))[1]
                x_label = (type + ' subgroups combination')
                y_label = ('Frequency (%)')
                plot_distributions(item, file, x_label, y_label, 90)


def plot_distributions(hist, file_name, x_label, y_label, rotation):

    x_values = sorted(hist)
    y_values = [hist[x] for x in x_values]
    sum_y_values = sum(y_values) / 100
    y_values = [round(y / sum_y_values, 2) for y in y_values]

    logger.debug(x_values)
    logger.debug(y_values)

    barplot = sns.barplot(x_values, y_values, color='mediumslateblue')
    ylim = [0, 1.2 * max(y_values)]
    if len(x_values) < 20:
        fontsize = 10
    elif len(x_values) < 60:
        fontsize = 5
    else:
        fontsize = 2
    barplot.set_ylim(ylim)
    barplot.set_xticklabels(x_values, rotation=rotation, fontsize=fontsize)
    barplot.set_xlabel(x_label)
    barplot.set_ylabel(y_label)

    plt.tight_layout()
    plt.savefig(file_name, dpi=500, bbox_inches='tight')
    plt.close()


def create_combintion_of_2(list):
    new_list =[]
    for i in range(len(list)):
        new_list.append(str(list[i][0]) + ' ' + str(list[i][1]))
    return (new_list)


def create_combintion_of_3(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(str(list[i][0]) + ' ' + str(list[i][1])+ ' ' + str(list[i][2]))
    return (new_list)


def create_hist (data):
    hist = {}
    for i in data:
        hist[i] = hist.get(i, 0) + 1
    return hist


def plot_peptide_records(CDR3_info, peptides_elution, db_peptides, num_of_db_records, output_path):
    if len(CDR3_info) == 0:
        return
    clonotype_frequency_list = []
    elution_relative_freq = []
    list_of_cdr3 = []
    dots_colors = []
    colors = {
        'IGH': 'red',
        'IGL': 'green',
        'IGK': 'purple'
    }

    for item in CDR3_info:
        peptide = item[0]
        list_of_cdr3.append(item[4])
        elution_relative_freq.append(peptides_elution[peptide][1])
        clonotype_frequency_list.append(len(db_peptides.get(peptide))/num_of_db_records)
        dots_colors.append(colors[item[9]])

    if(len(clonotype_frequency_list) != len(elution_relative_freq) != len(list_of_cdr3)):
        print('error')


    fig, ax = plt.subplots(figsize=(15, 8))
    ax.set_title('Proteomics vs. Genetics')
    ax.set_xlabel('Clonotype frequency')
    ax.set_ylabel('Relative frequency in the elution')

    for i, txt in enumerate(list_of_cdr3):
        ax.scatter(clonotype_frequency_list[i], elution_relative_freq[i], color='r')
        plt.scatter(clonotype_frequency_list[i], elution_relative_freq[i], marker='x', color=dots_colors[i])
        plt.text(clonotype_frequency_list[i], elution_relative_freq[i], txt, fontsize=7, color='black')

    plt.savefig(output_path)
    plt.close()


def generate_alignment_report_pie_chart(output_path, CDR3_info, run=None):

    cdr_isotype = [item[8] for item in CDR3_info]
    hist = create_hist(cdr_isotype)

    isotypes = sorted(hist, key=hist.get, reverse=True)
    portions = [hist[isotype] for isotype in isotypes]

    portions_percents = [100*portions[i]/sum(portions) for i in range(len(portions)) if portions[i]!=0]
    isotypes = [isotypes[i] for i in range(len(isotypes)) if portions[i]!=0]
    labels = ['{} ({:.3f}%)'.format(isotypes[i], portions_percents[i]) for i in range(len(portions_percents))]

    patches, texts = plt.pie(portions_percents, counterclock=False)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    if not run:
        run = 'Replicate '+ output_path[output_path.find('run')+len('run')]
    plt.savefig(output_path, dpi=500, bbox_inches='tight')
    plt.close()