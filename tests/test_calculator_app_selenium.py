'''
PLEASE READ
It is unlikely that you will be able to run this code unless you have Safari and have already enabled Selenium (see
Driver Requirements and scroll down to Safari: https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
Refer to the Selenium Webdriver documentation for the driver that matches your browser and operating system
https://www.selenium.dev/documentation/en/getting_started/
Selenium requires a server to be running with the app, this is provided by using the flask-testing library
LiveServerTestCase class. flask-testing requires the BaseTest to be defined with the use of setup and teardown rather
than fixtures. The syntax is therefore different to the examples you have seen so far.
Other differences you will see is the use of waits. These are added to ensure that the values we are looking for have
been loaded in the DOM before we test for them, otherwise a test may fail due to the web page not yet having loaded
rather than an error in the code.
NOTE:
You are not expected to do implement this for the COMP0035 coursework. This is more complex than you would be expected
to learn at this stage, however if wish to explore this now you will find it useful for COMP0034 (where some browser
based testing is expected).
'''
import time

import urllib3
from flask import url_for
from flask_testing import LiveServerTestCase
from selenium.webdriver import Safari
from selenium.webdriver.support.select import Select

from app import app


class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        """Setup the test driver for Safari"""
        self.driver = Safari()
        self.driver.get(self.get_server_url())

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        http = urllib3.PoolManager()
        response = http.request('GET', self.get_server_url())
        self.assertEqual(response.status, 200)


class TestCalculatorApp(TestBase):
    def test_h1_contains_calculator(self):
        # Navigate to the homepage
        self.driver.get("http://127.0.0.1:5000/")
        # Wait for 5 seconds
        self.driver.implicitly_wait(5)
        # Get the text contents of first heading which has an id of 'heading_1'
        h1 = self.driver.find_element_by_id('heading_1').text
        # Check that the text includes the word 'Calculator'
        assert 'Calculator' in str(h1)

    def test_add_returns_result_page(self):
        # Navigate to the homepage
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.implicitly_wait(10)

        # Locate the inputs in the form and enter the values
        self.driver.find_element_by_id("first_term").send_keys(5)
        self.driver.find_element_by_id("second_term").send_keys(7)
        operation = Select(self.driver.find_element_by_id("operation"))
        operation.select_by_visible_text('Add')
        self.driver.find_element_by_id("submit").click()
        self.driver.implicitly_wait(10)

        # Assert that browser redirects to the result page
        assert (url_for('result') in str(self.driver.current_url))

    def test_add_returns_correct_result(self):
        # Navigate to the homepage
        self.driver.get("http://127.0.0.1:5000/")
        time.sleep(3)

        # Locate the inputs in the form and enter the values
        self.driver.find_element_by_id("first_term").send_keys(5)
        self.driver.find_element_by_id("second_term").send_keys(7)
        operation = Select(self.driver.find_element_by_id("operation"))
        operation.select_by_visible_text('Add')
        time.sleep(3)
        self.driver.find_element_by_id("submit").click()

        # Assert that the value of the result on the form is 12 (the result is displayed in the placeholder attribute)
        r = self.driver.find_element_by_id("result").get_attribute("placeholder")
        assert '12' in str(r)
