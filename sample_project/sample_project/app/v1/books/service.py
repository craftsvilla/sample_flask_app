from flask import jsonify

from app.connections import SqlConnection
class SubApp1Service:
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'demo'
    }

    db_connection = SqlConnection(db_config)

    def __init__(self, params, headers):
        self.params = params
        self.headers = headers

    def get_static_api_response(self):
        return self.params, 'success'

    def get_books(self):
        try:
            query = "select * from books"
            results =SubApp1Service.db_connection.query_db(query)
            if not results:
                return "no data found"
            return results
        except Exception as e:
            return f"error {e} "


    def save_book(self,data):
            if not data:
                return "data is not provided"

            title= data.get("title")
            author= data.get("author")

            if not author or not title:
                return "title and author are required"
            try:

                query = "select title from books"
                titles = SubApp1Service.db_connection.query_db(query)
                for i in titles:
                    if title == i.get("title"):
                        return "This title already taken"

                query = "insert into books(title, author) values(%s,%s)"
                values = (title,author)

                SubApp1Service.db_connection.write_db(query, values)
                return "data saved sucessfully"
            except Exception as e:
                return f" error to store data {e}"

    def update_book(self,data,id):

            if not id:
                return "please Enter ID"
            title = data.get("title")
            try:
                query = "update books set title=%s where id=%s"
                values = (title, id)
                self.db_connection.query_db(query, values)

                return "update data sucessfully"
            except Exception as e:
                return f" error when updating data {e}"

    def delete_book(self,id):
            if not id:
                return "please Enter id"
            try:
                query = "DELETE FROM books WHERE id = %s"
                SubApp1Service.db_connection.write_db(query, (id,))
                return "book deleted successfully"
            except Exception as e:
                return f"Failed to delete book: {e}"

    def get_book_by_id(self,id):
        try:
            query = "select * from books where id= %s "
            results =SubApp1Service.db_connection.query_db_one(query,id)
            if not results:
                return "no data found"
            return results
        except Exception as e:
            return f"error {e} "



