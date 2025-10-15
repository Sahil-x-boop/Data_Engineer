import pdb

def add(x, y):
    return x + y

def lets_add():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    pdb.set_trace()
    
    result = add(a, b)
    print("Result: ",result)
    
lets_add()