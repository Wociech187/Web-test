from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello world</h1>"

app.run(host='192.200.100.32',port=7562,debug=True)
