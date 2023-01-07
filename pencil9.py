# coding: utf-8

# In[0]:


from selenium import webdriver
from bs4 import BeautifulSoup
import os

# In[1]

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
PATH_GD = '⁨usr/bin/chromedriver'

driver = webdriver.Chrome(PATH_GD, options=options)


# In[23]:


website = driver.get('https://www.ilmakiage.co.il/mineral-lip-pencil-4043')


# In[24]:


for _ in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

soup1 = driver.page_source.encode("utf-8")

driver.close()


# In[25]:


soup = BeautifulSoup(soup1, 'lxml')


# In[26]:


if soup.find('span', class_='qtyValidate_color')['style'] == 'display: none;':
    result = "Tut sheli, it'shopping time, your favorite lip pencil is in stock \n https://www.ilmakiage.co.il/mineral-lip-pencil-4043 \n"
    print(result)
elif soup.find('span', class_='qtyValidate_color')['style'] == 'display: block;':
    result = 'Ooops, the stock is empty. Open the app later to check quantity \n'
    print(result)
else:
    result = 'Error'
    print(result)

print(result)
