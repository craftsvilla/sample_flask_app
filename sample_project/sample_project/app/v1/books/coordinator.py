
from app.connections import SqlConnection
from config import Config
class BookCordinator:
    db_config = Config.db_config
    db_connection = SqlConnection(db_config)

    def get_all_books(self):
        try:
            query = "select author.name as author_name , books.title , books.id , books.created_at ,books.updated_at from books inner join author on author.id=books.author_id"
            results = BookCordinator.db_connection.query_db(query)
            if not results:
                return "no data found"
            return results
        except Exception as e:
            return f"error {e} "


    def save_book_data(self,data):
        if not data:
            return "data is not provided"

        title = data.get("title")
        name=data.get("author_name")

        query = "select title from books"
        titles = BookCordinator.db_connection.query_db(query)
        for i in titles:
            if title == i.get("title"):
                return "This title already taken"

        query = "select name from author"
        names= BookCordinator.db_connection.query_db(query)
        names_list=[]
        for i in names:
            names_list.append(i.get("name"))



        if name not in names_list:
            query = "insert into author(name) values(%s)"
            values = (name,)
            author = BookCordinator.db_connection.query_db(query, values)

            query1 = "select id from author where name=%s"
            value=(name,)
            id= BookCordinator.db_connection.query_db(query1,value)
            author_id=id[0].get("id")

            query = "insert into books(title, author_id) values(%s,%s)"
            values = (title, author_id)
            BookCordinator.db_connection.write_db(query, values)
            return "data saved sucessfully"

        query1 = "select id from author where name=%s"
        value = (name,)
        id = BookCordinator.db_connection.query_db(query1,value)
        author_id = id[0].get("id")
        query = "insert into books(title, author_id) values(%s,%s)"
        values = (title, author_id)

        BookCordinator.db_connection.write_db(query, values)
        return "data saved sucessfully"


    def update_book_data(self,data,id):

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

    def delete_book_data(self,id):
            if not id:
                return "please Enter id"
            try:
                query = "DELETE FROM books WHERE id = %s"
                BookCordinator.db_connection.write_db(query, (id,))
                return "book deleted successfully"
            except Exception as e:
                return f"Failed to delete book: {e}"

    def get_book_data_by_id(self,id):
        try:
            query = "select author.name as author_name , books.title from books inner join author on author.id=books.author_id where books.id=%s "
            results = BookCordinator.db_connection.query_db_one(query, id)

            if not results:
                return "no data found"
            # response={
            #     "title":results["title"],
            #     "author_name":results["author_name"]
            #  }
            return results
        except Exception as e:
            return f"error {e} "

