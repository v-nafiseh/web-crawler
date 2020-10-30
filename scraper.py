import csv
import re
import requests
import sys


from bs4 import BeautifulSoup as bs


web = "https://bagheketab.com/"

def resp(web):
    response = requests.get(web)
    if response.status_code ==200:
        return response.content
    sys.exit("invalid response recieved !!!!")    


soup = bs(resp(web), "lxml")  #passing lxml parser to parse out html content and making beautifulsoup object to work with



csv_file = open('image_links','w')
csv_writer = csv.writer(csv_file)



image_tags = soup.find_all("img")   

    

urls = [img["src"] for img in image_tags]   

for url in urls:
    if not  str(url).startswith(("http","https")):
        url = web + url
    csv_writer.writerow([url])  #writing each image url in rowx

csv_file.close()



