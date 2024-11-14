import numpy as np
import pandas as pd
import webbrowser
import mooc_rupdate as mr
def tupdate(link):
	dfc=pd.read_csv('final-moooc-list.csv')
	dft=pd.read_csv('TAGS3.csv')
	d_tag={dft.iloc[i][0]:dft.iloc[i][1] for i in range(len(dft))}
	if (isinstance(link,list)):
		print('course tag', link)
		for i in link:
			if i in d_tag.keys():
				print('found')
				d_tag[i]=d_tag[i]+1
		dft=pd.DataFrame([(k,v) for (k,v) in d_tag.items()])
		dft.to_csv('TAGS3.csv',index=False)
		mr.mooc_update()
		return 0
	webbrowser.open(link)
	loc=list(dfc['link']).index(link)
	tags=eval(dfc.iloc[loc][6])
	for i in tags:
		if i in d_tag.keys():
			d_tag[i]=d_tag[i]+1

	dft=pd.DataFrame([(k,v) for (k,v) in d_tag.items()])
	dft.to_csv('TAGS3.csv',index=False)
	mr.mooc_update()
