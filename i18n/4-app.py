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
babel = Babel()


def get_locale():
    """
    Priority:
    1) URL query param ?locale=xx (if supported)
    2) Best match from Accept-Language header
    3) Default locale ('en')
    """
    forced = request.args.get("locale")
    if forced in app.config["LANGUAGES"]:
        return forced
    match = request.accept_languages.best_match(app.config["LANGUAGES"])
    return match or app.config["BABEL_DEFAULT_LOCALE"]


# Initialize Babel with custom selector
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render the index page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
