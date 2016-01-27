
data = [ 
    {"sensor_id":"1","type":"charge","value":"4.025","date":"2016-01-27 11:34:17"},{"sensor_id":"1","type":"ground_humidity_10","value":"1.98","date":"2016-01-27 11:34:17"},{"sensor_id":"1","type":"ground_humidity_20","value":"0.99","date":"2016-01-27 11:34:17"},{"sensor_id":"1","type":"ground_humidity_30","value":"1.98","date":"2016-01-27 11:34:17"},{"sensor_id":"1","type":"ec","value":"0","date":"2016-01-27 11:34:17"},
    {"sensor_id":"1","type":"ph","value":"3.16002","date":"2016-01-27 11:34:17"},{"sensor_id":"1","type":"temperature","value":"18.9","date":"2016-01-27 11:34:17"},{"sensor_id":"1","type":"humidity","value":"72.4","date":"2016-01-27 11:34:17"},{"sensor_id":"1","type":"water_lost","value":"11","date":"2016-01-27 11:34:17"},{"sensor_id":"1","type":"charge","value":"4.091","date":"2016-01-26 21:27:23"},{"sensor_id":"1","type":"ground_humidity_10","value":"100","date":"2016-01-26 21:27:23"},{"sensor_id":"1","type":"ground_humidity_20","value":"100","date":"2016-01-26 21:27:23"},{"sensor_id":"1","type":"ground_humidity_30","value":"100","date":"2016-01-26 21:27:23"},{"sensor_id":"1","type":"ec","value":"0","date":"2016-01-26 21:27:23"},{"sensor_id":"1","type":"temperature","value":"22.7","date":"2016-01-26 21:27:23"},{"sensor_id":"1","type":"humidity","value":"76.8","date":"2016-01-26 21:27:23"},{"sensor_id":"1","type":"water_lost","value":"11","date":"2016-01-26 21:27:23"},{"sensor_id":"1","type":"charge","value":"4.093","date":"2016-01-26 21:12:21"},{"sensor_id":"1","type":"ground_humidity_10","value":"100","date":"2016-01-26 21:12:21"},{"sensor_id":"1","type":"ground_humidity_20","value":"100","date":"2016-01-26 21:12:21"},{"sensor_id":"1","type":"ground_humidity_30","value":"100","date":"2016-01-26 21:12:21"},{"sensor_id":"1","type":"ec","value":"0","date":"2016-01-26 21:12:21"},
    {"sensor_id":"1","type":"ph","value":"11.33583","date":"2016-01-26 21:12:21"},{"sensor_id":"1","type":"temperature","value":"23.3","date":"2016-01-26 21:12:21"},{"sensor_id":"1","type":"humidity","value":"72.9","date":"2016-01-26 21:12:21"},{"sensor_id":"1","type":"water_lost","value":"11","date":"2016-01-26 21:12:21"},{"sensor_id":"1","type":"charge","value":"4.09","date":"2016-01-26 19:42:23"},{"sensor_id":"1","type":"ground_humidity_10","value":"100","date":"2016-01-26 19:42:23"},{"sensor_id":"1","type":"ground_humidity_20","value":"100","date":"2016-01-26 19:42:23"},{"sensor_id":"1","type":"ground_humidity_30","value":"100","date":"2016-01-26 19:42:23"},{"sensor_id":"1","type":"ec","value":"0","date":"2016-01-26 19:42:23"},
    {"sensor_id":"1","type":"ph","value":"14","date":"2016-01-26 19:42:23"},
    {"sensor_id":"1","type":"temperature","value":"28","date":"2016-01-26 19:42:23"},{"sensor_id":"1","type":"humidity","value":"64","date":"2016-01-26 19:42:23"},{"sensor_id":"1","type":"water_lost","value":"22","date":"2016-01-26 19:42:23"},{"sensor_id":"1","type":"charge","value":"4.074","date":"2016-01-26 19:27:24"},{"sensor_id":"1","type":"ground_humidity_10","value":"100","date":"2016-01-26 19:27:24"},{"sensor_id":"1","type":"ground_humidity_20","value":"100","date":"2016-01-26 19:27:24"},{"sensor_id":"1","type":"ground_humidity_30","value":"100","date":"2016-01-26 19:27:24"},{"sensor_id":"1","type":"temperature","value":"29.1","date":"2016-01-26 19:27:24"},{"sensor_id":"1","type":"humidity","value":"70.5","date":"2016-01-26 19:27:24"},{"sensor_id":"1","type":"water_lost","value":"0","date":"2016-01-26 19:27:24"},{"sensor_id":"1","type":"charge","value":"4.079","date":"2016-01-26 19:12:20"}
]

# FLASK BLUEMIX

import os
from flask import Flask, jsonify

app = Flask(__name__)
# Change current directory to avoid exposure of control files
os.chdir('static')

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/sensors', methods=['GET'])
def get_tasks():
    return jsonify({'data': data})

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))

#FIN FLASK BLUEMIX