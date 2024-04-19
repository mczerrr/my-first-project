from flask import Flask #update pertama

app = Flask(__name__) #update kedua

@app.route("/")
def helloWorld():
    return "Hello, World!" #update terakhir
