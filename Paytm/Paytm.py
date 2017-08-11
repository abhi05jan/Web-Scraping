import urllib.request as urllib
import lxml
import time
from bs4 import BeautifulSoup as b
import csv


def enterProduct(name):
	splitted = name.split()
	mainProduct = '+'.join(splitted)
	return mainProduct
def totalPages(pages):
	if pages < 200:
		return pages
def startCrawl():
	search_string = enterProduct(name)
	r = totalPages(pages)
	with open(str(filename)+'.csv','w',encoding='utf-8') as csvfile:
		fieldnames = ['Title','Price']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for i in range(1,r+1):
			print("******************title& price"+str(i)+"***********")
			try:
				url="https://paytm.com/shop/search?q="+str(search_string)+"&from=organic&child_site_id=1&site_id=1"
				html=b(urllib.urlopen(url).read(),"lxml")
				titles = html.findAll('div',{'class' :'_2apC'})

				prices = html.findAll('span',{'class' :'_1kMS'})
				for(i,j) in zip(titles,prices):
					title,price = i.text,j.text[1:]
					writer.writerow({'Title':title,'Price':price})
			except:
				pass
            
def info():
    print("""
              

                
                         1.Enter the product name
                         2.Enter how many pages to scrape 
    """)
info()

try:
	name = input("enter product")
	pages = int(input("enter pages"))
	filename = input("enter name")
	enterProduct(name)
	totalPages(pages)
	startCrawl()
except:
	print("please enter detail properly")