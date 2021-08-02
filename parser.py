from time import sleep
#-*- coding: cp949 -*-
#-*- coding: utf-8 -*-


from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20210722.xml")


soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("region: ", location.select_one("city").string)
    print("weather:  ", location.select_one("wf").string)
    print("high temperator: ", location.select_one("tmn").string)
    print("min temperator: ", location.select_one("tmx").string)
    print()
