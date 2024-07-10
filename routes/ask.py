from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.dialog import DialogSchema, QuestionSchema
from services.db_service import save_dialog
from services.openai_service import ask_openai

blp = Blueprint('ask', __name__, description="Ask a question & pass to OpenAI")


@blp.route('/ask')
class Ask(MethodView):
    @blp.arguments(QuestionSchema)
    @blp.response(200, DialogSchema)
    def post(self, ask_data):
        question = ask_data['question']
        answer = ask_openai(question)
        dialog = save_dialog(question, answer)

        return dialog
