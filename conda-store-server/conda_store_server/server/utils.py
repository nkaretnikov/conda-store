from flask import current_app


def get_conda_store():
    return current_app.conda_store


def get_auth():
    return current_app.authentication
