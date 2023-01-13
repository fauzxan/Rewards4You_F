""" This Module is responsible for handling User Registration"""
from flask import Blueprint

module = Blueprint('register', __name__)

module.add_url_rule('/register', view_func= """#TODO""", methods=["POST", "GET"])
