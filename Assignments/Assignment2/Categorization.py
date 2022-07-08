
#this module is reusable module built to classify the unique items of the list and to calculate the repitition for each unique item 
#module input is list of any type of data 
#the output is a list of tuples of the unique items and it's repitition on the original list
class Categorization:
    def __init__(self):
         pass
    from asyncio.windows_events import NULL
    

    def categorize(l):
        repitition=0
        listoftuple=[]
        #sort the data so we can easily iterat through the list and check the similarities
        l.sort()
        for i,v in enumerate(l):
            # if statement to check that we reach to last element of the list to a voide an out of range error for i+1 

            if i+1 !=len(l):
                #this if statement is to check each element in the list with the next one and if it detect a similarities it will increase the repitition variable by one
                #if there is not similar it will be  increase the repition variable by one to catch the current item and add the unique item and it's repitition as a tuple to the list of tuples
                #and reset the repitition variable to zero so we can start new count for the next unique item and so on...
                 if l[i]==l[i+1]:
                     repitition+=1
                 else :
                     repitition+=1
                     tuple=(v,repitition)
                     listoftuple.append(tuple)
                     #print(listoftuple)
                     repitition=0
                #this else statement is to iterate the last item of the list the last item of the list 
            else:
                    repitition+=1
                    tuple=(v,repitition)
                    listoftuple.append(tuple)
                    repitition=0
        #after we iterate through all the item of the sorted list and find the repitition of each unique item we will return the 
        #out as list of tuples
        return listoftuple

    def string_words_count(wordslist):
     #creat a dictionary to save each word and its' repitition 
        wordcounter=dict()
     #go through each unique word 
        for word in wordslist:
            if word in wordcounter:
                wordcounter[word] += 1
            else:
                wordcounter[word] = 1

        print(dict.keys(max(wordcounter.values())))

        return  max(wordcounter.values())

         
    list1=['blue','red','red','blue','blue']
    string_words_count(list1)




   # l=[1,2,1,3,4,2,5,2,4,5,5,2,1,1]

    #print(string_words_count(l))
    #print(categorize(l))