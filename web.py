import pprint
import requests 
import bs4

KEYWORDS = ['РґРёР·Р°Р№РЅ', 'С„РѕС‚Рѕ', 'web', 'python']

response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')

article_list = soup.findAll('article', class_='tm-articles-list__item')

for article in article_list:
    link = f"https://habr.com{article.find('a', class_='tm-title__link')['href']}" 
    title_date = f"https://habr.com{article.find('a', class_='tm-articles-list__item')['title']}" 
    title_name = f"https://habr.com{article.find('a', class_='tm-title__link')['span']}" 
print(title_date, '-', title_name, '-', link)