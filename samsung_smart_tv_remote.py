#!/usr/bin/env python

import configparser, time, samsungctl, os

config = configparser.ConfigParser()
config.read(os.path.join('config', 'samsung_smart_tv_remote.ini'))

config_remote = {
    "name": config['SamsungSmartTV']['name'],
    "description": config['SamsungSmartTV']['description'],
    "id": "",
    "host": config['SamsungSmartTV']['host'],
    "port": int(config['SamsungSmartTV']['port']),
    "method": config['SamsungSmartTV']['method'],
    "timeout": 60
}

def change_channel(channel):
	with samsungctl.Remote(config_remote) as remote:
		for digit in channel:
			remote.control("KEY_" + digit)
			time.sleep(0.5)
		remote.control("KEY_ENTER")
		print "The channel was changed to", channel

def turn_off_tv():
	with samsungctl.Remote(config_remote) as remote:
		print "The TV is shutting down"
		remote.control("KEY_POWER")