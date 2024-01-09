import time
# start = time. process_time()
import requests
from bs4 import BeautifulSoup


start = time.time()
pronunciation = []
eng_words = ['a']
# f = open("eng_pron.txt", "w")
for word in eng_words:
    url = 'https://www.gujaratilexicon.com/dictionary/english-to-gujarati-translation/' + word + '/'
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    x = soup.find_all("p", class_="mx-2")
    # print(x)
    pronunciation.append(x[1].get_text().strip())
    # f.write(x[1].get_text().strip())
    # f.write(' ')

# f.close()

print(pronunciation)
# print(time. process_time() - start)
print(f'Time: {time.time() - start}')
# url = 'https://www.gujaratilexicon.com/dictionary/english-to-gujarati-translation/money/'
# r = requests.get(url)
# htmlContent = r.content
# soup = BeautifulSoup(htmlContent, 'html.parser')
# x = soup.find_all("p", class_="mx-2")
# print(x[1].get_text())
