#from lib2to3.pgen2.tokenize import tokenize
#import nltk
#from nltk.corpus import reuters,stopwords
#from nltk import sent_tokenize,word_tokenize
#from string import punctuation
#from nltk.stem import PorterStemmer
#from nltk.stem import WordNetLemmatizer
#nltk.download('reuters')
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
##print(reuters.fileids())
#
#print(len(reuters.words()))
#
#rawtext=reuters.raw('test/15500')
#print(rawtext)
#print(sent_tokenize(rawtext))
#
#
#for sen in sent_tokenize(rawtext):
#    print(word.lower() for word in word_tokenize(sen))
#
##remove un usefull words:
#stopwords_en=set(stopwords.words('english'))
##tokenize_lc=list(map(str.lower,word_tokenize(rawtext)))
##print(word for word in tokenize_lc if word  not in stopwords_en)
##punctuation:
#
##print('from string.punctuation:',type(punctuation),punctuation)
#punct_stopwords=stopwords_en.union(set(punctuation))
#tokenize_lc=list(map(str.lower,word_tokenize(rawtext)))
#print([word for word in tokenize_lc if word  not in punct_stopwords])
#
#
##stemming and lemmatization:
##difference stemming for suffix and prefix, lemmatization takes the meaning and the location 
##of the word in the sentence
#stemming=PorterStemmer()
#lemma=WordNetLemmatizer()
#words=['programs','programmer','programing','studies','goes']
#for w in words:
#    print(stemming.stem(w))
#for w in words:
#    print(lemma.lemmatize(w))

#NLP text preprocessing BOW:

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

corpus =['cats and dogs are not allowed','cats and dogs are antagonistic']
countvec=CountVectorizer()
x=countvec.fit_transform(corpus)
print(x)

df=pd.DataFrame()
df['voc']=countvec.get_feature_names()
print(df.head(10))

#NLP text preprossessing N-gram

sent='I like dancing in the rain'
from nltk import ngrams

ngram=ngrams(sent.split(' '),n=2)

print([x for x in ngram])


#NLP text preprossessing TF-IDF:


from sklearn.feature_extraction.text import TfidfVectorizer
corpus=['cats have four legs',
        'cats and dogs are antagonistic',
        'he hate dogs'
        ]

tfidf=TfidfVectorizer()
vect=tfidf.fit_transform(corpus)
print(vect)
df=pd.DataFrame()
df['vocabulary']=tfidf.get_feature_names()
df['sentence1']=vect.toarray()[0]
df['sentence2']=vect.toarray()[1]
df['sentence3']=vect.toarray()[2]

df.set_index('vocabulary',inplace=True)
print(df)