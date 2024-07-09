from db import db
from models import DialogModel
from sqlalchemy.exc import SQLAlchemyError
from flask_smorest import abort


def save_dialog(question, answer):
    dialog = DialogModel(question=question, answer=answer)

    try:
        db.session.add(dialog)
        db.session.commit()
        return dialog
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, message="An error occurred while inserting the dialog. Please try again.")
