#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:50:51 2019

@author: rodolfopardo
"""

#import sys
#!{sys.executable} -m pip install bs4 requests pandas lxml html5lib

import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

url = "https://www.clarin.com/"
river = requests.get(url).content
river

soup = BeautifulSoup(river, 'html')
soup
tabla = soup.select('.mt h2')
river = []
count = 0
for element in tabla:
    if count < 1:
        river.append(element.text)
        count +=1

print(river)


url1 = "https://www.clarin.com/deportes/futbol/river-gimnasia-mendoza-copa-argentina-horario-tv-verlo-vivo_0_zTuw4WU_E.html"

river_1 = requests.get(url1).content

soup1 = BeautifulSoup(river_1, "html")

texto = soup1.select('.body-nota p')
texto

river2 = []

for element in texto:
    print(element.text)
    river2.append(element.text)
    time.sleep(7)

