#!/usr/bin/python

import pycurl
from StringIO import StringIO
username=input('Username: ')
password=input('password: ')

#while(True):
#    url = input('Scan QR Code: ')
#    # CURL Request to url
#    print(url)

storeurl = "https://store.hollywoodkidsacademy.com/"
buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, storeurl + "wp-login.php")
c.setopt(c.WRITEDATA, buffer)
c.setopt(pycurl.SSL_VERIFYPEER, False)
c.setopt(pycurl.USERAGENT, 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
c.setopt(pycurl.TIMEOUT, 60)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.RETURNTRANSFER, 1)
cookiefile = os.tempnam(_APP_ROOT_PATH+"temp_files","cookie")
c.setopt(pycurl.COOKIEJAR, cookiefile)
c.setopt(pycurl.COOKIEFILE, cookiefile)
c.setopt(pycurl.REFERER, storeurl + "wp-admin/")
postdata= "log=" + username + "&pwd=" + password + "&wp-submit=Log%20In&redirect_to=" + url + "wp-admin/?testcookie=1";
c.setopt(pycurl.POSTFIELDS, postdata)
c.setopt(pycurl.POST, 1)
c.perform()
c.close()


body = buffer.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
print(body)
