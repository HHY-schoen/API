import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":20, "name":"Joe", "views":654},
        {"likes":675, "name":"How to cook", "views":3456},
        {"likes":64, "name":"Kim", "views":78}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)

input()
response = requests.get(BASE + "video/2")
print(response.json())