dic={'1': 20, '2': 40, '3': -90, '4': 100, '5': 70, '6': 0, '7':15, '8':60 }
Max=list(dic.values())
print(Max)
nuofdigits=int(input('no of digits needed'))
max=sorted(Max)
print(max)
print(max[-nuofdigits:])
//print(max[:nuofdigits])



