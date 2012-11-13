from flask import Flask, request, redirect, session, url_for, render_template
import json
import graph

app = Flask(__name__)
app.secret_key = 'asdasdjklasdjkl32'

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/path/<query>")
def path(query):
  return graph.lookup(query)

if __name__ == "__main__":
    app.run(debug=True)
