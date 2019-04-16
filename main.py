from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['debug'] = True

@app.route("/")
def index():
    return render_template('form.html')

if __name__ == '__main__':
    app.run