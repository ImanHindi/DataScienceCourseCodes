# def myfunc():
#     print('Hello World')
#     print('no')


# myfunc()

# to expand the function you could add another print
# can't divide by zero
# we can add a condition or add a functionality without changing the function
# we can define a function inside a function in python

def check(func):
    def inside(a,b):
        if b== 0:
            print("can't divide by zero")
            return
        func(a,b)
    #to execute inside function
    return inside

@check
def div(a,b):
    return a/b


#instead of this repitive syntax we can use decorators
#div = check(div)
print(div(10,0))

