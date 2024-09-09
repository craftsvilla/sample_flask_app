from flask import jsonify

from app.connections import SqlConnection
from config import Config
from .coordinator import BookCordinator
class SubApp1Service:
    def __init__(self, params, headers):
        self.params = params
        self.headers = headers
        self.cordinator=BookCordinator()

    def get_static_api_response(self):
        return self.params, 'success'

    def get_books(self):
        response=self.cordinator.get_all_books()
        return response


    def save_book(self,data):
        response=self.cordinator.save_book_data(data)
        return response



    def update_book(self,data,id):
        response=self.cordinator.update_book_data(data,id)
        return response


    def get_book_by_id(self,id):
        response=self.cordinator.get_book_data_by_id(id)
        return response

    def delete_book(self,id):
        response = self.cordinator.delete_book_data(id)
        return response







