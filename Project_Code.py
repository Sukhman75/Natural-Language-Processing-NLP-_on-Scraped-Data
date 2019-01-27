import requests
from bs4 import BeautifulSoup 
from random import choice
#   <<<STEP 1 To Fetch Text Data From The Website>>>

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

#Build A module for making the NLP function universal, that can be used for any type of text(English Only). 

#CALLING THE FUNCTION FROM A MODULE
from NLP_Func import NLP_func

NLP_func(Text_data)


