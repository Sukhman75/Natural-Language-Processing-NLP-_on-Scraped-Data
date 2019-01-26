import requests
from bs4 import BeautifulSoup 
from random import choice
Url1 = "http://quotes.toscrape.com/"



Url2 = "/page/1/"
all_quotes = []
while Url2:
  res = requests.get(f"{Url1}{Url2}")
  print(f"Scraping {Url1}{Url2}",'\n')
  soup = BeautifulSoup(res.text, "html.parser")
  quotes = soup.find_all(class_="quote")
  

  for quote in quotes:
   all_quotes.append({'text':quote.find(class_="text").get_text()})
  next_button = soup.find(class_="next")
  Url2 = next_button.find("a")["href"] if next_button else None


quote = choice(all_quotes)
Text_data = quote['text']
print("The data for text mining:",'\n',Text_data,'\n')

import nltk
from nltk.tokenize import RegexpTokenizer

token_Data = RegexpTokenizer(r'\w+')
filtered_data =  token_Data.tokenize(Text_data)

from nltk.corpus import stopwords
# nltk.download('punkt')


stop_words = set(stopwords.words('english'))
#print(stop_words)

print("List if Words without punctuation:",'\n',filtered_data)
words = []
for word in filtered_data:
  if word.lower() not in stop_words:
    words.append(word)
print("List if words without stopwords:",'\n',words)    
POS = nltk.pos_tag(words)
print("Parts of speech:",'\n',POS)


