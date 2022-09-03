from flask import Blueprint
from .controller import *

router = Blueprint("api", __name__)

router.add_url_rule(rule='/', endpoint="api-index", view_func=api_index, methods=['GET'])
