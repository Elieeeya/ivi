import pytest
import allure
from api_model.api_assertions import *


@allure.feature("API Testing")
class TestAPI:

    @pytest.fixture(autouse=True)
    def setup(self, api_helper):
        self.api = api_helper

    @allure.story("Post and Put Character")
    @allure.title("Test Post and Put Character")
    @allure.description("This test case performs POST and PUT operations for a character.")
    @pytest.mark.parametrize("character_data", [
        {
            "name": "Hawkeye",
            "universe": "Marvel Universe",
            "education": "High school (unfinished)",
            "weight": 104,
            "height": 1.90,
            "identity": "Publicly known"
        }
    ])
    def test_post_and_put_character(self, character_data):
        with allure.step("POST and PUT character"):
            response_post = self.api.post_character(character_data)
            allure.attach(response_post.text, name="Response POST", attachment_type=allure.attachment_type.TEXT)
            assert_response_status(response_post, 200)

            response_put = self.api.put_character(character_data)
            allure.attach(response_put.text, name="Response PUT", attachment_type=allure.attachment_type.TEXT)
            assert_response_status(response_put, 200)

    @allure.story("Successful Authentication")
    @allure.title("Test Successful Authentication")
    @allure.description("This test case performs successful authentication.")
    def test_successful_authentication(self):
        with allure.step("Performing authentication"):
            response = self.api.authenticate()
            allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.TEXT)
            assert_response_status(response, 200)

    @allure.story("Get Characters")
    @allure.title("Test Get Characters")
    @allure.description("This test case performs a GET request to retrieve characters.")
    def test_get_characters(self):
        with allure.step("GET characters"):
            response = self.api.get_characters()
            allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.TEXT)
            assert_response_status(response, 200)

    @allure.story("Get Character by Name")
    @allure.title("Test Get Character by Name")
    @allure.description("This test case performs a GET request to retrieve a character by name.")
    def test_get_character_by_name(self):
        character_name = 'Avalanche'
        with allure.step(f"GET character by name: {character_name}"):
            response = self.api.get_character_by_name(character_name)
            allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.TEXT)
            assert_response_status(response, 200)

    @allure.story("Delete Character by Name")
    @allure.title("Test Delete Character by Name")
    @allure.description("This test case performs a DELETE request to delete a character by name.")
    def test_delete_character_by_name(self):
        character_name = 'Abyss'
        with allure.step(f"DELETE character by name: {character_name}"):
            response = self.api.delete_character_by_name(character_name)
            allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.TEXT)
            assert_response_status(response, 200)

    @allure.story("Failed Delete Nonexistent Character")
    @allure.title("Test Failed Delete Nonexistent Character")
    @allure.description("This test case attempts to delete a nonexistent character.")
    def test_failed_delete_nonexistent_character(self):
        character_name = 'Vovan'
        with allure.step(f"DELETE nonexistent character by name: {character_name}"):
            response = self.api.delete_nonexistent_character(character_name)
            allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.TEXT)
            assert_response_contains(response, "No such name")

    @allure.story("Reset Collection")
    @allure.title("Test Reset Collection")
    @allure.description("This test case performs a POST request to reset the collection.")
    def test_reset_collection(self):
        with allure.step("POST reset collection"):
            response = self.api.reset_collection()
            allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.TEXT)
            assert_response_status(response, 200)