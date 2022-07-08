import string

def string_words_count(wordkeys,stingwords):
    
    wordcounter=dict()
    for word in stingwords:
        if word in wordcounter:
            wordcounter[word] += 1
        else:
            wordcounter[word] = 1


    
    return wordcounter

text=input('please insert a text' ).lower()
edite_text=text.translate(str.maketrans('','',string.punctuation))

print(edite_text)


str_list_of_words=edite_text=text.split(' ')

print(str_list_of_words)

str_set_of_words=set(str_list_of_words)

print(str_set_of_words)

word_counter=string_words_count(str_set_of_words,str_list_of_words)

print(word_counter)









