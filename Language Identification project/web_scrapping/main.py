import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com"
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)
title = soup.title

# # Beautiful Soup
# print(type(soup))
# # tags
# print(type(title))
# # Navigable String
# print(type(title.string))
# comment

# markup = '<p><!-- this is comment --></p>'
# soup2 = BeautifulSoup(markup)
# print(soup2.p.string)
# exit()

# get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)



# Get first element
# print(soup.find('p'))

# get class of any element
# print(soup.find('p')['class'])

# get all the elements with class text-gray-500
# print(soup.find_all('p', class_='text-gray-500'))

# get the tag from tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# get all the anchor tags from the page
anchor_tag = soup.find_all('a')
all_links = set()
# get all the links on the page
for link in anchor_tag:
    if link.get('href') != '#':
        link_Text = "https://codewithharry.com" + link.get('href')
        all_links.add(link_Text)
        print(link_Text)

__next = soup.find(id='__next')
print(__next.childern)
# print(anchor_tag)