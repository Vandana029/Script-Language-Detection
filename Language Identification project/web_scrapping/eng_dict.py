import time
# start = time. process_time()
import requests
from bs4 import BeautifulSoup

start = time.time()
words = set()
pronunciation = set()
url = 'https://www.dictionary.com/list/A'
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.find_all('a', class_='e1jj5rmm0'))
# words = soup('li', class='')
mylist = soup.find_all('a', class_='css-aw8l3w')
print(mylist)
for wordlist in mylist:
    for word in wordlist:
        words.add(word.strip())

print(words)
for w in words:
    url2 = 'https://www.gujaratilexicon.com/dictionary/english-to-gujarati-translation/' + w + '/'
    r2 = requests.get(url2)
    htmlContent2 = r2.content
    soup2 = BeautifulSoup(htmlContent2, 'html.parser')
    x = soup2.find_all("p", class_="mx-2")
    print(x, '#')
    if x:
        print(pronunciation.add(x[1].get_text().strip()))

print(pronunciation)
