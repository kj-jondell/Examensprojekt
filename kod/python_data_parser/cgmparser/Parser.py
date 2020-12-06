import xlrd 
from dateutil import parser

ROW_OFFSET = 5
SHEET_NO = 1

class Parser():

    """Docstring for Parser. """

    def __init__(self):
        pass
        
    def parse_data(self, filename):
        sheet = xlrd.open_workbook(filename).sheet_by_index(SHEET_NO)
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
