from bs4 import BeautifulSoup as bs
import requests

DOMAIN = 'http://bilgisayarhane.net/'
URL = 'http://bilgisayarhane.net/python-derslerini-pdf-olarak-indir/'
FILETYPE = '.pdf'

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    if FILETYPE in file_link:
        file_name = file_link.split('/')[-1]
        print(file_name)
        with open(file_name, 'wb') as file:
            file.write(requests.get(file_link).content)
