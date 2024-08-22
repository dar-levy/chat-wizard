from db import db
from models import DialogModel, UserModel
from sqlalchemy.exc import SQLAlchemyError
from flask_smorest import abort
from passlib.hash import pbkdf2_sha256


def save_dialog(question, answer):
    dialog = DialogModel(question=question, answer=answer)
    try_save_to_db(dialog)


def save_user(username, password):
    user = UserModel(
        username=username,
        password=pbkdf2_sha256.hash(password),
    )

    try_save_to_db(user)


def try_save_to_db(model):
    try:
        db.session.add(model)
        db.session.commit()

        return model
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, message="An error occurred while inserting the dialog. Please try again.")
