from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import time
import xlrd

from threading import Thread
from pythonosc import  udp_client
#from tasks import

app = Flask(__name__)
app.secret_key = os.urandom(42)

def threaded_task(file):
#     sheet = xlrd.open_workbook(file_contents=file.read()).sheet_by_index(1)
#     print(sheet.nrows)
# 
    client = udp_client.SimpleUDPClient("192.168.0.105", 7771)
    client.send_message('/hey', [440]) # test som skickar OSC meddelande till Supercollider (Sched.scd)

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