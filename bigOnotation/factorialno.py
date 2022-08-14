import time

def no_factorial(number):
    if number >=1:
       return number*no_factorial(number-1)
    return 1

start = time.time()
print(no_factorial(20))
print(time.time()-start)



def Fapunichi(number):
    if number >1:
        return Fapunichi(number-1)+Fapunichi(number-2)

    return 1


start1 = time.time()
print(Fapunichi(20))
print(time.time()-start1)
