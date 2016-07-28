# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request
import os, redis, socket

app = Flask(__name__)
app.redis = redis.StrictRedis(host=os.getenv('REDIS_HOST', 'cache'), 
            port=os.getenv('REDIS_PORT', 6379), 
            db=0)


@app.route("/", methods = ['POST', 'GET'])
def main():


    hostname=socket.gethostname()
    ipaddr=socket.gethostbyname(hostname)
    qtde = app.redis.get("curtidas")
    curtidas = int(qtde or 0)

    if (request.method == 'POST'):
        curtidas += 1
        app.redis.set("curtidas", curtidas)

    return render_template('index.html', ipaddr=ipaddr, hostname=hostname, curtidas=curtidas)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)