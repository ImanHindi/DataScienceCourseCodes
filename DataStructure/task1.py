import re
from string import ascii_letters
from tkinter import Y
import numpy as np
from pyparsing import Regex


x=np.array([['c','b','a'],['f','b','g'],['c','l','n']])

y=np.sort(x)
print(y)

for i in range(3):

    if np.sort((x[:,i])).any!=y[:,i].any:

        print("false") 
    else:
        print("true") 

#y=x.argsort()

text='7863234hjgjh2g47823640000000000000000'

x=text[:re.search(".0{4}", text).end()]
print(x)