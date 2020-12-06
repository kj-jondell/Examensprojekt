from scipy.interpolate import BSpline
import matplotlib.pyplot as plt
import numpy
import scipy.fftpack 
import scipy.signal
from cgmparser.Parser import Parser as parser

def plot_interpolated_values(times, values, show_plot=False, savefig=False):
    spl = BSpline(times, values, k = 1)
    spl_list = []

    for index in range(times[-1]):
        spl_list.append(spl(index))

    fig = plt.figure()
    plt.plot(range(times[-1]), spl_list)
    fig.suptitle("Interpolated values")
    plt.xlabel("Time [min]")
    plt.ylabel("Blood glucose level [mmol/L]")
    plt.tight_layout()
    if savefig:
        plt.savefig("interpolated.png")
    if show_plot:
        plt.show()

"""
Calculates differentiated list
"""
def get_differentiated(values):
    diff_list = []
    for index, value in enumerate(values):
        if index>0:
            diff_list.append((value-values[index-1])/(15)) #h = 15, step size...
    return diff_list 

"""
Plots differentiated list and returns
"""
def plot_differentiated_values(values, show_plot=False, title="Differentiated values", order=1, savefig=False):
    diff_list = get_differentiated(values)

    fig = plt.figure()
    plt.plot([value * 15 for value in range(len(diff_list))], diff_list, '-ok') # measures each 15 min...
    fig.suptitle(title)
    plt.xlabel("Time [min]")
    plt.ylabel(f"Blood glucose level [mmol/(Lmin^-{order})]")
    plt.tight_layout()
    if savefig:
        plt.savefig(f"{order}st-order.png")
    if show_plot:
        plt.show()
    return diff_list

def plot_fft(values, T = 1.0/800.0):
    N  = len(values)
    x = numpy.linspace(0.0, N*T, N)
    yf = scipy.fftpack.fft(values)
    xf = numpy.linspace(0.0, int(1.0/(2.0*T)), int(N/2))

    plt.plot(xf, 2.0/N * numpy.abs(yf[:N//2]))

index = 0
base_time = 0
import csv
import dateutil
with open('Karl JohannesJondell_glucose_7-12-2020.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    for row in reader:
        if index<10:
            try:
                #print(dateutil.parser.parse(row[2]))
                if index == 0:
                    base_time = dateutil.parser.parse(row[2])
                else:
                    print(int((dateutil.parser.parse(row[2])-base_time).total_seconds()/60))
            except:
                continue
            try:
                print(float(row[4].replace(',','.')))
            except:
                continue
            index = index+1

#times, values = parser().parse_data("kj@jondell.com.xls")
#plot_interpolated_values(times[:1000], values[:1000])
#plt.figure()
#plot_fft(values)
#plt.figure()
#differentiated = values
#for ind in range(10):
#    differentiated = get_differentiated(differentiated)
#plot_fft(differentiated)
#plot_interpolated_values(times[:1000], differentiated[:1000])
#plt.show()

# plot_interpolated_values(times[:100], values[:100], False, savefig=False)
# plot up to fifth order differentiation
# names = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight", "Ninth", "Tenth"]
# differentiated_values = values[:100]
# for order in range(len(names)):
#     differentiated_values = plot_differentiated_values(differentiated_values, False, order = order+1,  title=f"{names[order]}-order differentiated", savefig=False)
# 
# plt.show()

# first_order = plot_differentiated_values(values[:100], False, title="First order differentiated")
# second_order = plot_differentiated_values(first_order, False, title="Second order differentiated", order=2)
# third_order = plot_differentiated_values(second_order, title="Third order differentiated", order=3)
