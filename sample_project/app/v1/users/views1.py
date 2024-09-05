from flask.views import MethodView
from app.decorators import validate_request
from app.common_utils import render_success_response
from app.v1.users.service import SubApp1Service
from flask import jsonify
from flask import request
from app.connections import SqlConnection
import pymysql




# Database connection
def db_connection():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'db'
    }
    connection = pymysql.connect(**db_config)
    return(connection) 
db_connection()


class User_Book_API(MethodView):
    def get(self, id=None):
        conn = db_connection()
        cursor = conn.cursor()
        if id is None:
            cursor.execute("SELECT * FROM books")
            users = cursor.fetchall()
            return jsonify(users)
        else:
            cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
            user = cursor.fetchone()
            if user is None:
                return jsonify({"message": "books not found"})
            return jsonify(user)

    
    def post(self):
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')

        if not title or not author:
            return jsonify({"message": "title and author are required"})
        
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO books (title,author) VALUES (%s, %s)"
        cursor.execute(query, (title,author))
        conn.commit()
        new_user_id = cursor.lastrowid
        cursor.close()
        conn.close()

        return jsonify({"message": "books created successfully", "user_id": new_user_id})

    def put(self):
        data = request.get_json()
        id = data.get('id')
        title = data.get('title')
        author = data.get('author')

        if not title or not author:
            return jsonify({"message": "Title and author are required"})

        conn = db_connection()
        cursor = conn.cursor()
        query = "UPDATE books SET title = %s, author = %s WHERE id = %s"
        values = (title, author, id)
        cursor.execute(query, values)
        conn.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            conn.close()
            return jsonify({"message": "Book not found"})
        
        cursor.close()
        conn.close()
        
        return jsonify({"message": "Book updated successfully"})

    def delete(self):
        data = request.get_json()
        book_id = data.get('id')

        if not book_id:
            return jsonify({"message": "Book ID is required"})

        conn = db_connection()  
        cursor = conn.cursor()

        query = "DELETE FROM books WHERE id = %s"
        values = (book_id,)
        
        cursor.execute(query, values)
        conn.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            conn.close()
            return jsonify({"message": "Book not found"})

        cursor.close()
        conn.close()

        return jsonify({"message": "Book deleted successfully"}), 200


