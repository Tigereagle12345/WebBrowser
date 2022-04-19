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
  print

page = "file:///"+os.getcwd()+"/" + url + ".html"
webbrowser.open_new_tab(filename)
