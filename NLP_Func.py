def NLP_func(data):
	import pandas as pd 
	import matplotlib.pyplot as plt 
	import nltk
#Step 2 NLP
	from nltk.tokenize import RegexpTokenizer
	token_Data = RegexpTokenizer(r'\w+')
	filtered_data =  token_Data.tokenize(data)

	from nltk.corpus import stopwords
# nltk.download('punkt')


	stop_words = set(stopwords.words('english'))
#print(stop_words)

	print("List if Words without punctuation:",'\n',filtered_data,'\n')
	words = []
	for word in filtered_data:
		if word.lower() not in stop_words:
			words.append(word)
	print("List if words without stopwords:",'\n',words,'\n')    
	POS = nltk.pos_tag(words)
	print("Parts of speech:",'\n',POS)
#Step 3 Frequency Distribution plot
		
	Pos_List = []
	i = 0
	for i in range(len(POS)):
		x = POS[i][1]
		Pos_List.append(x)
	print(Pos_List)
	df = pd.Index(Pos_List)
	#fd = nltk.FreqDist(Pos_List)
	#fd.plot(30,cumulative=False)
	plots = df.value_counts()
	plots.plot(kind='bar')
	plt.show()

		
		

