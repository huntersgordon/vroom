#! /usr/bin/python2.7
from craigslist import CraigslistForSale
import os
import time
import math
#import StringIO

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


search = CraigslistForSale(site='losangeles',area='sfv', category='cta',
                         filters={'has_image': True,'query':'\"1997\" porsche','max_price': 200000, 'min_price':1000, 'posted_today':False})

#stri = "osascript -e \'tell application \"Safari\"\n\t tell window 1\n\t \t set current tab to (make new tab with properties {URL:\""
strj = "\"})\n\t end tell \nend tell\'"

hour = int(time.strftime('%H', time.localtime(time.time())))
day = int(time.strftime('%d', time.localtime(time.time())))
when = ""


#os.system(stri)
#os.system("osascript -e \'tell application \"Safari\" to activate\'")

i = 1

with open('porsche.html', 'r') as myfile:
    data=myfile.read().replace('\n', '')

#took out geotagged=True
for result in search.get_results(sort_by='newest'): #,limit = 50
    if (data.find(result['name'].encode('utf-8')) == -1):
        with open("porsche.html", "a") as myfile:
            myfile.write("<a href = \"" + result['url'].encode('utf-8') + "\">" + str(i) + ": " + result['price'].encode('utf-8') + " " + result['name'].encode('utf-8') + " " + result['url'].encode('utf-8') + "\n" + "</a><br><br>")
        print "new listing " + result['name'] + " added."
    if day - int(result['datetime'][8:10]) == 0:
	    when = str(hour - int(result['datetime'][11:13]))
    else:
        when = str(hour+(24*abs(day - int(result['datetime'][8:10]))) - int(result['datetime'][11:13]))
    print str(i) + ": " + result['price'] + ' ' + result['name'][:30] + ": " + result['url']
    #os.system(str(stri + result['url'] + strj))
    #notify(title    = str(result['name'][:30].encode('utf-8')),
    #subtitle = str(result['price'] + ", posted: " + when + " hours ago"),
    #message  = str(result['url']))
    i+=1
