FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip curl
RUN pip3 install flask jproperties

COPY sender.py /refit/sender.py 

WORKDIR /refit/

EXPOSE 8080

ENTRYPOINT ["python3", "sender.py"]