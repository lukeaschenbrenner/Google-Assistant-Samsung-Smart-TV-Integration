#!/usr/bin/env python

import paho.mqtt.client as mqtt
import configparser, json, os, sys, logging
import samsung_smart_tv_remote as remote

log = logging.getLogger('artik_cloud.py')
log.basicConfig(stream=sys.stdout, level=logging.DEBUG)

config = configparser.ConfigParser()
config.read(os.path.join('config', 'artik_cloud.ini'))

def on_connect(client, userdata, flags, rc):
	log.debug("Connected with result code " + str(rc))
	client.subscribe("/v1.1/actions/" + config['ArtikCloud']['device_id'])

def on_message(client, userdata, msg):
	print msg.topic, str(msg.payload)
	message = json.loads(msg.payload)
	actions = message['actions']
	for action in actions:
		if action['name'] == "changeChannel":
			remote.change_channel(action['parameters']['channel'])
		elif action['name'] == "tvOff":
			remote.turn_off_tv()
		else:
			print "There is no custom command implemented for", action['name']

client = mqtt.Client()
client.username_pw_set(config['ArtikCloud']['device_id'], config['ArtikCloud']['device_token'])
client.tls_set()
client.on_connect = on_connect
client.on_message = on_message

client.connect("api.artik.cloud", 8883, 60)

client.loop_forever()