
import time
import sys
import json
import logging
import paho.mqtt.client as mqtt
import pychromecast

global cast
cast = pychromecast.Chromecast('192.168.2.17')
cast.wait()

print("{0}" .format(cast.device))
time.sleep(1)
print("{0}" .format(cast.status))

if '--show-status-only' in sys.argv:
    sys.exit()
if not cast.is_idle:
    print("Killing current running app")
    cast.quit_app()
    time.sleep(5)
global mc
mc = cast.media_controller

def cc_action(payload):
    if payload["action"] == "play":
        mc.play_media(payload["desc"], "audio/mp3")
        time.sleep(2)
        mc.play()
        print("=> Playing {0}" .format(cast.media_controller.status))
    elif payload["action"] == "volume":
        print("=> Change volume to "+ str(payload["desc"]))
        cast.set_volume(payload["desc"])
    elif payload["action"] == "pause":
        print("=> Sending pause command")
        mc.pause()
    elif payload["action"] == "stop":
        print("=> Sending stop command")
        mc.stop()
    # elif payload["action"] == "quit":
    #     print("=> Sending quit_app command")
    #     cast.quit_app()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("radio_action")

def on_message(client, userdata, msg):
    if str(msg.topic) == 'radio_action':
        payload = json.loads(msg.payload)
        cc_action(payload)

def on_subscribe(client, userdata, mid, granted_qos):
 print("Subscribed to Topic: " + 
 "radio_action" + " with QoS: " + str(granted_qos))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

client.connect("mqtt", 1883, 60)
client.loop_forever()