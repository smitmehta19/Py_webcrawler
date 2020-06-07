from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://anshved.ml/")
#print(html.read()) #.read was added to acces the html code in human readable form
bsobject = BeautifulSoup(html.read(), "html.parser")
print(bsobject.title)#h1 or any other tag can be used..it simply finds  that code and ignores everything else
