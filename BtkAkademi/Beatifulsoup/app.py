import requests
from bs4 import BeautifulSoup

url = "https://www.itopya.com/notebook_k14"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
list = soup.find_all("div", {"class":"product-body"},limit=1)
price = soup.find_all("div",{"class":"price"},limit=1)
inStock = soup.find_all("div",{"class":"productStokBody"},limit=1)


for div in list:
    name = div.a.text.strip()
    link = div.a.get("href")
    print(name)
    
for div in price:
    price = div.strong.text.strip()
    print(price)
    
for div in inStock:
    inStock = div.strong.text.strip()
    print(inStock)

