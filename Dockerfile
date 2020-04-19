FROM python:3-alpine
LABEL name seqparser
LABEL src "https://github.com/remiflavien1/seqparser"
LABEL dockerfile fractalizers
RUN pip3 install seqparser
ENTRYPOINT ["seqparser"]
CMD ["-h"]