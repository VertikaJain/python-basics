# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

userJSON = '{ "name" : "vertika", "age" : 25}'  # create JSON

user = json.loads(userJSON)  # returns a dictionary
print(user)
print(type(user))
print(user["name"])

# create json from dictionary
company = {
    'name': 'amazon',
    'location': 'bangalore'
}

companyJSON = json.dumps(company)
print(companyJSON)
print(type(companyJSON)) # string/json
print(type(company)) # dictionary
