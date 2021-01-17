from cgmparser.Parser import Parser as parser
from pythonosc import udp_client
from Calculator import Calculator
import argparse
import numpy

times, values = parser().parse_csv_data(filename="Karl JohannesJondell_glucose_7-12-2020.csv")
zipped_lists = zip(times, values)
sorted_list = sorted(zipped_lists)

print(numpy.mean(values), numpy.median(values), numpy.max(values), numpy.min(values))
# parser = argparse.ArgumentParser()
# parser.add_argument("--ip", default="127.0.0.1")
# parser.add_argument("--port", default=7771)
# args = parser.parse_args()
# client = udp_client.SimpleUDPClient(args.ip, args.port)
# 
# def send_osc_message(time_value, value):
#     client.send_message("/value", value)
#     client.send_message("/time", time_value)
# 
# for time_value, value in sorted_list:
#     send_osc_message(time_value, value)
# 
# # skicka medelvärde (mean, mode, median), max o min, 
# client.send_message("/meta", [numpy.mean(values)])
# 
# client.send_message("/done", "")
