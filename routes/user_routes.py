from flask import Blueprint

from controllers import user_controllers

user = Blueprint("user", __name__)


@user.route("/user", methods = ["POST"])
def user_add():
    return user_controllers.user_add()


@user.route("/user", methods = ["GET"])
def user_get_all():
    return user_controllers.users_get_all()


@user.route("/user/<user_id>", methods = ["GET"])
def user_get_by_id(user_id):
    return user_controllers.user_get_by_id(user_id)


@user.route("/user/<user_id>", methods = ["PATCH"])
def user_activity(user_id):
    return user_controllers.user_activity(user_id)


@user.route("/user/<user_id>", methods = ["DELETE"])
def user_delete_by_id(user_id):
    return user_controllers.user_delete_by_id(user_id)


@user.route("/user/<user_id>", methods = ["PUT"])
def user_update_by_id(user_id):
    return user_controllers.user_update_by_id(user_id)


