FROM python:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

RUN cd /
RUN git clone https://github.com/Turkce-Botlar-Sohbet/Tiranozor.git

RUN cd /Tiranozor
WORKDIR /Tiranozor

RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt

CMD python3 bot.py
