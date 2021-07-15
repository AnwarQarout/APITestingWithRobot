import unittest
from TestRequests import *

class TestAPIDeleteRequests(unittest.TestCase):
    def test_delete_requests(self):
        response = requests.delete("https://reqres.in/api/users/2", json={"name": "anwar", "job": "Automation Testing"})
        self.assertEqual(status_return(response), 204)
        self.assertEqual(status_text_return(response), "Request is successful")