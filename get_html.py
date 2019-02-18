import urllib2
site=raw_input('Enter Your Site And Dont Forget http >> ')
rep=urllib2.urlopen(site)
print (rep.read())
