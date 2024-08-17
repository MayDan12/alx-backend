#!/usr/bin/env python3
"""
This is the module sets up a basic Flask
application with Babel for i18n support.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    This is the configuration class for Flask application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    This determine the best match for supported languages.

    Returns:
        str: This is the best match language.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    The route for the home page.

    Returns:
        str: This is the rendered template for the home page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)