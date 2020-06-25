"""Display a stock ticker visualization based on user input."""
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    """Render the app's main page."""
<<<<<<< HEAD
    if request.method == 'GET':
=======
    if request.methods == 'GET':
>>>>>>> ff0444aa864f91688c632ff0f143c4d5ae6e6317
        # Default gives IBM's ticker when first loaded.
        symbol = 'IBM'
        return render_template('index.html', symbol=symbol)

    else:
        # User submitted a ticker symbol aka method = 'POST'
        symbol = request.form['symbol']
        return render_template('index.html', symbol=symbol)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=33507)
