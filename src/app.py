# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request
import socket

app = Flask(__name__)


@app.route("/")
def main():

    hostname=socket.gethostname()
    ipaddr=socket.gethostbyname(hostname)

    return render_template('index.html', ipaddr=ipaddr, hostname=hostname)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)