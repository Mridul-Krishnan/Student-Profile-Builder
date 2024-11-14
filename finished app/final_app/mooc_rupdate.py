import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances

def mooc_update():
	dfc=pd.read_csv('final-moooc-list.csv')
	dft=pd.read_csv('TAGS3.csv')
	d_tag={dft.iloc[i][0]:dft.iloc[i][1] for i in range(len(dft))}
	d_course={i:list(dfc.iloc[i]) for i in range(len(dfc)) }
	cscore={i:0 for i in range(len(dfc))}
	for (i,v) in cscore.items():
		cvec=[]
		for (k,v) in d_tag.items():
			if k in eval(d_course[i][6]):
				cvec.append(int(d_tag[k]))
			else:
				cvec.append(0)
		pvec=[int(w) for (j,w) in d_tag.items()]
		cscore[i]=pairwise_distances([cvec,pvec],metric='euclidean')[0][1]

	cscore=sorted(cscore.items(),key=lambda kv:kv[1])

	f_course=[('\n'.join([d_course[i[0]][0],d_course[i[0]][2],d_course[i[0]][4],d_course[i[0]][5]]),d_course[i[0]][1]) for i in cscore]
	fdf=pd.DataFrame(f_course)

	fdf.to_csv('recommend_course.csv',index=False)
	print('new course list created')
	dft=pd.DataFrame([(k,v) for (k,v) in d_tag.items()])
	dft.to_csv('TAGS3.csv',index=False)
