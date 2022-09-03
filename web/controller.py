from flask import jsonify

def web_index():
    return jsonify({"status":200, "msg":"web_index"})