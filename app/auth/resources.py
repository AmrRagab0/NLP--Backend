from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
from uuid import uuid4
from app.auth.models import UserModel
from app.auth.services import UserServices

_auth_parser = reqparse.RequestParser()

_auth_parser.add_argument("username", type=str, help="User username.")

_auth_parser.add_argument("user_type", type=str, help="User type.")

_auth_parser.add_argument("password", type=str, help="User password.")

_auth_parser.add_argument("user_id", type=str, help="User id.")


class LoginResource(Resource):

    def post(self):
        data = _auth_parser.parse_args()

        try:

            if not data.get("username"):
                return {
                    "description": "username is required",
                    "error ": "not_found",
                }, 404

            if not data.get("password"):
                return {
                    "description": "password is required",
                    "error ": "not_found",
                }, 404
            user: UserModel = UserServices.get_user_by_username(
                data.get("username"))

            if not user:
                return {
                    "description": "The username is incorrect or the user doesn't exist",
                    "error": "invalid_username",
                }, 404
            if user.password == data.get("password"):
                access_token = create_access_token(
                    identity=user.user_id, fresh=True)
                refresh_token = create_refresh_token(identity=user.user_id)

                return {"accessToken": access_token, "refreshToken": refresh_token}, 200
            return {
                "description": "The password provided didn't match the user password.",
                "error": "invalid_password",
            }, 401
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500


# class RegisterResource(Resource):
#     @jwt_required()
#     def post(self):
#         #TOOD: check if the type of the user
#         data = _auth_parser.parse_args()
#         try:
#             if not data.get("username"):
#                 return {
#                     "description": "username is required",
#                     "error ": "not_found",
#                 }, 404
#             if not data.get("password"):
#                 return {"description": "email is required", "error ": "not_found"}, 404

#             if not data.get("user_type"):
#                 return {
#                     "description": "user type is required",
#                     "error ": "not_found",
#                 }, 404
#             if UserServices.get_user_by_username(data.get("username")):
#                 return {
#                     "description": "A user with this username already exists.",
#                     "error": "username_exists",
#                 }, 400
#             data["user_id"] = str(uuid4())

#             user = UserModel.from_json(data)
#             is_created = UserServices.add_user_to_db(user)

#             if not is_created:
#                 return {
#                     "description": "username already exists",
#                     "error": "username_exists",
#                 }, 400
#             access_token = create_access_token(user.user_id, fresh=True)
#             refresh_token = create_refresh_token(user.user_id)
#             return {
#                 "message": "User created successfully.",
#                 "user": UserModel.to_json(user),
#                 "accessToken": access_token,
#                 "refreshToken": refresh_token,
#             }, 201
#         except:
#             return {
#                 "description": "Internal server error",
#                 "error": "internal_server_error",
#             }, 500
