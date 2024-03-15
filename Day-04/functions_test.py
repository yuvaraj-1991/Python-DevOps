#Calculator

import sys 

a = 10 #Global Scope Variable
b = 5  #Global Scope Variable

# Function -- 1
def add(a, b):
    #c = 20  # LocalScope Variable
    add = a + b 
    return add

# Function -- 2
def sub(a,b):
    sub = a - b
    return sub

def mul(a,b):
    mul = a * b
    return mul

# print(addition(10, 5, 10))
# print(sub(10,4))

a = int(sys.argv[1]) #reading value and saving it to a and converting it to number
operation = sys.argv[2] #reading the input if it's add/sub/mul
b = int(sys.argv[3]) #reading value and saving it to b and converting it to number

if operation == 'add':
    output = add(a,b)
    print(output)
elif operation == 'sub':
    output = sub(a,b)
    print(output)  
elif operation == 'mul':
    output = mul(a,b)
    print(output)    

  