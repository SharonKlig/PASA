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

    igh_v_f , igh_d_f, igh_j_f, igh_vd_f , igh_vj_f, igh_dj_f ,igh_vdj_f  = pictures_folder + 'IGH_V_counts.png', \
                                                                  pictures_folder + 'IGH_D_counts.png', \
                                                                  pictures_folder + 'IGH_J_counts.png', \
                                                                  pictures_folder + 'IGH_VD_counts.png',\
                                                                  pictures_folder + 'IGH_VJ_counts.png',\
                                                                  pictures_folder + 'IGH_DJ_counts.png',\
                                                                  pictures_folder + 'IGH_VDJ_counts.png'
    plot_cdr3_length_distributions(CDR3_info , pictures_folder + 'cdr3_length_distributions.png')
    plot_cdr3_combination_distributions(CDR3_info,  igh_v_f , igh_d_f, igh_j_f, igh_vd_f , igh_vj_f, igh_dj_f ,igh_vdj_f)


def plot_cdr3_length_distributions(CDR3_info, file_name):

    CDR3_list = [len(item[4]) for item in CDR3_info]
    length = len(CDR3_list)
    '''
    n, bins, patches = plt.hist(x=CDR3_list, bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Length of CDR3 (AA level)')
    plt.ylabel('Frequency (%)')
    #plt.title('cdr3_length_distributions')
    plt.text(23, 45, r'$\mu=15, b=3$')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.savefig(pictures_folder + 'cdr3_length_distributions.png', dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None,
            transparent=False, bbox_inches=None, pad_inches=0.1,
            frameon=None, metadata=None)
    #plt.show()
    '''

    hist = create_hist (CDR3_list)
    title= 'cdr3_length_distributions'
    x_label, y_label  = '\nLength of CDR3 (AA level)', 'Frequency (%)\n'
    rotation=90
    plot_distributions3(hist, file_name, x_label, y_label, rotation)


def plot_cdr3_combination_distributions(CDR3_info, IGH_V_counts_file, IGH_D_counts_file, IGH_J_counts_file,\
                                        IGH_VD_counts_file, IGH_VJ_counts_file, IGH_DJ_counts_file, IGH_VDJ_counts_file):

    length = len(CDR3_info)

    V_list = [item[5] for item in CDR3_info]
    D_list = [item[6] for item in CDR3_info]
    J_list = [item[7] for item in CDR3_info]

    V_hist, D_hist, J_hist  = create_hist(V_list) , create_hist(D_list), create_hist(J_list)

    VD_combination = [(V_list[i], D_list[i]) for i in range(length)]
    VJ_combination = [(V_list[i], J_list[i]) for i in range(length)]
    DJ_combination = [(D_list[i], J_list[i]) for i in range(length)]

    VD_hist, VJ_hist, DJ_hist = create_hist(create_combintion_of_2(VD_combination)), create_hist(create_combintion_of_2(VJ_combination)), \
                                create_hist(create_combintion_of_2(DJ_combination))

    VDJ_combination = [(V_list[i], D_list[i], J_list[i]) for i in range(length)]

    VDJ_hist = create_hist(create_combintion_of_3(VDJ_combination))


    for item, file in zip([V_hist, D_hist, J_hist, VD_hist, VJ_hist, DJ_hist, VDJ_hist],\
                      [IGH_V_counts_file, IGH_D_counts_file, IGH_J_counts_file, \
                       IGH_VD_counts_file, IGH_VJ_counts_file, IGH_DJ_counts_file,
                       IGH_VDJ_counts_file]):

        type = ((os.path.split(file)[1]).split("_"))[1]
        x_label = (type + ' subgroups combination')
        y_label = ('Frequency (%)')
        plot_distributions3(item, file, x_label, y_label, 90)



def plot_distributions1(histogram, file):

    type = ((os.path.split(file)[1]).split("_"))[1]
    #if type.lower() in ['v', 'd', 'j']:

    n, bins, patches = plt.hist(x=histogram, bins='auto', color = '#0504aa',
                                    alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel(type + ' subgroups combination')
    plt.ylabel('Frequency (%)')
    # plt.title('cdr3_length_distributions')
    plt.text(23, 45, r'$\mu=15, b=3$')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.savefig(file, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                frameon=None, metadata=None)
    #plt.show()


def plot_distributions2(histogram, file):
    type = ((os.path.split(file)[1]).split("_"))[1]
    letter_counts = Counter(histogram)
    df = pandas.DataFrame.from_dict(letter_counts, orient='index')
    df.plot(kind='bar')
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.xlabel(type + ' subgroups combination')
    plt.ylabel('Frequency (%)')
    plt.savefig(file)


def plot_distributions3(hist, file_name, x_label, y_label , rotation):

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


def plot_peptid_records(peptides_elution, db_peptides, pic_path):
    num_of_db_list = []
    elution_counts = []
    list = []

    for peptid, value in db_peptides.items():
        list.append(peptid)
        num_of_db_list.append(len(value))
        elution_counts.append(peptides_elution[peptid][2])
    if(len(num_of_db_list) != len(elution_counts) != len(list)):
        print('error')
    #plt.pyplot.scatter(num_of_db_list, elution_counts, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None,
                          #        alpha=None, linewidths=None, verts=None, edgecolors=None, *, data=None, **kwargs)[source]

    fig, ax = plt.subplots(figsize=(15, 8))
    ax.set_title('Proteomics vs. Genetics')
    ax.set_xlabel('Number of records in DB')
    ax.set_ylabel('counts in the elution')
    #ax.scatter(num_of_db_list, elution_counts, color='r')

    for i, txt in enumerate(list):
        ax.scatter(num_of_db_list[i], elution_counts[i], color='r')
        plt.text(num_of_db_list[i] + 0.3, elution_counts[i] + 0.3, txt, fontsize=5)

        #ax.annotate(txt, (num_of_db_list[i], elution_counts[i]))

    plt.savefig(pic_path)


