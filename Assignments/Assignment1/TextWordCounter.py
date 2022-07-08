import string

#this function is to count the repitition of each word in the list of words 
#arguments:unique words and the list of all words in the text,
#return a dictionary of keys =unique word, and values:the repitition of unique word

def string_words_count(wordkeys,wordslist):
    #creat a dictionary to save each word and its' repitition
    wordcounter=dict()
    #go through each unique word 
    for word in wordkeys:
        count=0
        #check through the list of words if there is a repitition for this unique word and catch it in side counter
        for eachword in wordslist:
            if eachword==word:
                count+=1
        wordcounter[word]=count
        

    return wordcounter


'''
receiving data
'''
#input the Text to be edited. and convert it to lower case letters
text=input('please insert a text' ).lower()



'''
text preprocessing
'''
#remove the punctuation from the text using maketrans method and replace it with nothing(empty qoutation) 
#using string library so we can select all punctuations marks through all the text.
edite_text=text.translate(str.maketrans('','',string.punctuation))

#print the edited text to double check the output of the previous operation
print(edite_text)

#convert the text to list of words 
str_list_of_words=edite_text=text.split(' ')

#print the list to double check the output of the previous operation
print(str_list_of_words)

#converted the list to set to find the unique words of the text (remove words repittition)
str_set_of_words=set(str_list_of_words)

#print the set to double check the output of the previous operation
print(str_set_of_words)

'''
text counting words' process:
'''

#call the counter function to count the repitition of each word in the text
word_counter=string_words_count(str_set_of_words,str_list_of_words)

'''
deliver output:
'''

print(word_counter)







