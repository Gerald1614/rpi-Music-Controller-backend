## Synopsis

This is the backend for a project where I wanted to control a ChromeCast Audio with a Raspberry Pi using zero touch technologies.

## Description of the main project

The project is developped in three services that are all hosted on a single RPI (I chose this architecture to get possibilities to separate those services in different servers if needed and also get easier way to maintain those services)

The RPI is controlling over the WIFI a Chromecast Audio to play predefined channels based on inputs that are managed by no-contact devices. an RFID card reader enable the use to start a specific channel, a distance sensor can stop the music or change the volume. 
I also added a temperature captor that combined to a call to Openweather API can interupt the music to give meteo information with the help of Google Text-to_speech API.
The application is splitted in three tiers:
* a client controls all the captors and Inputs/Outputs of the RPI
* An MQTT server receives all changes of states through messages
* a backend send request to the chromecast based on events coming through MQTT and also expose streams required to play channels or meteo information that is built on the flight with the help of google text to speech API.

## Technlogies used

* Raspberry Pi 3B
* RFID-RC522 Reader
* BME280
* HC-SR04
* Openweathermap API
* Google Text-to-Speech API
* PyChromecast library
* Docker
* Mosquitto MQTT

In order to facilitate deployment of the applications, I deployed docker on the raspberry pi and used Docker-Compose to run the apps. it is super usefull.

## the back end 

The backend is based on Python code. I leverage the pychromecast library and just built one application to pass the right commands to pychromecast based on messaging coming from the MQTT server. this is also th place where docker-compose stands to deploy the threee tiers.

## Installation

> clone this repository as well as the client repository
> cd rpi_server
> 'docker-compose -f docker-compose.yml up --build'

that's it