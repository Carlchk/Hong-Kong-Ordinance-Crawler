from urllib.request import Request, urlopen
from selenium import webdriver
import json
import os
from datetime import datetime

myjson = "["
print('Enter the language: (eng/chi)')
lang = input();
print('Enter the number of ordinances:')
x = input()
print('Enter the total number of section:')
number = input()
link = "http://www.hklii.org/cgi-bin/sinodisp/"+ lang +"/hk/legis/ord/" + x +"/s'
browser = webdriver.Chrome()
for index in range(1,number):
    url = link + str(index) + ".html"
    browser.get(url)
    title = browser.find_elements_by_tag_name('h2')[0]
    title = title.get_attribute('innerText')
    #print(title)
    content = browser.find_elements_by_tag_name('section')[0]
    content = content.get_attribute('innerText')
    #print(content)
    myjson = myjson + "{" + "'index':" + "'" + str(index) + "'" + "," + "'title':" + "'"+ title + "'"+ "," + "'conetent':" + "'"+ content + "'"+ '},' 
myjson = myjson + "]"
time = datetime.now().strftime('%Y%m%d%H%M%S')
filename = 'export - '+ time + '.json'
f = open(filename, "x")
f.write(myjson)
f.close
