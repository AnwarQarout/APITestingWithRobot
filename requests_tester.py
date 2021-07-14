import unittest
import requests
from TestRequests import *

Get_200_URLs = ["https://reqres.in/api/users?page=2", "https://reqres.in/api/users/2",
                "https://reqres.in/api/unknown",
                "https://reqres.in/api/unknown/2",
                "https://reqres.in/api/users?delay=3"]

Get_404_URLs = ["https://reqres.in/api/users/23", "https://reqres.in/api/unknown/23"]

Post_201_URLs = [("https://reqres.in/api/users", {"name": "anwar", "job": "leader"})]

Post_200_URLs = [("https://reqres.in/api/register", {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}), ("https://reqres.in/api/login", {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
})]

Post_400_URLs = [("https://reqres.in/api/register", {
    "email": "sydney@fife"
}), ("https://reqres.in/api/login", {
    "email": "sydney@fife"
})]


class TestAPI(unittest.TestCase):

    def test_get_requests(self):
        for url in Get_200_URLs:
            response = requests.get(url)
            with self.subTest():
                self.assertEqual(status_return(response), 200)
                self.assertEqual(status_text_return(response), "Request is successful")

        for url in Get_404_URLs:
            response = requests.get(url)
            with self.subTest():
                self.assertEqual(status_return(response), 404)
                self.assertEqual(status_text_return(response), "Request is not successful")

    def test_post_requests(self):
        for row in Post_200_URLs:
            response = requests.post(row[0], json=row[1])
            with self.subTest():
                self.assertEqual(status_return(response), 200)
                self.assertEqual(status_text_return(response), "Request is successful")

        for row in Post_201_URLs:
            response = requests.post(row[0], json=row[1])
            with self.subTest():
                self.assertEqual(status_return(response), 201)
                self.assertEqual(status_text_return(response), "Request is successful")

        for row in Post_400_URLs:
            response = requests.post(row[0], json=row[1])
            with self.subTest():
                self.assertEqual(status_return(response), 400)
                self.assertEqual(status_text_return(response), "Request is not successful")

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
