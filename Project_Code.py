import requests
from bs4 import BeautifulSoup 
from random import choice
Url1 = "http://quotes.toscrape.com/"


def scrap_quotes():
 url2 = "/page/1/"
 all_quotes = []
 while url2:
  res = requests.get(f"{Url1}{url2}")
  print(f"Scraping {Url1}{url2}")
  soup = BeautifulSoup(res.text, "html.parser")
  quotes = soup.find_all(class_="quote")
  
  for quote in quotes:
   all_quotes.append({"text": quote.find(class_="text").get_text()})
  next_button = soup.find(class_="next")
  url2 = next_button.find("a")["href"] if next_button else None
 return all_quotes

def start_game(scrapQuotes):
 quote = choice(scrapQuotes)
 Text_data = quote['text']
 print(Text_data)
scrapQuotes = scrap_quotes()
start_game(scrapQuotes)