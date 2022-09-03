from flask import jsonify

def api_index():
    return jsonify({"status":200, "msg":"api_index"})