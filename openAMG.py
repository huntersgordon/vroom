#! /usr/bin/python2.7
from craigslist import CraigslistForSale
import os
import time
from time import gmtime, strftime
import math
import sys


def wait():
    m.getch()

areaa = 'sfv'

if (not len(sys.argv) < 2 and ((sys.argv[1]) == "clear")):
    with open('cars.html', 'w') as myfile:
        myfile.write("<p style = \"text-align: center; font-size: 40; \"> craigslist for cheap AMG Mercedes Benzes in the los angeles san fernando valley</p>")
        print "cars.html cleared"
    exit()

if (not len(sys.argv) < 2 and ((sys.argv[1]) == "check")):
    os.system("python2.7 check.py")
    exit()

if (len(sys.argv) > 1):
    print("usage: python2.7 openAMG.py [clear/check]")
    exit()



def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


search = CraigslistForSale(site='losangeles',area=areaa, category='cta',
                         filters={'has_image': True,'query':'AMG','max_price': 9000, 'min_price':2000, 'posted_today':False})

#stri = "osascript -e \'tell application \"Safari\"\n\t tell window 1\n\t \t set current tab to (make new tab with properties {URL:\""
strj = "\"})\n\t end tell \nend tell\'"

#hour = int(time.strftime('%H', time.localtime(time.time())))
#day = int(time.strftime('%d', time.localtime(time.time())))
#when = ""


#os.system(stri)
#os.system("osascript -e \'tell application \"Safari\" to activate\'")

i = 1
added = 0
sofar = ""

with open('cars.html', 'r') as myfile:
    data=myfile.read().replace('\n', '')

#took out geotagged=True
for result in search.get_results(sort_by='price_asc'): #,limit = 50
    if ((data.find(result['name'].encode('utf-8')) == -1) and (sofar.find(result['name'].lower()) == -1)):
        with open("cars.html", "a") as myfile: #append the listing
            myfile.write("<a href = \"" + result['url'].encode('utf-8') + "\">" + str(i) + ": " + result['price'].encode('utf-8') + " " + result['name'].encode('utf-8') + " " + result['url'].encode('utf-8') + "\n" + "</a><br><br>")
            added = added + 1
            sofar += result['name'].lower()
            i += 1
        print "new listing \"" + result['name'] + "\" added."
    #if day - int(result['datetime'][8:10]) == 0:
	#    when = str(hour - int(result['datetime'][11:13]))
    #else:
        #when = str(hour+(24*abs(day - int(result['datetime'][8:10]))) - int(result['datetime'][11:13]))
    #print str(i) + ": " + result['price'] + ' ' + result['name'][:30] + ": " + result['url']
    #os.system(str(stri + result['url'] + strj))
    #notify(title    = str(result['name'][:30].encode('utf-8')),
    #subtitle = str(result['price'] + ", posted: " + when + " hours ago"),
    #message  = str(result['url']))
    #i += 1


if (added == 0):
    print "no listings added."

else:
    with open("cars.html", "a") as myfile:
        myfile.write("<p style = \"font-size: 30px;\">--------------------------------------------pulled on: " + strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + " </p>")
    print str(added) + " listing(s) added."

raw_input('press enter...')
