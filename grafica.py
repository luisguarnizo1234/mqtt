import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

while(True):

	m1 = float(raw_input("x "))
	m2 = float(raw_input("y "))
	m3 = float(raw_input("z "))
	m4 = float(raw_input("w "))
	
	vector = np.array([[m1, m2],[m3, m4]])
	print(vector)
	df = pd.DataFrame(vector, columns= ["a", "b"])
	print(df)
	plt.figure('1')
	sns.heatmap(df, cmap="YlGnBu")
	plt.show()
	#plt.close()
