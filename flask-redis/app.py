from flask import Flask, jsonify, request
from redis import StrictRedis

import os


app = Flask(__name__)


@app.route('/guestbook/')
def redis():

    if 'cmd' in request.args:

        host = 'redis-master'
        if os.environ.get('GET_HOSTS_FROM') == 'env':
            host = os.environ.get('REDIS_MASTER_SERVICE_HOST')

        if request.args.get('cmd') == 'set':

            r = StrictRedis(host=host, port=6379)
            r.set(request.args.get('key'), request.args.get('value'))
            return jsonify(message='Updated')

        else:

            host = 'redis-slave'
            if os.environ.get('GET_HOSTS_FROM') == 'env':
                host = os.environ.get('REDIS_SLAVE_SERVICE_HOST')

            r = StrictRedis(host=host, port=6379)
            value = r.get(request.args.get('key')) or b''
            return jsonify(data=value.decode('utf-8'))
