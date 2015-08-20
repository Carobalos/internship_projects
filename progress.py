import os

import time

import urllib

#import xbmc, xbmcgui

url = raw_input('Enter the url of the file to download: ') 
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("My Script","Downloading File",url)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
 
