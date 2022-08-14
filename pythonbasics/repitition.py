from asyncio.windows_events import NULL

class Categorization:


    

    #l=['BMW','Marcedes','Lexus','RangeRover','BMW','Marcedes','Lexus','RangeRover','BMW','Marcedes','Lexus','RangeRover']
   # l=[1,1,2,5,6,4,5,4,3,3,7,7,2,2,2,1]

    

    #print(l)
    def categorize(self,l):
        repitition=0
        listoftuple=[]
        l.sort()
        for i,v in enumerate(l):
            if i+1 !=len(l):
                 if l[i]==l[i+1]:
                     repitition+=1
                 else :
                     repitition+=1
                     tuple=(v,repitition)
                     listoftuple.append(tuple)
                     print(listoftuple)
                     repitition=0
            else:
                    repitition+=1
                    tuple=(v,repitition)
                    listoftuple.append(tuple)
                    print(listoftuple)
                    repitition=0
        return listoftuple

  #  print(listoftuple)
