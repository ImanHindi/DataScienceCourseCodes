





def winner(blockhight):
    x=sum(map(lambda x:x-1,blockhight))%2
    #x=(sum(blockhight)%len(blockhight))%2
    print(x)
    if x:
        print('ps1')
    else:
        print('ps2')

winner([20,5,13,1])
winner([10,10,10,5,5])

#list1=['blue','red','red','blue','blue']

#list1.sort()
#uniquevalues=set(list1)
#x1=list.count(list1,'red')
#x2=list.count(list1,'blue')
#
#if x1>x2:
#    print('red')
#else:
#    print('blue')




