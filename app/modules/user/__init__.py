
from flask import Blueprint

from app.modules.user.views import register, login

module = Blueprint('modules_user', __name__)

module.add_url_rule('/register', view_func=register, methods=['post','get'] )
module.add_url_rule('/login', view_func=login, methods=['post'] )



