from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.ask_schema import AskSchema

blp = Blueprint('ask', __name__, description="Ask a question & pass to OpenAI")


@blp.route('/ask')
class Ask(MethodView):
    @blp.response(200, AskSchema)
    def post(self):
        return {"question": "Some question", "answer": "Some answer"}