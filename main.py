from bs4 import BeautifulSoup
import requests
import re
import os
import pandas as pd 
import time
os.system('cls')
# enter any product name you want to scrap 

product_name="evega"

url=f"https://www.newegg.com/p/pl?d={product_name}&N=4131"
result=requests.get(url).text
data=BeautifulSoup(result,"html.parser")
# first get total number of pages search results
pages=int(data.find(class_="list-tool-pagination-text").text.strip().split("/")[1])
names=[]
prices=[]
links=[]

for page in range(1,pages+1):
    time.sleep(5)
    url=f"https://www.newegg.com/p/pl?d={product_name}&N=4131&page={page}"
    result=requests.get(url).text
    data=BeautifulSoup(result,"html.parser")
    tbody=data.find(class_="row-body-inner")
    items=tbody.find_all(class_="item-cell")
    for item in items:
        try:
            price=item.find('li',class_="price-current").strong.string
            print(price)
            href=item.find(class_="item-title")
            link=href['href']
            title=href.string
            print(title)
        except:
            pass
        names.append(title)
        prices.append(price)
        links.append(link)
scrap={"Name":names,'Price':prices,"Link":links}

df = pd.DataFrame(scrap)
df.to_excel(f"{product_name}.xlsx")

print("completed data scraping check now")