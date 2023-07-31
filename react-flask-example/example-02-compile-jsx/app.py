# https://stackoverflow.com/questions/59355194/python-flask-error-failed-to-load-module-script-strict-mime-type-checking-i

# fix windows registry stuff
import mimetypes
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
