import urllib2, datetime
from BeautifulSoup import BeautifulSoup


soup  = BeautifulSoup(urllib2.urlopen("http://www.vibefm.ro/live/").read())
print datetime.datetime.utcnow()
print soup('div',{'id': 'live-current-track'})[0].a()[0].string