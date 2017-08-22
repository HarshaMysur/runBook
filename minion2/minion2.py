#!flask/bin/python
from flask import Flask, request
from shutil import copyfile
import os

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
	parent = os.pardir+"/code/common_folder"
	if ((os.path.exists(parent+"/"+request.get_json()['sourcefile']))):
		copyfile(parent+"/"+request.get_json()['sourcefile'], parent+"/"+request.get_json()['destinationfile'])
	else:
		return "File do not exists"
	return "Copied Successfully!!!"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)