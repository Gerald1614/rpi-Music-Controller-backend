FROM python:3

WORKDIR /usr/src/app

COPY ./pychromecast12/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip3 install paho-mqtt
RUN pip install pychromecast