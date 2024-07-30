#!/usr/bin/python3
"""Script starts a Flask web application"""


from flask import Flask
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
def display_text(text):
    """displays C followed by the value of text"""
    
    return f"C, {escape(text)}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
