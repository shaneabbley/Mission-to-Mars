#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')


# In[5]:


# slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[14]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[16]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# Optional delay for loading the page
#browser.is_element_present_by_css('div.list_text', wait_time=1)

hemisphere_image_urls = []

for x in range(4):
    hemispheres = {}
    html = browser.html
    hemis_soup = soup(html, 'html.parser')
    # Find and click on each hemisphere
    browser.links.find_by_partial_text('Enhanced')[x].click()
    #hemis_soup = soup(html, 'html.parser')
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    #browser.links.find_by_partial_text('Open').click()
    #hemis_soup = soup(html, 'html.parser')
    #browser.is_element_present_by_css('div.list_text', wait_time=1)
    html = browser.html
    hemis_soup = soup(html, 'html.parser')
    hemis_soup
    hemisphere_title = hemis_soup.find('h2', class_='title').get_text()
    hemispheres['Title']=hemisphere_title
    img_url_rel = hemis_soup.find('img', class_='wide-image').get('src')
    img_url_rel
    img_url = f'https://https://astrogeology.usgs.gov{img_url_rel}'
    hemispheres['URL']=img_url
    browser.back()
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    hemisphere_image_urls.append(hemispheres)

    


# In[17]:


hemisphere_image_urls


# In[ ]:





# In[18]:


# 5. Quit the browser
browser.quit()


# In[ ]:




