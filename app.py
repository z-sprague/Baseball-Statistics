from flask import Flask, render_template, jsonify, request
from random import sample
from functions import get_data

app = Flask(__name__)


@app.route('/', methods=['GET'])
def chart():
    alct_data = None
    nlct_data = None
    years = []
    for i in range(2019, 1968, -1):
        years.append(i)
    if request.args.get('years') is None:
        year = 2019
    else:
        year = int(request.args.get('years'))

    alea_data = get_data(year, 0)

    if year > 1993:
        alct_data = get_data(year, 1)
        alwt_data = get_data(year, 2)
        nlea_data = get_data(year, 3)
        nlct_data = get_data(year, 4)
        nlwt_data = get_data(year, 5)
    else:
        alwt_data = get_data(year, 1)
        nlea_data = get_data(year, 2)
        nlwt_data = get_data(year, 3)

    # alea_data = alea_stats(year)
    # alwt_data = alwt_stats(year)
    # nlea_data = nlea_stats(year)
    # nlwt_data = nlwt_stats(year)

    return render_template('index.html', years=years, year=year,
                           alea_data=alea_data, nlea_data=nlea_data,
                           alwt_data=alwt_data, nlwt_data=nlwt_data,
                           alct_data=alct_data, nlct_data=nlct_data)


@app.route('/data')
def league_data():
    return jsonify({'results': sample(range(1, 10), 5)})


if __name__ == '__main__':
    app.run(debug=True)
