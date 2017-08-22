#!flask/bin/python
from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    #print("ey")
    parent = os.pardir+"/code/common_folder"
    path = parent + "/" + request.get_json()['directoryname']
    if not os.path.exists(path):
        os.mkdir(path)
    else:
	    return "Directory already exists"
    #os.mkdir(path);
    return "Successfully Creted"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)