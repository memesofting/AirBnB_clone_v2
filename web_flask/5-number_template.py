#!/usr/bin/python3
"""Script starts a Flask web application"""


from flask import Flask, abort, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """returns Hello HBNB"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """displays HBNB"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """displays C followed by the value of text"""

    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text="is cool"):
    """displays C followed by the value of text"""

    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<n>', strict_slashes=False)
def display_number(n):
    """displays value of 'n' if n is a number"""

    try:
        n = int(n)
        return f"{escape(n)} is a number"
    except ValueError:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def display_html(n):
    """displays a HTML page only if n is an integer"""

    try:
        n = int(n)
        return render_template('5-number.html', number=escape(n))
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
