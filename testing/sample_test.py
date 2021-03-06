import requests
import json
import pymysql as db

db_connect = db.connect(user='root', password='', database='emploees')
cur = db_connect.cursor(db.cursors.DictCursor)

cur.execute("SELECT * FROM emploees as e WHERE e.id IN (select id from emploees where id=4)")

print(cur.description)

print()

for row in cur:
    print(row["id"], ": ", row["name"])

BASE_URL = "https://reqres.in"

params = {'page': 2}
result = requests.get(BASE_URL + "/api/users", params=params)
print(json.dumps(result.json(), indent=2))

result_post = requests.post(BASE_URL + "/api/users", {"name": "Yevgen", "job": "QA"})

print(result_post.json())

if json.dumps(result.json(), indent=2).find("Yevgen"):
    print("Yay, Yevgen is here")
    response2 = requests.patch(BASE_URL + "/api/users", {"name": "Yevgen", "job": "Software Test Engineer"})
else:
    print("Nooooo")

print(json.dumps(response2.json(), indent=2))

req_register = requests.post(BASE_URL + "/api/register", {"email": "test@gmail.com", "password": "pass"})

print(json.dumps(req_register.json(), indent=3))

print("test succeded")

print("test succeded 2, that's great")

##data = json.load(json.dumps(req_register.json(), indent=3))

##print(data['token'])
