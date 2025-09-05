#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    # Point Babel to the translations directory
    BABEL_TRANSLATION_DIRECTORIES = "translations"


app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel()


def get_locale():
    """Pick best match from Accept-Language header."""
    lang = request.args.get("lang")
    if lang in app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# Initialize Babel with custom locale selector
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port=5000, host="localhost")
