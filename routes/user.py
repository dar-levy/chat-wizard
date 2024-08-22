from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from schemas.user import UserSchema
from models import UserModel
from services.db_service import save_user, delete_user

blp = Blueprint('Users', 'users', __name__, description="Operations on users")


@blp.route('/register')
class User(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data['username']).first():
            abort(409, 'User already exists')

        return save_user(user_data['username'], user_data['password'])

@blp.route('/user/<int:user_id>')
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        delete_user(user)

        return {"message": "User deleted"}, 200
