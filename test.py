#!/usr/bin/python

import pycurl
import os
import io
from io import BytesIO

username=input('Username: ')
password=input('password: ')

#while(True):
#    url = input('Scan QR Code: ')
#    # CURL Request to url
#    print(url)

storeurl = "https://store.hollywoodkidsacademy.com/"
e = io.BytesIO()

c = pycurl.Curl()
c.setopt(pycurl.WRITEFUNCTION, e.write)
c.setopt(c.URL, storeurl + "wp-login.php")
c.setopt(pycurl.SSL_VERIFYPEER, False)
c.setopt(pycurl.USERAGENT, 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
c.setopt(pycurl.TIMEOUT, 60)
c.setopt(pycurl.FOLLOWLOCATION, 1)
#c.setopt(pycurl.RETURNTRANSFER, 1)
cookiefile = 'temp'
c.setopt(pycurl.COOKIEJAR, cookiefile)
c.setopt(pycurl.COOKIEFILE, cookiefile)
c.setopt(pycurl.REFERER, storeurl + "wp-admin/")
postdata= "log=" + username + "&pwd=" + password + "&wp-submit=Log%20In&redirect_to=" + storeurl + "wp-admin/?testcookie=1";
c.setopt(pycurl.POSTFIELDS, postdata)
c.setopt(pycurl.POST, 1)
c.perform()
c.close()


body = e.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
print(body)
