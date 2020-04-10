FROM centos:latest

RUN yum -y install python3 
RUN pip3 install flask

WORKDIR /webserver

COPY . /webserver
EXPOSE 4080

ENTRYPOINT ["python3"]
CMD ["app2.py"]
