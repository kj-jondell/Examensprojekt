from cgmparser.Parser import Parser
from pathlib import Path
from pythonosc import udp_client
from Calculator import Calculator
import numpy
import io
import time
import xlrd

class DataSender:

    def __init__(self):
        self.client = udp_client.SimpleUDPClient("localhost", 7771)

    def send_file(self, file):
        extension = Path(file.filename).suffix
        if extension == ".csv":
            times, values = Parser().parse_csv_data(stream=io.StringIO(file.stream.read().decode("UTF-8"), newline=None))
        elif extension in [".xls", ".xlsx"]:
            times, values = Parser().parse_data(user_file=file.read())
        else:
            return

        # client.send_message('/newPackage', '') # implementera start-flagg
        for value in values:
            self.client.send_message('/value', value) # test som skickar OSC meddelande till Supercollider (Sched.scd)
        self.client.send_message('/valueDone', '') # test som skickar OSC meddelande till Supercollider (Sched.scd)

# times, values = parser().parse_csv_data(filename="Karl JohannesJondell_glucose_7-12-2020.csv")
# values = Calculator.get_differentiated(values, 0.5) # step_size = 1, to not scale data...
# #zipped_lists = zip(times, values)
# #sorted_list = sorted(zipped_lists)
# 
# print(numpy.mean(values), numpy.median(values), numpy.max(values), numpy.min(values))
# parser = argparse.ArgumentParser()
# parser.add_argument("--ip", default="127.0.0.1")
# parser.add_argument("--port", default=7771)
# args = parser.parse_args()
# client = udp_client.SimpleUDPClient(args.ip, args.port)
# 
# client.send_message("/newPacket", "differentiated")
# 
# def send_osc_message(value, time_value=None):
#     client.send_message("/value", value)
# 
#     if time_value != None:
#         client.send_message("/time", time_value)
#     
# for value in values:
#     send_osc_message(value)
# 
# # for time_value, value in sorted_list:
# #     send_osc_message(time_value, value)
# # 
# # # skicka medelvärde (mean, mode, median), max o min, 
# # client.send_message("/meta", [numpy.mean(values)])
# # 
# client.send_message("/done", "")
# 