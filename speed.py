import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

web = requests.get("https://www.speedtest.net/global-index")

soup = BeautifulSoup(web.text, "html.parser")

table = soup.find_all('table')[2]

tableValues = []
for x in table.find_all('tr'):
    td_tags=x.find_all('td')
    td_val = [y.text for y in td_tags]
    tableValues.append(td_val)

df=pd.DataFrame(tableValues)
df.to_excel('tablenew.xlsx', index=False)
df.to_csv('tablenew.csv',index=False)