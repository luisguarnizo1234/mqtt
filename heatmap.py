import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


def graficar(n1, n2, n3, n4):

	print "metodo graficar"
	y1 = str(n1)
	y2 = str(n2)
	y3 = str(n3)
	y4 = str(n4)

	tama1 = len(y1)
	tama2 = len(y2)
	tama3 = len(y3)
	tama4 = len(y4)
	y1=y1[1:(tama1-2)]
	y2=y2[1:(tama2-2)]
	y3=y3[1:(tama3-2)]
	y4=y4[1:(tama4-2)]
	
	m1 = float(y1)
	m2 = float(y2)
	m3 = float(y3)
	m4 = float(y4)
	print"float:"
	print(m1)
	print(m2)
	print(m3)
	print(m4)

	print "convirtio graficar" 
	 
	vector = np.array([[m1, m2],[m3, m4]])
	print(vector)
	df = pd.DataFrame(vector, columns= ["a", "b"])
	print(df)
	plt.figure('1')
	sns.heatmap(df, cmap="YlGnBu")
	plt.show()
	
	
	
