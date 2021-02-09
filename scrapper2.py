from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')[4]

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.strip() for i in td]
    temp_list.append(row)

headers = ['name','distance','mass','radius']
name = []
distance =[]
mass = []
radius =[]

for i in range(1,len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

print(radius[0])

df2 = pd.DataFrame(list(zip(name,distance,mass,radius)),columns=headers)

df2.to_csv('file2.csv')