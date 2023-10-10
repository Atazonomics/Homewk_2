import pandas as pd
import pytest

# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#
def car_at_light(light):
    if light == 'red':
        return 'stop'
    elif light == 'green':
        return 'go'
    elif light == 'yellow':
        return 'wait'
    else:
        raise Exception(f"Undefined instruction for color: {light}")

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 
def safe_subtract(val1, val2):
    try:
        if type(val2) in [int, float] and type(val1) in [int, float]:
            return val1 - val2
        else:
            return None
    except Exception as e:
        print('exception occurred ' + str(e))
# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

def retrieve_age_lbyl(dictionary):
    if 'birth' in dictionary.keys():
        return dictionary['birth']
    else:
        return None

def retrieve_age_eafp(dictionary):
    try:
        return dictionary['birth']
    except Exception as e:
        print('exception occurred ' + str(e))

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#
def read_data(file_name):
    try:
        return pd.read_csv(file_name)
    except Exception as e:
        print('exception occurred ' + str(e))

# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings += string+"_"

### (c) Careful!
j=10
while j > 0:
   j -= 1

### (d)
productory = 1
for elem in [1, 5, 25]:
    productory *= elem


def test_functions():
    assert car_at_light('green') == 'go'
    assert car_at_light('red') == 'stop'
    assert car_at_light('yellow') == 'wait'
    with pytest.raises(Exception):
        car_at_light('greasdfen') == Exception
    assert safe_subtract('asdf','asd') == None
    assert safe_subtract(5,10) == -5
    assert retrieve_age_lbyl({'name': 'John', 'last_name': 'Doe', 'birth': 1987}) == 1987
    assert retrieve_age_lbyl({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}) == None 
    assert retrieve_age_eafp({'name': 'John', 'last_name': 'Doe', 'birth': 1987}) == 1987
    with pytest.raises(Exception):
        assert retrieve_age_eafp({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})
    assert read_data('data.csv') is not None
    assert read_data('data1.csv') is None