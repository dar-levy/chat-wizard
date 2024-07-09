from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.dialog import DialogSchema, QuestionSchema

blp = Blueprint('ask', __name__, description="Ask a question & pass to OpenAI")


@blp.route('/ask')
class Ask(MethodView):
    @blp.arguments(QuestionSchema)
    @blp.response(200, DialogSchema)
    def post(self, ask_data):
        return {
            "id": 1,
            "question": ask_data['question'],
            "answer": "Some answer"
        }