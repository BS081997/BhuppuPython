'''import re

a=re.search(r'..d','food baar')
print(a) '''
import math

'''import re
def is_valid_Python_variable_name(string):
    found = re.match("[_A-Za-z][_a-zA-Z0-9]*",string)
    return  bool(found)
print(is_valid_Python_variable_name("the"))
'''

'''import re
def get_number_of_occurrences(string,substring):
    findings = list(re.finditer(substring,string))
    return len(findings)
print(get_number_of_occurrences("If life were predictable it would cease to be life, and be without flavor","life"))
'''


a=math.sin(math.radians(30))
print(a)
b=math.sin(math.radians(60))
print(b)

a=math.pi
print(a)

b=math.e
print(b)

c=math.sqrt(16)
print("c= ",c)