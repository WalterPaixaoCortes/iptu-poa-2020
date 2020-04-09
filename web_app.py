import os
import traceback
import datetime

from flask import Flask, render_template, request, redirect, url_for, flash, g, session, send_from_directory, jsonify

app = Flask(__name__)


# ---------------------------------------------------------------------------------------------
# Main Route - Home
# ---------------------------------------------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calc')
def calculation():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=8080)