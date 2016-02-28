FROM ubuntu:14.04
RUN apt-get install -y python
ADD . /src
WORKDIR /src
CMD ["python", "sleep.py", "10"]
