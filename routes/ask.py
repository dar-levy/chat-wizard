from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint('ask', __name__, description="Ask a question & pass to OpenAI")

class Ask(MethodView):
    def post(self):
        pass