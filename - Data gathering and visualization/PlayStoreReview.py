from google_play_scraper import Sort, reviews_all
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Review Word Cloud')
parser.add_argument('-a', '--app', action='store', help='enter app', default=None)
parsed = parser.parse_args()

app = parsed.app

result_5 = reviews_all(
	app,
	sleep_milliseconds=0,
	lang='en', 
	country='us', 
	sort=Sort.MOST_RELEVANT, 
	filter_score_with=5)

result_1 = reviews_all(
	app,
	sleep_milliseconds=0, 
	lang='en',
	country='us',
	sort=Sort.MOST_RELEVANT, 
	filter_score_with=1)	
    
def createWordCloud(data):
	comment_words = ''
	stopwords = set(STOPWORDS)
	  
	# iterate through the csv file
	for val in data:
	      
	    # typecaste each val to string
		val = str(val)
	  
	    # split the value
		tokens = val.split()
	      
	    # Converts each token into lowercase
		for i in range(len(tokens)):
			tokens[i] = tokens[i].lower()
	      
		comment_words += " ".join(tokens)+" "
	  
	wordcloud = WordCloud(width = 800, height = 800,
		        background_color ='white',
		        stopwords = stopwords,
		        min_font_size = 10).generate(comment_words)
	  
	# plot the WordCloud image                       
	plt.figure(figsize = (8, 8), facecolor = None)
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.tight_layout(pad = 0)
	  
	plt.show()
	
createWordCloud(result_5)
createWordCloud(result_1)
