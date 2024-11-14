#!/usr/bin/env python
# coding: utf-8

# **Importing all the required packages**
import csv
import pandas as pd
import numpy as np
import nltk
#nltk.download('all-corpora')
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize
#nltk.download('stopwords')
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_–~'''
stop_words= set(stopwords.words('english'))

df= pd.read_csv('final_web.csv')


def tag_search(tag):
	newdf=pd.DataFrame(columns=['Title','Link','Text','Tag'])
	c=1
	for i in range(len(df)):
		
		if tag in df['Tag'][i]:
			
			newdf.loc[c,'Title']=df.loc[i,'Title']
			newdf.loc[c,'Link']=df.loc[i,'Link']
			newdf.loc[c,'Text']=df.loc[i,'Text']
			newdf.loc[c,'Tag']=df.loc[i,'Tag']
			c=c+1
	newdf.to_csv('articles2.csv',index= None, header = 	True)	
		
	
def title_keyword(keyword):

	
	title= df.Title.values # transferring all title into numpy array
	link = df.Link.values
	links=[]
	dataf= pd.DataFrame(columns=['Title','Link','Text','Tag'])
	def remove_punc_sw(wtokens):
		a=[]
		
		for w in wtokens:                # checking every word to eliminate punctuation and stop words
			if w not in punctuations:
				if w not in stop_words:
					a.append(w)
		return a
		
	def content_tokenize(text):
		wtoken= word_tokenize(text)     #converts the sentence into tokens
		wtoken= remove_punc_sw(wtoken)  #removing punctutation and stopwords
		return wtoken
		
	def convert_lower_case(text):
		return text.lower()	
	
	def find_links(keywords):
		
		i=int(1)
		for t in title:                       # checking if the entered keyword is a subset in the titles present
			t1= convert_lower_case(t)
			a=[]
			a=content_tokenize(t1)			
				
			if set(keywords).issubset(set(a)):
				index= np.where(title==t)

				l=str(link[index])
				dataf.loc[i,'Sno']=i
				dataf.loc[i,'Title']=t
				dataf.loc[i,'Link']=l[2:-2]
				dataf.loc[i,'Text']=df.loc[i,'Text']
				dataf.loc[i,'Tag']=df.loc[i,'Tag']
			   
				i=i+1
				links.append(link[index])
				
				
				

	
	keyword= convert_lower_case(keyword)
	keywords= content_tokenize(keyword)

	find_links(keywords)
	dataf.to_csv(r'articles2.csv', index = None, header=True)






