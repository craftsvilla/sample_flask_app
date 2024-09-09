from flask import Blueprint
from app.v1.users import views as sample_subapp_views
from app.v1.books import views as book_views


v1 = Blueprint('v1', __name__)


# subapp1 urls
sample_subapp_prefix = '/users'



v1.add_url_rule(sample_subapp_prefix + '/getUserName', view_func=sample_subapp_views.GetUserName.as_view('endpoint_1'))



v1.add_url_rule(
    sample_subapp_prefix + '/getUser',
    view_func=sample_subapp_views.GetUserDetails.as_view('endpoint_2')
)

book_prefix = '/books'

v1.add_url_rule(
    book_prefix,
    view_func=book_views.GetBookDetails.as_view('get_books'),
    methods=['GET']
)

v1.add_url_rule(
    book_prefix + '/create',
    view_func=book_views.GetBookDetails.as_view('create_book'),
    methods=['POST']
)

v1.add_url_rule(
    book_prefix + '/update',
    view_func=book_views.GetBookDetails.as_view('update_book'),
    methods=['PUT']
)

v1.add_url_rule(
    book_prefix + '/delete',
    view_func=book_views.GetBookDetails.as_view('delete_book'),
    methods=['DELETE']
)

v1.add_url_rule(
    book_prefix + '/<int:id>',
    view_func=book_views.GetBookDetails.as_view('get_book_by_id'),
    methods=['GET']
)