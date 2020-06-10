print("REQUESTING SOME DATA FROM THE INTERNET...")

#PART ONE

import requests

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)


import json

product = json.loads(response.text)

print(type(product)) #> <class 'dict'>

print(product["name"]) #> {'first_name': 'Ophelia', 'last_name': 'Clarke', 'message': 'Hi, thanks for the ice cream!', 'fav_flavors': ['Vanilla Bean', 'Mocha', 'Strawberry']}

#PART TWO

import requests

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)


import json

cream = json.loads(response.text)

Matched_Cream = []
for n in cream:
    print(n["id"],n["name"])

#PART THREE

import requests

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
students = requests.get(request_url)
print(response.status_code)
print(students.text)


import json

students = json.loads(students.text)

grades = []

for g in students:
   grades.append[g["finalGrade"]]
    
print(min[grades])
print(max[grades])