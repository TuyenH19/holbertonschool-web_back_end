#!/usr/bin/env python3
"""
Basic Flask + Flask-Babel app demonstrating mock login and locale selection.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)

# --- Mocked users table (acts like a DB) ---
users = {
  1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
  2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
  3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
  4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# --- Helper: get current user from ?login_as=<id> ---
def get_user():
    """Return a user dict or None if not found / not provided."""
    login_as = request.args.get("login_as")
    if not login_as:
        return None
    try:
        user_id = int(login_as)
    except (TypeError, ValueError):
        return None
    return users.get(user_id)


# --- Run before every request: attach user to flask.g ---
@app.before_request
def before_request() -> None:
    """Set g.user to the current user, if any."""
    g.user = get_user()


# --- Locale selection: prefer user's locale if valid, else best match ---
def get_locale() -> str:
    """Determine the best match with our supported languages."""
    user = getattr(g, "user", None)
    if user and user.get("locale") in app.config["LANGUAGES"]:
        return user["locale"]

    req_locale = request.args.get("locale")
    if req_locale in app.config["LANGUAGES"]:
        return req_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"]) or "en"


# NEW: pass selector into Babel()
babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render the index page."""
    return render_template("5-index.html")
