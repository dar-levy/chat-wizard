from marshmallow import Schema, fields, validate


class AskSchema(Schema):
    id = fields.Int(dump_only=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)


class QuestionSchema(Schema):
    question = fields.Str(required=True, validate=validate.Length(max=100))
