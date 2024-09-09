import pymysql
from flask import jsonify, request
from flask.views import MethodView
from app.decorators import validate_request
from app.common_utils import render_success_response
from app.v1.users.service import SubApp1Service
from app.connections import SqlConnection

# db_config = {
#         'host': 'localhost',
#         'user': 'root',
#         'password': 'root',
#         'database': 'demo'
#     }
#
# db_connection = SqlConnection(db_config)



class GetUserName(MethodView):
    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).get_static_api_response()
        return render_success_response(response, message)


class GetUserDetails(MethodView):
    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response = SubApp1Service(params, headers)
        data = response.get_users()
        return jsonify({"data": data})

    @validate_request
    def post(self, params, headers, *args, **kwargs):
        data = request.get_json()
        response = SubApp1Service(params, headers).save_users(data)
        return jsonify({"data": response})

    @validate_request
    def delete(self, params, headers, *args, **kwargs):
        data = request.get_json()
        id = data.get("id")
        response = SubApp1Service(params, headers).delete_users(id)
        return jsonify({"data": response})

    @validate_request
    def put(self, params, headers, *args, **kwargs):
        data = request.get_json()
        id = data.get('id')
        response = SubApp1Service(params, headers).update_users(data, id)
        return jsonify({"data": response})












