from bs4 import BeautifulSoup
import requests
import time


class News:

    
    _class1 = "JtKRv"
    
    def get_news(self,key):

        response = requests.get(f'https://news.google.com/search?q={key}&hl=en-IN&gl=IN&ceid=IN%3Aen')
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)
        s =soup.find(class_ = self._class1).text.strip()
        #start = s.find("More") + len("More")
        #s = s[start:]
        print(s)
        return s

    def g_news(self):
        response = requests.get('https://news.google.com/search?q=world%20news&hl=en-US&gl=US&ceid=US%3Aen')
        soup = BeautifulSoup(response.text, 'html.parser')
        s = soup.find_all(class_ =self._class1)
        #print(s[3].text.strip())
        return s
p = News()
#p.get_news('Indigo')
p.g_news()
