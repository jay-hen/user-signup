from flask import Flask

app = Flask(__name__)
app.config['debug'] = True

form = """

"""

@app.route("/")
def index():
    return form

app.run