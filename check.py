import os
import urllib
with open('/Users/Hunter 1/Desktop/vroom/cars.html', 'r') as myfile:
    data=myfile.read().replace('\n', '')
links = []
while (data.find("href") != -1):
    if data[90:190].find("p style = \"c") == -1:
        links.append(data[data.find("href") + 8 : data[data.find("href") + 8:].find("\"") + data.find("href") + 8])
    data = data[data[data.find("href") + 8:].find("\"") + data.find("href") + 9:]

s = ""
count = 0
with open('/Users/Hunter 1/Desktop/vroom/cars.html', 'r') as myfile:
    data=myfile.read().replace('\n', '')
for i in links:
    s = urllib.urlopen(i).read()
    if ((s.find("This posting has") != -1) or (s.find("Post not found.") != -1)):
        count+=1
        print(i + " is no longer available.")
        ispot = data.find(i)
        modified = data[0:ispot-10] + "p style = \"color: red\" " + data[ispot-9:]
        with open("cars.html", "w") as myfile:
            myfile.write(modified)
        with open('/Users/Hunter 1/Desktop/vroom/cars.html', 'r') as myfile:
            data=myfile.read().replace('\n', '')
    else:
        print(i + " is a good link.")

print (str(count) +  " links removed.")
