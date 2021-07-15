import unittest
from TestRequests import *
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

class TestAPIPostRequests(unittest.TestCase):

    def setUp(self):
        self.link = "https://reqres.in/api/"


    def test_post_200_requests(self):
        for row in Post_200_URLs:
            response = requests.post(url=self.link+row[0], json=row[1])
            test_response = requests.get(url=self.link+row[0])
            with self.subTest():
                self.assertEqual(status_return(response), 200)
                self.assertEqual(status_text_return(response), "Request is successful")
                self.assertIn(str(row[1]),json_printer(test_response))


    def test_post_201_requests(self):
        for row in Post_201_URLs:
            response = requests.post(url=self.link+row[0], json=row[1])
            test_response = requests.get(url=self.link + row[0])
            with self.subTest():
                self.assertEqual(status_return(response), 201)
                self.assertEqual(status_text_return(response), "Request is successful")
                self.assertIn(str(row[1]), json_printer(test_response))


    def test_post_400_requests(self):
        for row in Post_400_URLs:
            response = requests.post(url=self.link+row[0], json=row[1])
            test_response = requests.get(url=self.link + row[0])
            with self.subTest():
                self.assertEqual(status_return(response), 400)
                self.assertEqual(status_text_return(response), "Request is not successful")
                self.assertIn(str(row[1]), json_printer(test_response))

    def tearDown(self):
        print("done")