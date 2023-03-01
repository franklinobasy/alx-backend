#!/usr/bin/env python3
"""Basic Babel Setup"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class for flask app
    """
    DEBUG = True
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """view function for root route

    Returns:
        html: homepage
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """get best language match

    Returns:
        str: best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# uncomment this line and comment the @babel.localeselector
# you get this error:
# AttributeError: 'Babel' object has no attribute 'localeselector'
# babel.init_app(app, locale_selector=get_locale)

if __name__ == '__main__':
    app.run()
