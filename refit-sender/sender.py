from flask import Flask, jsonify
from jproperties import Properties
import time
import requests
import json
import threading

app = Flask(__name__)

propPath = "/refit/config/refit.properties"
#propPath = "/Users/prakharrastogi/Desktop/project/refit.properties" #Need to change
url = "http://refit-receiver-svc.default.svc.cluster.local:8080/receiver"
#url = "http://localhost:8081/receiver" 
payload = {'message': 'Hello World!!'}
send = False
config = ''

@app.route('/sender')
def sender():
	#Create a thread and keep hitting request to receiver
	avg_time = int(config.get("sender_avg_time").data)
	global send
	if(send):
		send = False
		print("Stop Pinging....")
	else:
		send = True
		print("Start Pinging....")

	if(send):
		t1 = threading.Thread(target = ping, args = (avg_time,))
		t1.start()
	return "Request Accepted on Sender"

def ping(avg_time):
	while (send):
		print("ping " + url + " with payload: " , payload)
		headers =  {"Content-Type": "application/json"}
		response = requests.post(url, json = payload, headers=headers)
		print(response.text)
		time.sleep(avg_time)

def loadProperties():
	configProp = Properties()
	with open(propPath, 'rb') as config_file:
		configProp.load(config_file)
	return configProp

if __name__ == '__main__':
	config = loadProperties()
	app.run(host='0.0.0.0', port=8080, debug=True)