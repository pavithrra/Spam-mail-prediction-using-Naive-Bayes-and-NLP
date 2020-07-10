import pandas as pd
import workers
from multiprocessing import Pool
from multiprocessing import Process
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
import re
from sklearn.model_selection import train_test_split

df = pd.read_csv("ham_spam.csv", encoding = 'latin-1')

df = df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], axis=1)

def return_words(row):
    
    # consistent casing
    row = row.lower()
    
    # # Tokenization
    row = re.sub('[^A-Za-z0-9\s]+', '', row)
    words = word_tokenize(row)
    
    # Removing Common words - stop words
    clean_list = []
    stop_words = stopwords.words('english')
    stop_words.append(["etc", "also"])
    for word in words:
        if word not in stop_words:
            clean_list.append(word)
    
    # # Stemming - Using this one - the below ones are just for reference:
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    words = []
    for word in clean_list:
        w = lemmatizer.lemmatize(word,pos='a')
        if w == word:
            w = lemmatizer.lemmatize(w,pos='v')
        if w == word:
            w = lemmatizer.lemmatize(w,pos='n')
        if (w == word) and (len(w)) > 3:
            w = stemmer.stem(w)
        words.append(w)
        
    words = list(set(words))

    return words


df['words'] = df['v2'].apply(lambda x: return_words(x))
#workers.mapping_parallelize(df[:5])

import os

def info(title):
    print(title)
    print('module name:', __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
	# info('main line')
	# p = Process(target=workers.mapping_parallelize, args=(df,))
	# p.start()
	# p.join()

	df2 = pd.read_csv("test.csv")

	
	from sklearn.model_selection import train_test_split
	X = df2
	y = df1["v1"]
	y = y.str.replace("ham",'0').str.replace("spam",'1')

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

	from sklearn.naive_bayes import MultinomialNB
	model = MultinomialNB().fit(X_train, y_train)

	model.score(X_test, y_test)

	




