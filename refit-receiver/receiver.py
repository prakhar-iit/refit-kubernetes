from flask import Flask, request, jsonify
from jproperties import Properties

import json
app = Flask(__name__)

propPath = '/refit/config/refit.properties'

@app.route('/receiver', methods=['POST'])
def receiver():
	requestPayload = json.loads(request.data)
	print(requestPayload.get("message"))
	return 'I got it, roger'

def loadProperties():
	configProp = Properties()
	with open(propPath, 'rb') as config_file:
		configProp.load(config_file)
	return configProp

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)