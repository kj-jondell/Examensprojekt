import xlrd 
from scipy.interpolate import BSpline
import matplotlib.pyplot as plt
from dateutil import parser

ROW_OFFSET = 5
SHEET_NO = 1

def parse_data(sheet):
    amt_data = sheet.nrows - ROW_OFFSET
    base_time = 0
    times = []
    values = []
    for row in range(amt_data):
        ### read and interpret data.
        date_string = sheet.cell_value(rowx = ROW_OFFSET + row, colx = 0)
        glucose_level = sheet.cell_value(rowx = ROW_OFFSET + row, colx = 1)

        date = parser.parse(date_string)
        values.append(glucose_level)

        if base_time == 0:
            base_time = date
        times.append((int)((date-base_time).total_seconds()/60))
    return times, values

def plot_interpolated_values(times, values, show_plot=True, savefig=False):
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
Plots differentiated list and returns
"""
def plot_differentiated_values(values, show_plot=True, title="Differentiated values", order=1, savefig=False):
    diff_list = []
    for index, value in enumerate(values):
        if index>0:
            diff_list.append((value-values[index-1])/(15)) #h = 15, step size...

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

    

sheet = xlrd.open_workbook("kj@jondell.com.xls").sheet_by_index(SHEET_NO)
times, values = parse_data(sheet)
plot_interpolated_values(times[:100], values[:100], False, savefig=True)
#plot up to fifth order differentiation
names = ["First", "Second", "Third", "Fourth", "Fifth"]
differentiated_values = values[:100]
for order in range(len(names)):
    differentiated_values = plot_differentiated_values(differentiated_values, False, order = order+1,  title=f"{names[order]}-order differentiated", savefig=True)

#plt.show()

# first_order = plot_differentiated_values(values[:100], False, title="First order differentiated")
# second_order = plot_differentiated_values(first_order, False, title="Second order differentiated", order=2)
# third_order = plot_differentiated_values(second_order, title="Third order differentiated", order=3)
