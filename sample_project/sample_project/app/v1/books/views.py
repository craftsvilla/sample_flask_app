import pymysql
from flask import jsonify, request
from flask.views import MethodView
from app.decorators import validate_request
from app.common_utils import render_success_response
from app.v1.books.service import SubApp1Service
from app.connections import SqlConnection




class GetBookDetails(MethodView):
    @validate_request
    def get(self, params, headers, id=None,*args, **kwargs):
        if not id:
            response = SubApp1Service(params, headers)
            data = response.get_books()
            return jsonify({"data": data})
        response=SubApp1Service(params, headers)
        data=response.get_book_by_id(id)
        return jsonify({"data":data})

    @validate_request
    def post(self, params, headers, *args, **kwargs):
        data = request.get_json()
        response = SubApp1Service(params, headers).save_book(data)
        return jsonify({"data": response})

    @validate_request
    def delete(self, params, headers, *args, **kwargs):
        data = request.get_json()
        id=data.get("id")
        response = SubApp1Service(params, headers).delete_book(id)
        return jsonify({"data": response})

    @validate_request
    def put(self, params, headers, *args, **kwargs):
        data = request.get_json()
        id = data.get('id')
        response = SubApp1Service(params, headers).update_book(data,id)
        return jsonify({"data": response})







