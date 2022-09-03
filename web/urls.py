from flask import Blueprint
from .controller import *

router = Blueprint("web", __name__)

router.add_url_rule(rule='/', endpoint="web-index", view_func=web_index, methods=['GET'])
