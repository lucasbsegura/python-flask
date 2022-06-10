from flask import Flask, jsonify, make_response, render_template, request

app1 = Flask(__name__)

@app1.route('/')
def hello_world():
    return "Hello World!"

@app1.route('/pranjal')
def hello_pranjal():
    return "Hello Pranjal!"

@app1.route('/html')
def get_html():
    return render_template("index.html")

@app1.route('/qs')
def get_qs():
    if request.args:
        req=request.args
        return " ".join(f"{k}:{v}" for k, v in req.items())
    return "No query string"

if __name__ == '__main__':
    app1.run(debug=True)