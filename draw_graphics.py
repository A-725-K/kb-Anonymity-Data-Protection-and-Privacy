import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def read_data():
    ks = defaultdict(lambda: defaultdict(dict))
    with open('tmp', 'r', encoding='utf-8') as f:
        l = f.readline().rstrip() 
        while l:
            t = l.split(' ')  
            
            ks[t[4]][t[0]][t[3]] = (t[1], t[2]) #path_coverange, execution_time
            l = f.readline().rstrip() 
    return ks


def print_time_graphic(ks):
    print_graphic(ks, 1)

def print_coverage_graphic(ks):
    print_graphic(ks, 0)

def print_graphic(ks, flag):
    labels = ['P-F', 'P-T']
    for k, sizes in ks.items():
        #print(k,algs)
        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars
        fig, ax = plt.subplots()
        ax.set_ylabel('Execution Time') if flag == 1 else ax.set_ylabel('Path Coverage')
        ax.set_title('K = ' + k)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        legend = []
        rects = []
        i = width*int(len(sizes)/2)*(-1)  #serve per formattare la distanza tra le varie dimensioni 
        for size, algs in sizes.items():
            times = []
            legend += [size]
            for alg, values in algs.items():
                times += [float(values[flag])]
            rects += [ax.bar(x + i, times, width, label=size)]
            i += width
        
        for r in rects:
            autolabel(r,ax)
        ax.legend(legend)
        fig.tight_layout()
        plt.show()
    


ks = read_data()
print_time_graphic(ks)
print_coverage_graphic(ks)



