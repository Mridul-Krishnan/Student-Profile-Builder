import pandas as pd

def tagreset():
	dft=pd.read_csv('TAGS3.csv')
	d_tag={dft.iloc[i][0]:dft.iloc[i][1] for i in range(len(dft))}
	for (k,v) in d_tag.items():
		d_tag[k]=0


	dft=pd.DataFrame([(k,v) for (k,v) in d_tag.items()])
	dft.to_csv('TAGS3.csv',index=False)
tagreset()
