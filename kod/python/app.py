from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import time
import xlrd

from threading import Thread
from pythonosc import  udp_client

from cgmparser.Parser import Parser

#from tasks import

app = Flask(__name__)
app.secret_key = os.urandom(42)

def threaded_task(file):
#     sheet = xlrd.open_workbook(file_contents=file.read()).sheet_by_index(1)
#     print(sheet.nrows)
# 
    times, values = Parser().parse_data(user_file=file.read())
    #values = Calculator.get_differentiated(values, 0.5) # step_size = 1, to not scale data...
    client = udp_client.SimpleUDPClient("localhost", 7771)
    for value in values:
        client.send_message('/value', value) # test som skickar OSC meddelande till Supercollider (Sched.scd)
    client.send_message('/valueDone', '') # test som skickar OSC meddelande till Supercollider (Sched.scd)

@app.route('/uploader', methods=['GET', 'POST'])
def upload_new_file():
    if request.method == 'POST':
        f = request.files['file']

        thread = Thread(target=threaded_task, args=(f,))
        thread.daemon = True
        thread.start()

        return "Upload successful!"

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug = True)
