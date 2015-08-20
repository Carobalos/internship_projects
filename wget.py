#usr/bin/python

import os

import time

import urllib

from progressbar import ProgressBar 

url = raw_input('Enter the url of the file to download: ')

dl_times = int(raw_input('Enter the number of times to download: '))

download_name = str(url.split('/')[-1])   

time_list = []  

progress = ProgressBar()

for i in progress(xrange(0, dl_times)):
	t1 = time.time() 
	urllib.urlretrieve(url, download_name) 
	t2 = time.time() 

	time_taken = t2 - t1 
	#print i+1, '-', 'Time taken for download to complete: {} seconds'.format(time_taken) 
	print i+1, '-', 'Time taken for download to complete: %d seconds' % time_taken
	
	os.system('rm -f '+str(download_name))

print 'Successfully downloaded: %d times' % dl_times
	
#if progress == 100
	#print i+1, '-' 'Sucessfully downloaded: %d times' % dl_times
#else{
	#print i+1, '-' 'Successfully downloaded: %s out of %d' %  (dl_times, dl_times)
#}

time_list.append(time_taken) 

average_time = sum(time_list) / len(time_list) 

print 'The average download time is {}'.format(average_time) 
#print 'The average download time is %d seconds' %average_time # Print the average time/ downloaad

