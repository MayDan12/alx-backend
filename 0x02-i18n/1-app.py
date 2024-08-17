#!/usr/bin/env python3
"""
This is the module sets up a basic Flask
application with Babel for i18n support.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    The configuration class for Flask application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    the Route for the home page.

    Returns:
        str: This is the rendered template for the home page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)