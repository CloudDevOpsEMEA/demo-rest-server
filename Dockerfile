FROM python:3

LABEL name="Python3 Flask based web application for demo purposes"
LABEL description="The server runs on a given port and basepath. It exposes a number of REST endpoints that are handy for demo purposes on application behavior."
LABEL source-repo="https://github.com/boeboe/demo-rest-server"
LABEL version=${VERSION}

RUN pip install Flask

ADD entrypoint.sh /
ADD demoserver.py /

ENV BASEPATH ""
ENV DELAY ""
ENV PORT ""
ENV SIZE ""

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
