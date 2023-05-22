#import time
import csv
#from selenium import webdriver
from bs4 import BeautifulSoup
import requests
url = requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
#br = webdriver.Chrome("C:/Users/sanya/OneDrive/DesktopCoding/PRO-127/chromedriver.exe")
#br.get(url)
#time.sleep(10)

def scraping():
    header=["Name","Distance","Mass","Radius"]
    star =[]

    for i in range(0,5):
        data = BeautifulSoup(url.content,"html.parser")
        for ultag in data.find_all("tr",attrs={"class","headerSort"}):
            litag=ultag.find_all("th")
            tempdata=[]
            for i,val in enumerate(litag):
                if i == 0:
                    tempdata.append(val.find_all("a")[0].contents[0])
                else:
                    try:
                        tempdata.append(val.contents[0])    
                    except:
                        tempdata.append("")
            star.append(tempdata)
            print(star)
        #page.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()    
        
    with open("scrapingdata.csv","w") as f:
        csvdata = csv.writer(f)
        csvdata.writerow(header)
        csvdata.writerows(star)
scraping()                                



