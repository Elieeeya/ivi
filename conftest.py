import os
import pytest
from api_model.api_methods import ApiMethods
from dotenv import load_dotenv

load_dotenv()

# Глобальные переменные для авторизации
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


@pytest.fixture
def api_helper():
    return ApiMethods(USERNAME, PASSWORD)
