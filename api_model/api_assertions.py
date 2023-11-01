def assert_response_status(response, expected_status_code):
    assert response.status_code == expected_status_code


def assert_response_contains(response, expected_content):
    assert expected_content in response.text
