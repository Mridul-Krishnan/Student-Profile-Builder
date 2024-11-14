#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import sklearn
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import euclidean_distances


index=0
df= pd.read_csv('final_web.csv')
def find_index(l):
	print("tfidf")
	links= df.Link.values
	index=np.where(links==l)
	recommend(int(index[0]))
	
	
	
dataf= pd.DataFrame(columns=['Title','Link'])
stopword_list= stopwords.words('english')
vectorizer= TfidfVectorizer(analyzer='word')
tfidf_matrix= vectorizer.fit_transform(df['Text'])

tfidf_feature_name= vectorizer.get_feature_names()

cosine_similarity= linear_kernel(tfidf_matrix, tfidf_matrix)

df= df.reset_index(drop=True)
indices= pd.Series(df['Title'].index)

def recommend(index):
	print("recommending")
	ids= indices[index]
	similarity_scores= list(enumerate(cosine_similarity[ids]))
	similarity_scores= sorted(similarity_scores, key= lambda x:x[1], reverse=True)
	similarity_scores= similarity_scores
	#print(similarity_scores)

	a_index= [i[0] for i in similarity_scores]

	# print( *df['title'].loc[a_index], sep='\n')
	# print(*df['link'].iloc[a_index],sep='\n')
	i=1
	for x in a_index[1:]:
		#dataf.loc[i,'Sno']=i
		dataf.loc[i,'Title']= df['Title'].loc[x]
		dataf.loc[i,'Link']= df['Link'].loc[x]
		i=i+1
        
	dataf.to_csv('articles2.csv',index= None, header= True)
	
        




