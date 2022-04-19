import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from database import *
import json

# Selenium Setup
driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_url = "https://www.google.com/"
driver.get(chrome_url)
search_url = "https://www.google.com/search?q="

# Functions
def robots():
  url = driver.current_url
  robots_url = str(url + "robots.txt")
  
  driver.get(robots_url)
  source = driver.page_source
  if "User-agent:" in source:
    page_text = driver.find_element_by_xpath("/html/body").text
    print(page_text)
 
def storedata(word):
  url = driver.current_url
  source = driver.page_source
  siteindex[word]["url"] = url
  siteindex[word]["url"]["sourcefile"] = str(url) + ".html"
  file = open("../Database/" + str(siteindex[word]["url"]["sourcefile"]), "w")
  file.write(source)
  file.close
  
  file = open("database.py", "w")
  file.close
  file = open("database.py", "w")
  file.write(json.dumps(siteindex))
  file.close
  

# Start
wordlist = open("./Wordlist/wordlist.txt", "r")
for word in wordlist:
  if word != "":
    driver.get(search_url + word)
    links = driver.find_elements_by_tag_name("a")
    for link in links:
      the_url = link.get_attribute(href)
      driver.get(the_url)
      storedata(word)
      
  
