FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip curl dnsutils
RUN apt install dnsutils
RUN pip3 install flask jproperties requests

COPY sender.py /refit/sender.py

WORKDIR /refit/

EXPOSE 8080

ENTRYPOINT ["python3", "sender.py"]