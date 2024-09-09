from flask import Blueprint
from app.v1.users import views as sample_subapp_views
from app.v1.users.views1 import User_Book_API


v1 = Blueprint('v1', __name__)


# subapp1 urls
sample_subapp_prefix = '/users'

v1.add_url_rule(sample_subapp_prefix + '/getUserName', view_func=sample_subapp_views.GetUserName.as_view('endpoint_1'))


v1.add_url_rule(
    sample_subapp_prefix + '/getUserDetails',
    view_func=sample_subapp_views.GetUserDetails.as_view('endpoint_2')
)

user_view = User_Book_API.as_view('user_book_api')

v1.add_url_rule(sample_subapp_prefix + '/books', view_func=user_view, methods=['GET', "POST"])

v1.add_url_rule(sample_subapp_prefix + '/books', view_func=user_view, methods=['PUT','DELETE'])

v1.add_url_rule(
    sample_subapp_prefix + '/books/<int:id>', 
    view_func=user_view,
    methods=['GET']
)


