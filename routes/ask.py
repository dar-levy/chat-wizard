from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import DialogModel
from schemas.dialog import DialogSchema, QuestionSchema

blp = Blueprint('ask', __name__, description="Ask a question & pass to OpenAI")


@blp.route('/ask')
class Ask(MethodView):
    @blp.arguments(QuestionSchema)
    @blp.response(200, DialogSchema)
    def post(self, ask_data):
        ask_data['answer'] = "Some answer until openAI feature"
        dialog = DialogModel(**ask_data)

        try:
            db.session.add(dialog)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the dialog. Please try again.")

        return dialog