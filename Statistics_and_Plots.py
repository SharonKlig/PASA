import logging
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas
from collections import Counter


def analyze_cdr3(CDR3_info, pictures_folder):

    igh_v_f , igh_d_f, igh_j_f, igh_vd_f , igh_vj_f, igh_dj_f ,igh_vdj_f  = pictures_folder + 'IGH_V_counts.png', \
                                                                  pictures_folder + 'IGH_D_counts.png', \
                                                                  pictures_folder + 'IGH_J_counts.png', \
                                                                  pictures_folder + 'IGH_VD_counts.png',\
                                                                  pictures_folder + 'IGH_VJ_counts.png',\
                                                                  pictures_folder + 'IGH_DJ_counts.png',\
                                                                  pictures_folder + 'IGH_VDJ_counts.png'
    plot_cdr3_length_distributions(CDR3_info , pictures_folder)
    plot_cdr3_combination_distributions(CDR3_info,  igh_v_f , igh_d_f, igh_j_f, igh_vd_f , igh_vj_f, igh_dj_f ,igh_vdj_f)


def plot_cdr3_length_distributions(CDR3_info, pictures_folder):
    CDR3_list = [len(item[4]) for item in CDR3_info]
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


def plot_cdr3_combination_distributions(CDR3_info, IGH_V_counts_file, IGH_D_counts_file, IGH_J_counts_file,\
                                        IGH_VD_counts_file, IGH_VJ_counts_file, IGH_DJ_counts_file, IGH_VDJ_counts_file):
    V_list = [item[5] for item in CDR3_info]
    D_list = [item[6] for item in CDR3_info]
    J_list = [item[7] for item in CDR3_info]

    for item, file in zip([V_list, D_list, J_list], [IGH_V_counts_file, IGH_D_counts_file, IGH_J_counts_file]):
        plot_distributions2(item, file)

    lengh = len(V_list)

    VD_combination = [(V_list[i],D_list[i]) for i in range (lengh)]
    VJ_combination = [(V_list[i], J_list[i]) for i in range(lengh)]
    DJ_combination = [(D_list[i], J_list[i]) for i in range(lengh)]

    for item, file in zip([create_combintion_of_2(VD_combination), create_combintion_of_2(VJ_combination),\
                           create_combintion_of_2(DJ_combination)], \
                          [IGH_VD_counts_file, IGH_VJ_counts_file, IGH_DJ_counts_file]):
        plot_distributions2(item, file)

    VDJ_combination = [(V_list[i], D_list[i], J_list[i]) for i in range(lengh)]
    plot_distributions2(create_combintion_of_3(VDJ_combination) , IGH_VDJ_counts_file)




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



def plot_peptid_records(peptides_list, peptides_dict_0, db_peptides, pic_path):
    num_of_db_list = []
    elution_counts = []
    for peptid in peptides_list:
        num_of_db_list.append(len(db_peptides[peptid]))
        elution_counts.append(peptides_dict_0[peptid][0])
    if(len(num_of_db_list) != len(elution_counts) != len(peptides_list)):
        print('error')
    #plt.pyplot.scatter(num_of_db_list, elution_counts, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None,
                          #        alpha=None, linewidths=None, verts=None, edgecolors=None, *, data=None, **kwargs)[source]

    fig, ax = plt.subplots()
    ax.scatter(num_of_db_list, elution_counts)

    for i, txt in enumerate(peptides_list):
        ax.annotate(txt, (num_of_db_list[i], elution_counts[i]))

    plt.savefig(pic_path)