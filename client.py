from server import handle_request

request = {
    "name": "Student",
    "id": 1,
    "grades": [80, 90, 85]
}

print("Average:", handle_request(request))
