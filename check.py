import os
import urllib
with open('/Users/Hunter 1/Desktop/vroom/cars.html', 'r') as myfile:
    data=myfile.read().replace('\n', '')
links = []
while (data.find("href") != -1):
    links.append(data[data.find("href") + 8 : data[data.find("href") + 8:].find("\"") + data.find("href") + 8])
    data = data[data[data.find("href") + 8:].find("\"") + data.find("href") + 9:]

for i in links:
    if (urllib.urlopen(i).read().find("Post not found.") != -1):
        print(i + " is no longer available.")
    else:
        print(i + " is a good link.")
