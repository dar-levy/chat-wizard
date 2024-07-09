from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.ask_schema import AskSchema, QuestionSchema

blp = Blueprint('ask', __name__, description="Ask a question & pass to OpenAI")


@blp.route('/ask')
class Ask(MethodView):
    @blp.arguments(QuestionSchema)
    @blp.response(200, AskSchema)
    def post(self, ask_data):
        print(ask_data)
        return {
            "id": 1,
            "question": "Some question",
            "answer": "Some answer"
        }