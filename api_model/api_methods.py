import requests
import allure


class ApiMethods:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.BASE_URL = 'http://rest.test.ivi.ru/v2'

    @allure.step("Authenticate")
    def authenticate(self):
        response = requests.get(self.BASE_URL + '/characters', auth=(self.username, self.password))
        return response

    @allure.step("Get Characters")
    def get_characters(self):
        response = requests.get(self.BASE_URL + '/characters', auth=(self.username, self.password))
        return response

    @allure.step("Get Character by Name")
    def get_character_by_name(self, character_name):
        response = requests.get(self.BASE_URL + f'/character?name={character_name}',
                                auth=(self.username, self.password))
        return response

    @allure.step("Post Character")
    def post_character(self, character_data):
        response = requests.post(self.BASE_URL + '/character', json=character_data, auth=(self.username, self.password))
        return response

    @allure.step("Put Character")
    def put_character(self, character_data):
        response = requests.put(self.BASE_URL + '/character', json=character_data, auth=(self.username, self.password))
        return response

    @allure.step("Delete Character by Name")
    def delete_character_by_name(self, character_name):
        response = requests.delete(self.BASE_URL + f'/character?name={character_name}',
                                   auth=(self.username, self.password))
        return response

    @allure.step("Delete Nonexistent Character")
    def delete_nonexistent_character(self, character_name):
        response = requests.delete(self.BASE_URL + f'/character?name={character_name}',
                                   auth=(self.username, self.password))
        return response

    @allure.step("Reset Collection")
    def reset_collection(self):
        response = requests.post(self.BASE_URL + '/reset', auth=(self.username, self.password))
        return response
