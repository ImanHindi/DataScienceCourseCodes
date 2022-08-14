
from numpy import true_divide



def fun(l,x):
    ind=int(len(l)/2)
    if l[ind]==x:
        print(True)
        pass
    elif l[ind]>x and ind!=1:
        print(l[:ind],x)        
        fun(l[:ind],x)
    elif l[ind]<x and ind!=1:
        print(l[ind:],x)
        fun(l[ind:],x)
    elif ind==1:
        print(False)
l=[1,2,3,4,5,6,2,6,9,10,2]
l.sort()


fun(l,1)