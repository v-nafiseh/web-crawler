## Simple web crawler project implemented with python 

#### steps for implementing crawler with BeautifulSoup:
- 1.installing Requests and BeautifulSoup 
- 2.importing above libaries
- 3.initializing target web url
- 4.http request to web url through get method of requests library
- 5.making a beautifulsoup object and passing our web url and parser(lxml or any other parser) to it
- 6.finding all image tags with find_all('img') command
- 7.getting the src attribute of each img tag
- 8.looping through each url found in above sections and writing them in a csv file.

#### steps for implementing crawler with scrapy framework
- installing scrapy
- starting a scrapy project with scrapy startproject 'name' command
- entering the project directory
- making our spider .py file in spiders directory
- importing scrapy 
- creating scraper class which inherits scrapy.spider class
- defining spider name and start urls
- defining parse method
- extracting target dada from webpage with css and xpath selectors 
- adding extracted data to item object of Items class
- writing the data to specified csv file
