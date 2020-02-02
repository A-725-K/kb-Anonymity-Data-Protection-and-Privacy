import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict


# Attach a text label above each bar in *rects*, displaying its height
def autolabel(rects, ax, flag):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{0:.3f} s'.format(height) if flag else '{0:.2f} %'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom')


# read data to plot from a temporary file
def read_data(tmp_file):
    ks = defaultdict(lambda: defaultdict(dict))
    with open(tmp_file, 'r', encoding='utf-8') as f:
        l = f.readline().rstrip() 
        while l:
            t = l.split(' ')  
            ks[t[4]][t[0]][t[3]] = (t[1], t[2]) #path_coverange, execution_time
            l = f.readline().rstrip()
    return ks


def print_time_graphic(ks):
    print_graphic(ks, True)


def print_coverage_graphic(ks):
    print_graphic(ks, False)


# generate a graphic for a property for each algorithm
def print_graphic(ks, flag):
    labels = ['P-F', 'P-T']
    for k, sizes in ks.items():
        #print(k, algs)
        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars

        fig, ax = plt.subplots()
        ax.set_ylabel('Execution Time [s]') if flag else ax.set_ylabel('Path Coverage [%]')
        ax.set_xlabel('Algorithm')
        ax.set_title('K = ' + k)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        
        legend = []
        rects = []
        i = width * int(len(sizes)/2) * (-1)  # to format the distance bewteen dimensions 
        for size, algs in sizes.items():
            times = []
            legend += [str(size) + ' tuples']
            for alg, values in algs.items():
                times += [float(values[flag])]
            rects += [ax.bar(x + i, times, width, label=size)]
            i += width
        
        for r in rects:
            autolabel(r, ax, flag)

        ax.legend(legend, title='Tuples per dataset')
        fig.tight_layout()
        #plt.show()
        plt.savefig('../stat/ExecutionTime{}.png'.format(k) if flag else '../stat/PathCoverage{}.png'.format(k))


############
### MAIN ###
############

ks = read_data('tmp')
print_time_graphic(ks)
print_coverage_graphic(ks)
