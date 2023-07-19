from flask import Blueprint, request
from controllers import avatarController

bp = Blueprint('avatar', __name__)

@bp.route('/create', methods=['POST'])
def create_avatar():
    return avatarController.create_avatar(request)

@bp.route('/retrieve', methods=['GET'])
def retrieve_avatar():
    return avatarController.retrieve_avatar(request)

@bp.route('/delete', methods=['DELETE'])
def delete_avatar():
    return avatarController.delete_avatar(request)

@bp.route('/update', methods=['PATCH'])
def update_avatar():
    return avatarController.update_avatar(request)