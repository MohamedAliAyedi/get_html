import urllib2
site=raw_input('Enter Your Site >> ')
rep=urllib2.urlopen(site)
print (rep.read())
