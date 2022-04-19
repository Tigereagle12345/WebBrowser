import os
import webbrowser
import sys
os.system("cd .. /")
sys.path.insert(1, "/WebCrawler/")
from database import *

page = "file:///"+os.getcwd()+"/" + url + ".html"
webbrowser.open_new_tab(filename)
