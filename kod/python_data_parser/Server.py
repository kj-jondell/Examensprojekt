from cgmparser.Parser import Parser as parser
import time as timer
from pythonosc import udp_client
import argparse

times, values = parser().parse_data("kj@jondell.com3.xls")
#times, values = parser().parse_data("kj@jondell.com.xls")

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1")
parser.add_argument("--port", default=7771)
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)

def send_osc_message(message):
    client.send_message("/filter", float(message))

for index, time in enumerate(times):
    timer.sleep(0.005)
    #send_osc_message(values[index]/20.0)
    try:
        send_osc_message(values[index]-values[index+1])
    except:
        pass
