#!/usr/bin/env python3
"""
A basic flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration for Babel setup"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)


@app.route('/')
def index():
    """
    Render the 1-index.html template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port=5000, host="localhost")
