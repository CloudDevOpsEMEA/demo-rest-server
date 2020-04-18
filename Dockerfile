FROM python:3

LABEL name="Graphite JSON events to Pickle metrics convertor"
LABEL description="Python based app that ingest Graphite events and forwards them as metrics"
LABEL source-repo="https://github.com/boeboe/demo-rest-server"
LABEL version=${VERSION}

ADD entrypoint.sh /
ADD jsontopickle.py /

ENV BASEPATH ""
ENV DELAY ""
ENV PORT ""
ENV SIZE ""

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
