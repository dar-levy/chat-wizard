from marshmallow import Schema, fields, validate


class DialogSchema(Schema):
    id = fields.Int(dump_only=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)


class QuestionSchema(Schema):
    question = fields.Str(required=True, validate=validate.Length(min=5, max=200))
