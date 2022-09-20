from time import time

def timer(func):
    print('carai')
    def f(x, y = 10):
        before = time()
        rv = func(x, y)
        after = time()
        print ( 'Elapsed', after - before)
        return rv
    return f

@timer
def add(x,y):
    return x + y
#add = timer(add) 
#The line above would be the way to use a decorator if the gramatics of @timer would not exist
#The core idea is to wrap behavior around

print('add(10)',     add(10))