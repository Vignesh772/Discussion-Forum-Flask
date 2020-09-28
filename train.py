
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import pickle

#df = pd.read_csv("test.csv")
#df1=pd.read_csv("data1.csv")
#df.dropna(inplace=True)
#df.to_csv("test1.csv")
df=pd.read_csv("disc_dataset.csv")
#df.dropna(inplace=True)

#df.head()
my_stop_words=text.ENGLISH_STOP_WORDS#.union(["book"])

#print(my_stop_words)
vectorizer = TfidfVectorizer(stop_words=my_stop_words)
print(np.concatenate((df.Question, df.Answer)))

vectorizer.fit(np.concatenate((df.Question, df.Answer)))
print("HELLO")
pickle.dump(vectorizer, open("model2.pk", 'wb'))
Question_vectors = vectorizer.transform(df.Question)
print(Question_vectors)
pickle.dump(Question_vectors, open("question_vector2.pk", 'wb'))

'''


l=df.shape[0]

dframe=pd.concat([df.Question , df.Answer],axis=1)
dframe.to_csv("disc_dataset.csv")

print(dframe.shape)
#df1=df.Question[0:l//2]  +  df.Answer[0:l//2]
df1=pd.concat([df.Question[0:l//2] , df.Answer[0:l//2]],axis=1)
print(df1.shape)
df1.to_csv("disc_dataset_bs_1.csv")

#df2=df.iloc[l//2:l,:]
df2=pd.concat([df.Question[l//2:l] , df.Answer[l//2:l]],axis=1)
print(df2.shape)
df2.to_csv("disc_dataset_bs_2.csv")'''
