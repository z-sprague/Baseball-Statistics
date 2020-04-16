from flask import Flask, render_template, jsonify, request
from random import sample
from functions import get_data, get_size, bar_colors, bar_outline_colors

app = Flask(__name__)


@app.route('/', methods=['GET'])
def chart():
    alea_data, nlea_data, alct_data, nlct_data, alwt_data, nlwt_data, older_data, \
        = None, None, None, None, None, None, None,

    bc = bar_colors
    boc = bar_outline_colors
    size = 0

    years = []
    for i in range(2019, 1870, -1):
        years.append(i)
    if request.args.get('years') is None:
        year = 2019
    else:
        year = int(request.args.get('years'))

    if year > 1968:
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
    else:
        older_data = get_data(year)
        size = int(get_size(year))

    return render_template('index.html', years=years, year=year,
                           alea_data=alea_data, nlea_data=nlea_data,
                           alwt_data=alwt_data, nlwt_data=nlwt_data,
                           alct_data=alct_data, nlct_data=nlct_data,
                           older_data=older_data, bc=bc,
                           boc=boc, size=size)


@app.route('/', methods=['GET'])
def league_data():
    return None


if __name__ == '__main__':
    app.run(debug=True)
