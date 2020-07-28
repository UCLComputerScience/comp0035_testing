import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_index_page_valid(client):
    """
    GIVEN a Flask application
    WHEN the '/' home page is requested (GET)
    THEN check the response is valid (200 status code)
    """
    response = client.get('/')
    assert response.status_code == 200


def test_index_content(client):
    """
        GIVEN a Flask application
        WHEN the '/' home page is requested
        THEN check the response contains "Calculator"
        """
    response = client.get('/')
    assert 'Calculator' in str(response.data)


def test_response_contains(client):
    """
        GIVEN two terms have been entered correctly and add is selected and the form submitted
        WHEN the form is submitted from the index page
        THEN check the response URL is /result
        """
    assert True  # Write the code to implement this test


def test_result_content(client):
    """
        GIVEN two terms (3, 5) have been entered correctly and add is selected and the form submitted
        WHEN the form is submitted from the index page
        THEN check the result contains 8
        """
    assert True  # Write the code to implement this test