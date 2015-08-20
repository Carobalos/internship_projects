import os

import time

import urllib

from progressbar import ProgressBar

url = raw_input('Enter the url of the file to download: ')

dl_times = int(raw_input('How many times would you like to download: '))

download_name= str(url.split ('/')[-1])

time_list = []

progress = ProgressBar ()

#time_taken = 0
for i in progress(xrange(0, dl_times)):
    t1 = time.time()
    try:
        urllib.urlretrieve(url, download_name)  
    	t2 = time.time()
       
    	time_taken = t2 -t1

    	time_list.append (time_taken)  
                 
    	print i+1, '-', 'Time taken to complete download: {} seconds'.format(time_taken)
    except:
        print "Unable to retrieve"

os.system ('rm -f ' +str(download_name))
  
average_time = sum(time_list) / len(time_list)  

print 'The average time to complete download is {} seconds'.format(average_time) 








