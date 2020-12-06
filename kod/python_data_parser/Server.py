from cgmparser.Parser import Parser as parser
import time as timer
from pythonosc import udp_client
import argparse

times, values = parser().parse_data("kj@jondell.com.xls")

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="localhost")
parser.add_argument("--port", default=7771)
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)

def send_osc_message(message):
    client.send_message("/filter", float(message))

while True:
    for index, time in enumerate(times[1:100]):
        timer.sleep(0.1)
        send_osc_message(values[index]-values[index+1])
