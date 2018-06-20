#__Exception

try:
    1/0
except ZeroDivisionError as e:
    print(str(e)+".But it is totally fine.")
print()

#__Custom Exception

class MyException(Exception):
    pass
try:
    raise MyException("Human-readable message")
except MyException as e:
    print("Your exception just occured with a message: "+str(e))
