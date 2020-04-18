# Small HTTP/REST demo server

## Introduction

This is a small Python3 Flask based web application for demo purposes.

The server runs on a given port and basepath. It exposes a number of 
REST endpoints that are handy for demo purposes on application behavior.

Supported endpoints, starting from a set or overridden <basepath>, are

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
    (*) delay : for endpoints with delay functionality
    (**) size : for the binary endpoint

## How to run

The docker image is available on Dockerhub at

https://hub.docker.com/repository/docker/boeboe/demo-rest-server

In order to run the docker image

```console
# docker run --name restserver  -p 8008:9000 -e BASEPATH="/api/v1" -e DELAY="10" -e PORT="9000" -e SIZE="2048" boeboe/demo-rest-server
# docker run --name restserver  -p 8008:8000 boeboe/demo-rest-server
```

All ENV variables are optional

 - BASEPATH : the base url for your endpoints (default: "/api")
 - DELAY    : delay from slow endpoints (default: 5)
 - PORT     : the tcp port to serve this web application (default: 8000)
 - SIZE     : return size of your binary endpoint in bytes (default: 1024)

## Note

This container is purely used for demo purposes and not meant for production 
environments at all. 