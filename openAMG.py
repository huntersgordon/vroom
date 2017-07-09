#! /usr/bin/python2.7
from craigslist import CraigslistForSale
import os
import time

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


search = CraigslistForSale(site='losangeles',area='sfv', category='cta',
                         filters={'has_image': True,'query':'AMG','max_price': 9000, 'min_price':1000, 'posted_today':True})

#stri = "osascript -e \'tell application \"Safari\"\n\t tell window 1\n\t \t set current tab to (make new tab with properties {URL:\""
strj = "\"})\n\t end tell \nend tell\'"

hour = int(time.strftime('%H', time.localtime(time.time())))
day = int(time.strftime('%d', time.localtime(time.time())))
when = ""


#os.system(stri)
#os.system("osascript -e \'tell application \"Safari\" to activate\'")

i = 1
#took out geotagged=True
for result in search.get_results(sort_by='newest', limit = 7):
    if day - int(result['datetime'][8:10]) == 0:
	    when = str(hour - int(result['datetime'][11:13]))
    else:
        when = str(hour+24 - int(result['datetime'][11:13]))
    print str(i) + ": " + result['price'] + ' ' + result['name'][:30] + ": " + result['url']
    #os.system(str(stri + result['url'] + strj))
    notify(title    = str(result['name'][:30]),
    subtitle = str(result['price'] + ", posted: " + when + " hours ago"),
    message  = str(result['url']))
    i+=1
