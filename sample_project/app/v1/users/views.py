from flask.views import MethodView
from app.decorators import validate_request
from app.common_utils import render_success_response
from app.v1.users.service import SubApp1Service
from flask import jsonify
from flask import request
from app.connections import SqlConnection
import pymysql



def db_connection():
    # conn=mysql.connector.connect(host='localhost',user="root",password="root",database= "demo")
    # cur=conn.cursor()


    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'db'
    }


    connection = pymysql.connect(**db_config)
    return(connection) 
db_connection()
class GetUserName(MethodView):

    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).get_static_api_response()
        return render_success_response(response, message)

class GetUserDetails(MethodView):
    def get(self):
       conn = db_connection()
       cursor = conn.cursor(pymysql.cursors.DictCursor)
       query = "SELECT * FROM employee"
       cursor.execute(query)
       results = cursor.fetchall()
       cursor.close()
       conn.close()
       return jsonify({"message": "GET: Data received", "data": results})
    

    
    @validate_request
    def post(self, *args, **kwargs):
        data = request.get_json()
        id = data.get('id')
        name = data.get('name')

        conn = db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO employee (id, name) VALUES (%s, %s)"
        values = (id, name) 

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "No user found with the provided ID"})

        cursor.close()
        conn.close()

        return jsonify({"message": "User created successfully"})


    @validate_request
    def put(self, *args, **kwargs):
        data = request.get_json()
        id = data.get('id')
        name = data.get('name')
        
        
        conn = db_connection()
        cursor = conn.cursor()

        query = "UPDATE employee SET name=%s WHERE id=%s"
        values = (name, id)  

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "No user found with the provided ID"})

        cursor.close()
        conn.close()

        return jsonify({"message": "User updated successfully"})
    

    @validate_request
    def delete(self, *args, **kwargs):
        id = request.args.get('id') 

        if not id:
            return jsonify({"message": "ID is required"}), 400

        conn = db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM employee WHERE id = %s"
        values = (id,)

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "No user found with the provided ID"}), 404

        cursor.close()
        conn.close()

        return jsonify({"message": "User deleted successfully"}), 200