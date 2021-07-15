import unittest
import requests
from TestRequests import *

Get_200_URLs = ["users?page=2", "users/2",
                "unknown",
                "unknown/2",
                "users?delay=3"]

Get_404_URLs = ["users/23", "unknown/23"]

Post_201_URLs = [("users", {"first_name": "anwar", "job": "leader"})]

Post_200_URLs = [("register", {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}), ("login", {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
})]

Post_400_URLs = [("register", {
    "email": "sydney@fife"
}), ("login", {
    "email": "sydney@fife"
})]


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.link = "https://reqres.in/api/"

    def test_get_requests(self):
        for url in Get_200_URLs:
            response = requests.get(url=self.link+url)
            with self.subTest():
                self.assertEqual(status_return(response), 200)
                self.assertEqual(status_text_return(response), "Request is successful")

        for url in Get_404_URLs:
            response = requests.get(url=self.link+url)
            with self.subTest():
                self.assertEqual(status_return(response), 404)
                self.assertEqual(status_text_return(response), "Request is not successful")



    def test_post_requests(self):
        for row in Post_200_URLs:
            response = requests.post(url=self.link+row[0], json=row[1])
            test_response = requests.get(url=self.link+row[0])
            with self.subTest():
                self.assertEqual(status_return(response), 200)
                self.assertEqual(status_text_return(response), "Request is successful")
                self.assertIn(str(row[1]),json_printer(test_response))


        for row in Post_201_URLs:
            response = requests.post(url=self.link+row[0], json=row[1])
            test_response = requests.get(url=self.link + row[0])
            with self.subTest():
                self.assertEqual(status_return(response), 201)
                self.assertEqual(status_text_return(response), "Request is successful")
                self.assertIn(str(row[1]), json_printer(test_response))


        for row in Post_400_URLs:
            response = requests.post(url=self.link+row[0], json=row[1])
            test_response = requests.get(url=self.link + row[0])
            with self.subTest():
                self.assertEqual(status_return(response), 400)
                self.assertEqual(status_text_return(response), "Request is not successful")
                self.assertIn(str(row[1]), json_printer(test_response))




    def test_put_requests(self):
        response = requests.post("https://reqres.in/api/users/2", json={"name": "anwar", "job": "Automation"})
        self.assertEqual(status_return(response), 200)
        self.assertEqual(status_text_return(response), "Request is successful")



    def test_patch_requests(self):
        response = requests.patch("https://reqres.in/api/users/2", json={"name": "anwar", "job": "Automation Testing"})
        self.assertEqual(status_return(response), 200)
        self.assertEqual(status_text_return(response), "Request is successful")



    def test_delete_requests(self):
        response = requests.delete("https://reqres.in/api/users/2", json={"name": "anwar", "job": "Automation Testing"})
        self.assertEqual(status_return(response), 204)
        self.assertEqual(status_text_return(response), "Request is successful")


    def tearDown(self):
        print("done")