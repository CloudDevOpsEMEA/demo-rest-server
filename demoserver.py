#!/usr/bin/env python3
'''
This is a small mocke web application to simulate a broken application
'''
import argparse
import io
import os
import random
import time
from flask import Flask, json, make_response, redirect, request, send_file, url_for

APP = Flask(__name__)
BASEPATH = "/api"
DELAY = 5
PORT = 8000
SIZE = 1024

def get_http_help():
    '''Return help'''

    return '''
This is a mock web application to demo HTTP/REST behaviour
----------------------------------------------------------

Supported endpoints, starting from a basepath '{}', are

    /200 or /200_ok                    : GET/POST/PUT/DELETE/PATCH
    /201 or /201_created               : POST/PUT
    /202 or /202_accepted              : POST/PUT/DELETE/PATCH
    /204 or /204_no_content            : POST/PUT/DELETE/PATCH
    /302 or /302_found                 : GET/POST/PUT/DELETE/PATCH
    /307 or /307_temporary_redirect    : GET/POST/PUT/DELETE/PATCH
    /400 or /400_bad_request           : GET/POST/PUT/DELETE/PATCH
    /401 or /401_unauthorized          : GET/POST/PUT/DELETE/PATCH
    /403 or /403_forbidden             : GET/POST/PUT/DELETE/PATCH
    /404 or /404_not_found             : GET/POST/PUT/DELETE/PATCH
    /405 or /405_not_allowed           : GET/POST/PUT/DELETE/PATCH
    /500 or /500_internal_server_error : GET/POST/PUT/DELETE/PATCH
    /503 or /503_service_unavailable   : GET/POST/PUT/DELETE/PATCH
    /random                            : GET for response with random http return code
    /slow                              : GET for slow responses with 200 OK (*)
    /slow_random                       : GET for slow responses with random http return code (*)
    /various_delay                     : GET for random delay response with 200 OK (*)
    /various_delay_random              : GET for random delay response with random http return code (*)
    /binary                            : GET for binary data responses (**)
    <others>                           : This help

Optional request query parameters:
    (*) delay : for endpoints with delay functionality (default {})
    (**) size : for the binary endpoint (default {})
'''.format(BASEPATH, DELAY, SIZE)

def get_return_body(*, code, msg):
    '''Returns JSON bodies'''
    return json.dumps({"code": code, "message": msg})

#####################
### 2xx Responses ###
#####################

@APP.route(BASEPATH + "/200", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/200_ok", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_200_ok():
    '''HTTP 200 (Ok)'''
    if request.method == "GET":
        return get_return_body(code=200, msg="you have successfully retrieved an object"), 200
    if request.method == "POST":
        return get_return_body(code=200, msg="you have successfully performed an action"), 200
    if request.method == "PUT":
        return get_return_body(code=200, msg="you have successfully updated and object"), 200
    if request.method == "DELETE":
        return get_return_body(code=200, msg="you have successfully deleted an object"), 200
    if request.method == "PATCH":
        return get_return_body(code=200, msg="you have successfully partially updated an object"), 200
    return "", 200

@APP.route(BASEPATH + "/201", methods=["POST", "PUT"])
@APP.route(BASEPATH + "/201_created", methods=["POST", "PUT"])
def post_201_ok():
    '''HTTP 201 (Created)'''
    return get_return_body(code=201, msg="you have successfully created a new object"), 201

@APP.route(BASEPATH + "/202", methods=["POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/202_accepted", methods=["POST", "PUT", "DELETE", "PATCH"])
def post_202_accepted():
    '''HTTP 202 (Accepted)'''
    if request.method == "POST":
        return get_return_body(code=202, msg="your request to create a new object has been accepted"), 202
    if request.method == "PUT":
        return get_return_body(code=202, msg="your request to update an object has been accepted"), 202
    if request.method == "DELETE":
        return get_return_body(code=202, msg="your request to delete an object has been accepted"), 202
    if request.method == "PATCH":
        return get_return_body(code=202, msg="your request to partially modify has been accepted"), 202
    return "", 202

@APP.route(BASEPATH + "/204", methods=["POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/204_no_content", methods=["POST", "PUT", "DELETE", "PATCH"])
def get_204_no_content():
    '''HTTP 204 (No Content)'''
    return "", 204

#####################
### 3xx Responses ###
#####################

@APP.route(BASEPATH + "/302", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/302_found", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_302_found():
    '''HTTP 302 (Found)'''
    return redirect(url_for('200'), 302, get_return_body(code=302, msg="found"))

@APP.route(BASEPATH + "/307", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/307_temporary_redirect", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_307_temporary_redirect():
    '''HTTP 307 (Temporary Redirect)'''
    return redirect(url_for('200'), 307, get_return_body(code=307, msg="temporary redirect"))

#####################
### 4xx Responses ###
#####################

@APP.route(BASEPATH + "/400", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/400_bad_request", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_400_bad_request():
    '''HTTP 400 (Bad Request)'''
    return get_return_body(code=400, msg="bad request"), 400

@APP.route(BASEPATH + "/401", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/401_unauthorized", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_401_unauthorized():
    '''HTTP 401 (Unauthorized)'''
    return get_return_body(code=401, msg="unauthorized"), 401

@APP.route(BASEPATH + "/403", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/403_forbidden", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_403_forbidded():
    '''HTTP 403 (Forbidden)'''
    return get_return_body(code=403, msg="forbidden"), 403

@APP.route(BASEPATH + "/404", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/404_not_found", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_404_not_found():
    '''HTTP 404 (Not found)'''
    return get_return_body(code=404, msg="not found"), 404

@APP.route(BASEPATH + "/405", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/405_not_allowed", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_405_not_allowed():
    '''HTTP 405 (Not Allowed)'''
    return get_return_body(code=404, msg="not allowed"), 405

#####################
### 5xx Responses ###
#####################

@APP.route(BASEPATH + "/500", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/500_internal_server_error", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_500_internal_server_error():
    '''HTTP 500 (Internal Server Error)'''
    return get_return_body(code=500, msg="internal server error"), 500

@APP.route(BASEPATH + "/503", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route(BASEPATH + "/503_service_unavailable", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def get_503_service_unavailable():
    '''HTTP 503 (Service Unavailable)'''
    return get_return_body(code=503, msg="service unavailable"), 503


#########################
### Special Responses ###
#########################

@APP.route(BASEPATH + "/random", methods=["GET"])
def get_random():
    '''Random response'''
    responses = [200, 201, 202, 204, 302, 307, 400, 401, 403, 404, 500, 503]
    code = random.choice(responses)
    return get_return_body(code=code, msg="random response"), code

@APP.route(BASEPATH + "/slow", methods=["GET"])
def get_slow():
    '''Slow response'''
    time.sleep(DELAY if "delay" not in request.args else int(request.args["delay"]))
    return get_return_body(code=200, msg="slow response")

@APP.route(BASEPATH + "/slow_random", methods=["GET"])
def get_slow_random():
    '''Slow and random response'''
    time.sleep(DELAY if "delay" not in request.args else int(request.args["delay"]))
    responses = [200, 201, 202, 204, 302, 307, 400, 401, 403, 404, 500, 503]
    code = random.choice(responses)
    return get_return_body(code=code, msg="random slow response"), code

@APP.route(BASEPATH + "/various_delay", methods=["GET"])
def get_various_delay():
    '''Various response delay'''
    time.sleep(random.randint(0, DELAY if "delay" not in request.args else int(request.args["delay"])))
    return get_return_body(code=200, msg="various delay response")

@APP.route(BASEPATH + "/various_delay_random", methods=["GET"])
def get_various_delay_random():
    '''Various and random response delay'''
    responses = [200, 201, 202, 204, 302, 307, 400, 401, 403, 404, 500, 503]
    code = random.choice(responses)
    time.sleep(random.randint(0, DELAY if "delay" not in request.args else int(request.args["delay"])))
    return get_return_body(code=code, msg="random various delay response"), code

@APP.route(BASEPATH + "/binary", methods=["GET"])
def binary():
    """Send back random binary data"""
    return send_file(io.BytesIO(os.urandom(SIZE if "size" not in request.args else int(request.args["size"]))),
                     attachment_filename='random.file', mimetype='application/octet-stream')

@APP.route('/', defaults={'path': ''}, methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@APP.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def catch_all(path):
    """Print help with the available endpoints"""
    response = make_response(get_http_help(), 200)
    response.mimetype = "text/plain"
    print("Path received: '{}'".format(path))
    return response, 200


###########################
### Program starts here ###
###########################

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("-b", "--basepath", default="/api", type=str, help="the base url for your endpoints")
    PARSER.add_argument("-d", "--delay", default=5, type=int, help="delay from slow endpoints")
    PARSER.add_argument("-p", "--port", default=8000, type=int, help="the tcp port to serve this web application")
    PARSER.add_argument("-s", "--size", default=1024, type=int, help="return size of your binary endpoint in bytes")
    ARGS = PARSER.parse_args()

    if ARGS.basepath:
        BASEPATH = ARGS.basepath
    if ARGS.delay:
        DELAY = ARGS.delay
    if ARGS.port:
        PORT = ARGS.port
    if ARGS.size:
        SIZE = ARGS.size

    print("Going to start webserver on port {} with basepath '{}'".format(PORT, BASEPATH))    
    APP.run(host="0.0.0.0", port=PORT)
