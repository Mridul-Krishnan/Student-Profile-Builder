import numpy 
import pandas as pd
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import webbrowser
d=pd.read_csv('tags1.csv')
def tupdate(link):
	webbrowser.open(link)
	
	df=pd.read_csv('df.csv')
	count = CountVectorizer(stop_words='english')

	df = df.reset_index()
	indices = pd.Series(df.index, index=df['link'])
	idx = indices[link]
	if type(d['soup'][0])==numpy.float64:
		d['soup'][0]=''
	d['soup'][0]=d['soup'][0]+df['soup'][idx]

	count_matrix = count.fit_transform(df['soup'])
	count_matrix1 = count.transform(d['soup'])

	cosine_sim2 = cosine_similarity(count_matrix1, count_matrix)
	def get_recommendations(link, cosine_sim2=cosine_sim2):
		idx = indices[link]
		sim_scores = list(enumerate(cosine_sim2[0]))
		sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
		sim_scores = sim_scores[1:51]
		video_indices = [i[0] for i in sim_scores]
	    #print(sim_scores)
		return df.iloc[video_indices].sort_values(by=['rating'], ascending=False)


	z=get_recommendations(link,cosine_sim2)

	z.to_csv('dfr.csv',index=False)
	d.to_csv('tags1.csv',index=False)



