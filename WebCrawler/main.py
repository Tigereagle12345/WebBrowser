import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Selenium Setup
driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_url = "https://www.google.com/"
driver.get(chrome_url)

# Functions
def robots():
  url = driver.current_url
  robots_url = str(url + "robots.txt")
  
  driver.get(robots_url)
  source = driver.page_source
  if "User-agent:" in source:
    page_text = driver.find_element_by_xpath("/html/body").text
    print(page_text)
  