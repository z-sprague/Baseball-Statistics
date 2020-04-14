from flask import Flask, render_template, jsonify, request
from random import sample
from functions import alea_data, alct_data, alwt_data, nlea_data, nlct_data, nlwt_data

app = Flask(__name__)


@app.route('/')
def chart():
    return render_template('index.html',
                           alea_data=alea_data, alct_data=alct_data,
                           nlea_data=nlea_data, nlct_data=nlct_data,
                           alwt_data=alwt_data, nlwt_data=nlwt_data)


@app.route('/data')
def league_data():
    return jsonify({'results': sample(range(1, 10), 5)})


if __name__ == '__main__':
    app.run(debug=True)
