from flask import Flask

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "ChatWizard REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
api = Api(app)
api.register_blueprint(ask_blueprint)


if __name__ == '__main__':
    app.run()
