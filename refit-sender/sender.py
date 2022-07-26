from flask import Flask, jsonify
from jproperties import Properties
import time
import requests
import json

app = Flask(__name__)
propPath = "/refit/config/refit.properties"
url = "refit-receiver-svc.default.svc.cluster.local:8080/receiver"
payload = {'message': 'Hello World!!'}

def sender(config):
	while True:
		response = requests.post(api_url, payload)
		print(response.json())
		time.sleep(config)

def loadProperties():
	configProp = Properties()
	with open(propPath, 'rb') as config_file:
		configProp.load(config_file)
	return configProp

if __name__ == '__main__':
	config = loadProperties()
	app.run(host='0.0.0.0', port=8080, debug=True)
	#config = loadProperties()
	#print(config.get("Average").data)
