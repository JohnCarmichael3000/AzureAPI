from flask import Flask, jsonify
from flask import render_template
from AzureCLI import *

#initialize application itself
azureAPI = Flask(__name__)

#two routess

@azureAPI.route('/')
def home():
    try:
        return render_template("home.html")

    except SyntaxError:
        return 'A syntax error has occurred. Please run the code through a build process and try again...'

    except Exception as e:
        return e

#second route - list VM's
@azureAPI.route('/listvms', methods=['GET'])
def listvms():
    return jsonify(AzureCLI.listVMs())
#listVMs returns a list in JSON

# if you want to run the API locally:
#azureAPI.run(host='127.0.0.1', port=5000)

#0.0.0.0 is for Azure Cloud, Azure will map ip address
azureAPI.run(host='0.0.0.0', port=80)
