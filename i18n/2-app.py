#!/usr/bin/env python3
"""
A basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for Flash app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel()


def get_locale():
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Initialize Babel with our custom locale selector
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Render the 2-index.html template
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port=5000, host="localhost")
