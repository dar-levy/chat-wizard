from sqlalchemy import Column, Integer, String, Text
from db import db


class DialogModel(db.Model):
    __tablename__ = "dialogs"

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    question = db.Column(Text, nullable=False)
    answer = db.Column(Text, nullable=False)
