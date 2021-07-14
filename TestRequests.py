import json

import requests

def status_text_return(response):
    print(response.status_code)
    if response:  # Between 200 - 400
        print("Request is successful")
        return "Request is successful"
    else:
        print("Request is not successful")
        return "Request is not successful"


def status_return(response):
    status_text_return(response)
    return response.status_code


def json_printer(response):
    print("---Printing Json Response...---")
    print(response.json())


def headers_printer(response):
    print("---Printing Response Headers..---")
    print(response.headers)

"""
print("-------- sending GET request https://reqres.in/api/users?page=2 --------")
response = requests.get("https://reqres.in/api/users?page=2")
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- sending GET request https://reqres.in/api/users/2 --------")
response = requests.get("https://reqres.in/api/users/2")
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- sending GET request https://reqres.in/api/users/23 --------")
response = requests.get("https://reqres.in/api/users/23")
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- sending GET request https://reqres.in/api/unknown --------")
response = requests.get("https://reqres.in/api/unknown")
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- sending GET request https://reqres.in/api/unknown/2 --------")
response = requests.get("https://reqres.in/api/unknown/2")
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- sending GET request https://reqres.in/api/unknown/23 --------")
response = requests.get("https://reqres.in/api/unknown/23")
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- sending GET request https://reqres.in/api/users?delay=3 --------")
response = requests.get("https://reqres.in/api/users?delay=3")
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")"""

"""
print("-------- Sending POST request https://reqres.in/api/users --------")
response = requests.post("https://reqres.in/api/users", json={"name": "anwar", "job": "leader"})
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- Sending POST request https://reqres.in/api/register --------")
response = requests.post("https://reqres.in/api/register", json={
    "email": "sydney@fife"
})
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- Sending POST request https://reqres.in/api/login --------")
response = requests.post("https://reqres.in/api/login", json={
    "email": "sydney@fife"
})
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- Sending POST request https://reqres.in/api/register --------")
response = requests.post("https://reqres.in/api/register", json={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
})
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- Sending POST request https://reqres.in/api/login --------")
response = requests.post("https://reqres.in/api/login", json={
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
})
json_printer(response)
headers_printer(response)
status_return(response)
print(response.url)"""


print("-------- Sending PUT request https://reqres.in/api/users/2 --------")
response = requests.post("https://reqres.in/api/users/2", json={"name": "anwar", "job": "Automation"})
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- Sending PATCH request https://reqres.in/api/users/2 --------")
response = requests.patch("https://reqres.in/api/users/2", json={"name": "anwar", "job": "Automation Testing"})
json_printer(response)
headers_printer(response)
status_return(response)

print("\n\n")

print("-------- Sending DELETE request https://reqres.in/api/users/2 --------")
response = requests.delete("https://reqres.in/api/users/2", json={"name": "anwar", "job": "Automation Testing"})
headers_printer(response)
status_return(response)


