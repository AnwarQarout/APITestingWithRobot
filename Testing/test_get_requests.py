import unittest
from TestRequests import *




Get_200_URLs = ["users?page=2", "users/2",
                "unknown",
                "unknown/2",
                "users?delay=3"]

Get_404_URLs = ["users/23", "unknown/23"]

class TestAPIGetRequests(unittest.TestCase):

    def setUp(self):
        self.link = "https://reqres.in/api/"

    def test_get_200_requests(self):
        for url in Get_200_URLs:
            response = requests.get(url=self.link+url)
            with self.subTest():
                self.assertEqual(status_return(response), 200)
                self.assertEqual(status_text_return(response), "Request is successful")


    def test_get_404_requests(self):
        for url in Get_404_URLs:
            response = requests.get(url=self.link+url)
            with self.subTest():
                self.assertEqual(status_return(response), 404)
                self.assertEqual(status_text_return(response), "Request is not successful")

    def tearDown(self):
        print("done")