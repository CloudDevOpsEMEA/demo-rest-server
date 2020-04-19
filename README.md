# Small HTTP/REST demo server

## Introduction

This is a small Python3 Flask based web application for demo purposes.

The server runs on a given port and basepath. It exposes a number of 
REST endpoints that are handy for demo purposes on application behavior.

Supported endpoints, starting from a set or overridden basepath, are

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
 - delay (*) : for endpoints with delay functionality
 - size (**) : for the binary endpoint

## How to run

The source and docker image are available on Github and Dockerhub at

 - https://github.com/boeboe/demo-rest-server
 - https://hub.docker.com/repository/docker/boeboe/demo-rest-server

In order to run the docker image

```console
# docker run --name restserver
             -p 8008:9000
             -e BASEPATH="/api/v1"
             -e DELAY="10"
             -e PORT="9000"
             -e SIZE="2048"
             boeboe/demo-rest-server

# docker run --name restserver
             -p 8008:8000
             boeboe/demo-rest-server
```

All ENV variables are optional

 - BASEPATH : the base url for your endpoints (default: "/api")
 - DELAY    : delay from slow endpoints (default: 5)
 - PORT     : the tcp port to serve this web application (default: 8000)
 - SIZE     : return size of your binary endpoint in bytes (default: 1024)


## Example usage

The following examples use [httpie](https://httpie.org) as command line http client

```console
>>>>>>>>>> ${print help} <<<<<<<<<<
# http localhost:8000/
HTTP/1.0 200 OK
Content-Length: 1765
Content-Type: text/plain; charset=utf-8
Date: Sat, 18 Apr 2020 23:06:45 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

This is a mock web application to demo HTTP/REST behaviour
----------------------------------------------------------

Supported endpoints, starting from a basepath '/api', are

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
    (*) delay : for endpoints with delay functionality (default 5)
    (**) size : for the binary endpoint (default 1024)

>>>>>>>>>> ${create an object using http rest post} <<<<<<<<<<
# http -f POST  localhost:8000/api/201
HTTP/1.0 201 CREATED
Content-Length: 70
Content-Type: text/html; charset=utf-8
Date: Sat, 18 Apr 2020 23:06:51 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

{
    "code": 201,
    "message": "you have successfully created a new object"
}

>>>>>>>>>> ${retrieve an object using http rest get} <<<<<<<<<<
# http localhost:8000/api/200
HTTP/1.0 200 OK
Content-Length: 69
Content-Type: text/html; charset=utf-8
Date: Sat, 18 Apr 2020 23:07:02 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

{
    "code": 200,
    "message": "you have successfully retrieved an object"
}

>>>>>>>>>> ${do an http partial update of an object} <<<<<<<<<<
# http -f PATCH localhost:8000/api/202
HTTP/1.0 202 ACCEPTED
Content-Length: 78
Content-Type: text/html; charset=utf-8
Date: Sun, 19 Apr 2020 13:57:43 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

{
    "code": 202,
    "message": "your request to partially modify has been accepted"
}

>>>>>>>>>> ${do an http update of an object} <<<<<<<<<<
# http -f PUT localhost:8000/api/200
HTTP/1.0 200 OK
Content-Length: 68
Content-Type: text/html; charset=utf-8
Date: Sun, 19 Apr 2020 13:58:13 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

{
    "code": 200,
    "message": "you have successfully updated and object"
}

>>>>>>>>>> ${do an http rest delete of an object} <<<<<<<<<<
# http -f DELETE localhost:8000/api/204
HTTP/1.0 204 NO CONTENT
Content-Type: text/html; charset=utf-8
Date: Sat, 18 Apr 2020 23:07:20 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

>>>>>>>>>> ${get a 503 http response code} <<<<<<<<<<
# http localhost:8000/api/503
HTTP/1.0 503 SERVICE UNAVAILABLE
Content-Length: 47
Content-Type: text/html; charset=utf-8
Date: Sat, 18 Apr 2020 23:07:28 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

{
    "code": 503,
    "message": "service unavailable"
}

>>>>>>>>>> ${get a 404 http response code} <<<<<<<<<<
# http localhost:8000/api/404
HTTP/1.0 404 NOT FOUND
Content-Length: 37
Content-Type: text/html; charset=utf-8
Date: Sat, 18 Apr 2020 23:07:32 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

{
    "code": 404,
    "message": "not found"
}

>>>>>>>>>> ${get a random http response code} <<<<<<<<<<
# http localhost:8000/api/random
HTTP/1.0 503 SERVICE UNAVAILABLE
Content-Length: 43
Content-Type: text/html; charset=utf-8
Date: Sat, 18 Apr 2020 23:07:36 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

{
    "code": 503,
    "message": "random response"
}

>>>>>>>>>> ${get a random http response code} <<<<<<<<<<
# http localhost:8000/api/random
HTTP/1.0 204 NO CONTENT
Content-Type: text/html; charset=utf-8
Date: Sat, 18 Apr 2020 23:07:37 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

>>>>>>>>>> ${will only respond after 10sec} <<<<<<<<<<
# http localhost:8000/api/slow?delay=10 
zsh: no matches found: localhost:8000/api/slow?delay=10
# http "localhost:8000/api/slow?delay=10"
HTTP/1.0 200 OK
Content-Length: 41
Content-Type: text/html; charset=utf-8
Date: Sat, 18 Apr 2020 23:08:31 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

{
    "code": 200,
    "message": "slow response"
}

>>>>>>>>>> ${respond with binary data of certain size} <<<<<<<<<<
# http "localhost:8000/api/binary?size=10"
HTTP/1.0 200 OK
Cache-Control: public, max-age=43200
Content-Length: 10
Content-Type: application/octet-stream
Date: Sat, 18 Apr 2020 23:08:49 GMT
Expires: Sun, 19 Apr 2020 11:08:49 GMT
Server: Werkzeug/1.0.1 Python/3.8.2

]ڡ�F�ǋ7
```

## Note

This container is purely used for demo purposes and not meant for production 
environments at all. 
