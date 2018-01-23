FROM ubuntu:14.04
RUN apt-get update && apt-get install -y python2.7
ADD . /src
WORKDIR /src
CMD ["python2.7", "sleep.py", "10"]
