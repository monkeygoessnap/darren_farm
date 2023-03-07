from flask import Flask, redirect, render_template, request
import json

app = Flask(__name__)

status = {
    'farm1': None,
    'farm2': None,
    'farm3': None
}

@app.route("/")
def index():
    """HOME PAGE"""
    return render_template("index.html")

@app.rute("/data", methods=['GET', 'POST'])
def data():
    """DATA"""

    if request.method == 'POST':
        data = request.json
        if 'farm1' in data:
            status['farm1'] = data['farm1']
        elif 'farm2' in data:
            status['farm2'] = data['farm2']
        elif 'farm3' in data:
            status['farm3'] = data['farm3']

    return json.dumps(status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)