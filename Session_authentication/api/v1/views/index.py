#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized/', methods=['GET'], strict_slashes=False)
def unauthorizedView() -> str:
    """unauthorized View endpoint

    Returns:
        str: abort 401 status
    """
    return abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def test_forbidden() -> str:
    """ GET /api/v1/forbidden
    Return:
      - Raise error
    """
    return abort(403)
