import json
from pprint import pprint as print
from urllib import request
response = request.urlopen("https://jsonplaceholder.typicode.com/users")
json_response = response.read()
users = json.loads(json_response)

print(users)
print(users[0], depth=2, indent=4)
