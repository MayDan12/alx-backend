#!/usr/bin/env python3
"""
This is the module sets up a basic Flask
application with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    The Route for the home page.

    Returns:
        str: This is the rendered template for the home page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)