import unittest
from TestRequests import *

class TestAPIPutRequests(unittest.TestCase):

    def test_put_requests(self):
        response = requests.post("https://reqres.in/api/users/2", json={"name": "anwar", "job": "Automation"})
        self.assertEqual(status_return(response), 201)
        self.assertEqual(status_text_return(response), "Request is successful")