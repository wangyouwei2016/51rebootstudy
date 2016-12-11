import urllib
import urllib2
ip = '211.137.19.234'
url = "http://freeapi.ipip.net/{}".format(ip)
print url
req = urllib2.Request(url)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res