

l=[5,1,4,2,8,9,6,10,7,11,25,4,3]

def sort_fun(l,length,x):
    for i in range(length):
        if length==1:
            return l
        if i+1<=length-1:
            if l[i]>l[i+1] :
                max=l[i]
                l[i]=l[i+1]
                l[i+1]=max  
    x=x+1
    length=len(l)-x
    return    sort_fun(l,length,x)

#def sort_fun(l):
#
#    for i in range(len(l)):
#       for v in range(len(l)-i-1):
#            if l[v]>l[v+1]:
#                max=l[v]
#                l[v]=l[v+1]
#                l[v+1]=max  
#    return l

print(sort_fun(l,len(l),0))