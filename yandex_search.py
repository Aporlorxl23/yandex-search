#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 23:05:01 2020
@author: A.Baran Ertemir & Eren Şimşek <Aporlorxl23>
"""
import requests, argparse
from bs4 import BeautifulSoup

def main():
    header = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    for page in range(0,depth):
        search = main_Url+"&p="+str(page)
        response = requests.get(search,headers=header)
        html = response.content
        soup = BeautifulSoup(html,"html.parser")

        for i in soup.find("div",{"class":"content__left"}).find_all("a"):
            if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
                if i.get("href") not in alldata:
                    alldata.append(i.get("href"))

    if output != "":
        try:
            file = open(output,"a")
            for i in alldata:
                print(i)
                file.write(i+"\n")
        except:
            for i in alldata:
                print(i)
                print("Output Save Error")
        finally:
            file.close()
    else:
        for i in alldata:
            print(i)


if __name__ == "__main__":
    Parser = argparse.ArgumentParser(description="A.Baran Ertemir & Eren Şimşek <Aporlorxl23> Yandex Search Script")
    Parser.add_argument("-k","--keyword",required=True,type=str,help="Search Keyword")
    Parser.add_argument("-d","--depth",required=False,default=5,type=int,help="Depth Number")
    Parser.add_argument("-o","--output",required=False,default="",type=str,help="Output File")
    Args = Parser.parse_args()
    keyword = Args.keyword
    main_Url = "https://yandex.com.tr/search/?lr=101657&text="+keyword
    depth= Args.depth
    output = Args.output
    alldata = []
    main()
