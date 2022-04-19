import os
import webbrowser
import sys
os.system("cd .. /")
sys.path.insert(1, "/WebCrawler/")
from database import *

search = input("Search Browser: ")
ori_search = search

# Remove characters
search = search.replace("the", "")
search = search.replace("", "-")

# Split strings into words
search = search.split("-")

print("Results for " + str(ori_search))
for word in search:
  if not word in siteindex.keys():
    print("Error, word " + word + " doesn't exist.")
  else:
    for url in siteindex[word].keys()
    print(url)

url = input("What site would you like to visit (Make sure to answer with the exact URL)? \n")

page = "file:///"+os.getcwd()+"/" + url + ".html"
webbrowser.open_new_tab(filename)
