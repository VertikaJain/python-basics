# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

""" import datetime
today= datetime.date.today() """
# OR
from validator import validate_email #user defined
from camelcase import CamelCase  # pip modules
from datetime import date  # Core modules
today = date.today()
print(today)

# Install other libraries using: pip3 install lib-name
# To check installed libraries: pip3 freeze

c = CamelCase()
print(c.hump("hello geeks"))

email = "abc@test.com"
if(validate_email(email)):
    print("Valid email.")
else:
    print("Invalid email.")
