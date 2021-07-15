import unittest
from TestRequests import *

class TestAPIPatchRequests(unittest.TestCase):
    
    def test_patch_requests(self):
        response = requests.patch("https://reqres.in/api/users/2", json={"name": "anwar", "job": "Automation Testing"})
        self.assertEqual(status_return(response), 200)
        self.assertEqual(status_text_return(response), "Request is successful")