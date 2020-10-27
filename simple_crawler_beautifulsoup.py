from bs4 import BeautifulSoup
import requests
import sys



def resp(url):
    res=requests.get(url)
    if res.status_code == 200:
        return res.content
    sys.exit("invalid response recieved !!!")   



# soup = BeautifulSoup(res.text, 'lxml')
# # for x in soup.find_all('div'):
# #     print(x)

 
# article = soup.find('article')

# summary = article.find('div', class_='entry-content').p.text
# print(summary)

#open writable csv
#make soup obj
#iterate and extract data
#add data to csv file
#close file writing
url = "http://coreyms.com"
html = resp(url)
soup = BeautifulSoup(html, 'lxml')


print(soup.prettify)