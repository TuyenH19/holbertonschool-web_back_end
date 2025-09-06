#!/usr/bin/env python3
"""
Basic Flask app with Babel to force locale with URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_TRANSLATION_DIRECTORIES = "translations"


app = Flask(__name__)
app.config.from_object(Config)

# Module-level Babel object
babel = Babel(app)


def get_locale():
    """
    Get matching locale from URL parameter or request headers
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Initialize Babel with custom selector
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render the index page"""
    return render_template("4-index.html")
