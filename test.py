x= 13
y=14
z=17

# add function adds two numbers x and y

def add (value1,value2):
    return value1+value2


# print Yes if sum of x and y is greater than sum y and z else print No
"""
operator can be ==, <=, >=, <, >
if(condition 1 operator condition 2):
    task
else:
    task
"""

if(add(x,y)>add(y,z)):
    print('Yes')
else:
    print('No')
