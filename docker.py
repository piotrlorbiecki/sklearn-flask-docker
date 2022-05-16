def decorator(function_as_parameter):
    def wrapper():
        print('first string theory')
        function_as_parameter()
        print('second string theory')
    return wrapper

def fun1():
    print('hello world')
[3]
f = decorator(fun1)
[4]
f()

!pip install flask-restful
from flask_restful import Api


