#__Join two arrays

import json

'''array_of_strings_one='["one","two"]'
array_of_strings_two='["three","four"]'

def join_two_arrays(array_of_strings_one,array_of_strings_two):
    list_one=json.loads(array_of_strings_one)
    list_two=json.loads(array_of_strings_two)
    joined_list=list_one+list_two
    return json.dumps(joined_list)
print (join_two_arrays(array_of_strings_one,array_of_strings_two)) '''


#__check json value

def jsonize_if_not_already_json(value):
    try:
        value=json.loads(value)
    except ValueError:
        pass
    return json.dumps(value)
print(jsonize_if_not_already_json("one"))
print(jsonize_if_not_already_json('"ONE"'))
print(jsonize_if_not_already_json('False'))
print(jsonize_if_not_already_json("false"))
print(jsonize_if_not_already_json("1"))
print(jsonize_if_not_already_json('1'))