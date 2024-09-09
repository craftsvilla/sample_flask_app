from app.connections import SqlConnection
from .coordinator import UserCordinator

class SubApp1Service:
    def __init__(self, params, headers):
        self.params = params
        self.headers = headers
        self.cordinator=UserCordinator()

    def get_static_api_response(self):
        return self.params, 'success'


    def get_users(self):
        response=self.cordinator.get_users_data()
        return response




    def save_users(self,data):
        response=self.cordinator.save_users_data(data)
        return response

    def update_users(self,data,id):
        response = self.cordinator.update_users_data(data,id)
        return response

    def delete_users(self,id):
        response = self.cordinator.delete_users_data(id)
        return response





