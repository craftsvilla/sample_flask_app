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


    def get_users(self):
        try:
            query = "select * from users"
            results =SubApp1Service.db_connection.query_db(query)
            if not results:
                return "no data found"
            return results
        except Exception as e:
            return f"error {e} "


    def save_users(self,data):
            if not data:
                return "data is not provided"

            id= data.get("id")
            name= data.get("name")

            if not id or not name:
                return "id and name are required"
            try:

                query = "select * from users"
                names = SubApp1Service.db_connection.query_db(query)
                for i in names:
                    if name == i.get("name"):
                        return "This name already taken . "

                query = "insert into users(id, name) values(%s,%s)"
                values = (id,name)

                SubApp1Service.db_connection.write_db(query, values)
                return "data saved sucessfully"
            except Exception as e:
                return f" error to store data {e}"

    def update_users(self,data,id):
            if not id:
                return "please Enter ID"
            name = data.get("name")
            try:
                query = "update users set name=%s where id=%s"
                values = (name, id)
                self.db_connection.query_db(query, values)

                return "update data sucessfully"
            except Exception as e:
                return f" error when updating data {e}"

    def delete_users(self,id):
            if not id:
                return "please Enter id"
            try:
                query = "DELETE FROM users WHERE id = %s"
                SubApp1Service.db_connection.write_db(query, (id,))
                return "user deleted successfully"
            except Exception as e:
                return f"Failed to delete book: {e}"




