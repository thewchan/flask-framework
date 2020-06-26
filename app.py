"""Display a stock ticker visualization based on user input."""
import json
from flask import Flask, render_template, request, redirect
from bokeh.embed import json_item
from bokeh.resources import CDN
from ticker import ticker


app = Flask(__name__)
app.vars = {}


def create_ticker(symbol):
    """Render ticker json object from stock symbol."""
    p = ticker(symbol)

    return p


@app.route('/', methods=('GET', 'POST'))
def index():
    """Render the app's main page."""
    if request.method == 'GET':
        # Default gives IBM's ticker when first loaded.
        app.vars['symbol'] = 'IBM'
        return render_template('index.html',
                               symbol=app.vars['symbol'],
                               )

    else:
        # User submitted a ticker symbol aka method = 'POST'
        app.vars['symbol'] = request.form['symbol']
        return render_template('index.html',
                               symbol=app.vars['symbol'],
                               )


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/plot')
def plot():
    """Render json item from bokeh plot."""
    p = create_ticker(app.vars['symbol'])
    return json.dumps(json_item(p, 'myplot'))


if __name__ == '__main__':
    app.run(port=33507)
