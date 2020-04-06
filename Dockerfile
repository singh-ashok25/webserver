from centos:latest

RUN yum -y install python3 
RUN pip3 install flask
RUN yum -y install git

RUN git clone https://github.com/singh-ashok25/webserver.git
WORKDIR /webserver

#COPY . /webserver
EXPOSE 4080

ENTRYPOINT ["python3"]
CMD ["app2.py"]
