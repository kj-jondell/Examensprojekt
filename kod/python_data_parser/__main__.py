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

sheet = xlrd.open_workbook("kj@jondell.com.xls").sheet_by_index(SHEET_NO)

times, values = parse_data(sheet)
spl = BSpline(times, values, k = 1)
spl_list = []

for value in range(times[-1]):
    spl_list.append(spl(value))

plt.plot(range(times[-1]), spl_list)
plt.show()


