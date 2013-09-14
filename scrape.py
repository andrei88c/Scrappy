import urllib2, datetime
from bs4 import BeautifulSoup


soup  = BeautifulSoup(urllib2.urlopen("http://www.vibefm.ro/live/").read())
print datetime.datetime.utcnow()
print soup('a',{'title': 'Asculta live'})[0].string

soup  = BeautifulSoup(urllib2.urlopen("http://www.radiozu.ro/").read())
print datetime.datetime.utcnow()
print  soup('div',{'class': 'piesa-live'})[0].get_text(' - ',strip=True)

soup  = BeautifulSoup(urllib2.urlopen("http://www.kissfm.ro/").read())
print datetime.datetime.utcnow()
print  soup('h6',{})[0].get_text(' - ',strip=True)