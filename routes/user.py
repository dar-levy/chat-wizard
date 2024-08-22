from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.user import UserSchema
from models import UserModel
from services.db_service import save_user

blp = Blueprint('Users', 'users', __name__, description="Operations on users")


@blp.route('/register')
class User(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data['username']).first():
            abort(409, 'User already exists')

        user = save_user(user_data['username'], user_data['password'])

        return user
