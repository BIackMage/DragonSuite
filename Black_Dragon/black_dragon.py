from flask import Flask, render_template, send_from_directory
from flask import request
import os

## this is an example Flask app. It will serve the html file found @ /templates/index.html (a nifty TOR Primer)
## it will also allow for communications across TOR
## data is sent to the Flask app via either POST or GET requests
## echos the data back via the index.html's footer variable {{ message }} 

# Flask constructor takes the name of  current module (__name__) as argument.
# TODO update the static_folder to where you're serving from
app = Flask(__name__,
            static_url_path='', 
            static_folder='/home/kali/Desktop/Dragon_Suite/Black_Dragon/static')
           
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

@app.route('/', methods=['POST', 'GET'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    # handle GET requests
    if request.method == 'GET':
        # get the secret data
        secret = request.args.get('secret', default="NoSecret!")
        # print to the server's terminal
        print("***** Received secret communication over TOR via GET. *****\n{}".format(secret))
        # send the web page back to the client or browser (message embedded)
        message = "Hello from our super secret listening post!!"
        if secret == "NoSecret!":
            message += " You didn't send me anything. Sad."
        else:
            message += " You sent me this: {}".format(secret)
        return render_template('index.html', message=message)
    #handle POST requests
    if request.method == 'POST':
        # get the secret data
        secret = request.form['secret']
        # print to the server's terminal
        print("***** Received secret communication over TOR via POST. *****\n{}".format(secret))
        # send the web page back to the client or browser (message embedded)
        message = "Hello from our super secret listening post!!"
        message += " You sent me this: {}".format(secret)
        return render_template('index.html', message=message)

# serve the favicon so we don't see annoying errors that it doesn't exist
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon') 


# how I'm serving the embedded images for the index.html page
@app.route('/static/<file>', methods=['GET'])
def render_static(file):
    secret = request.args.get('secret', default = '*', type = str)
    print("Exfil'ed data: {}".format(secret))
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               file) 

    
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='127.0.0.1', port=8080)  