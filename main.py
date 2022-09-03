import os
from flask import Flask
from flask_cors import CORS
from cli_commands import cli_commands
from web.urls import router as web_router
from api.urls import router as api_router



app = Flask(__name__, template_folder="templates", static_folder="static")

CORS(app)

app.register_blueprint(web_router, url_prefix="/")
app.register_blueprint(api_router, url_prefix="/api")

app = cli_commands(app)


if __name__ == "__main__":    
    app.run(port=8080)
