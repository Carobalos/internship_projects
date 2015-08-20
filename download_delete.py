# This library enables you to interact with the operating system's in-built functions
import os

# This library provides time functions
import time

# This one provides utilities to interact with webpages and web resources
import urllib

# Import the progressbar class to display the progress of the download
from progressbar import ProgressBar

# Enter the location of the download you wish to acquire
url = raw_input('Enter the url of the file to download: ')

# Enter the number of times you would like to download the file
dl_times = int(raw_input('Enter the number of times to download: '))

# Create a variable that is the download name. The split function takes the name of the download as the word/ character set after the last backslask
download_name = str(url.split('/')[-1])
 
# Create an empty list of the times taken for each download
time_list = []

# Create an instance of the class
progress = ProgressBar()

# A for loop that downloads the link, takes the time per download and deletes the download after
for i in progress(xrange(0, dl_times)):
	t1 = time.time() # Start time for download
	urllib.urlretrieve(url, download_name) # Retrieval of the download
	t2 = time.time() # End time for download


	time_taken = t2 - t1 # Time taken - difference between start and end times

	time_list.append(time_taken) # add each download time taken to the list/ populate the list
	
	print i+1, '-', 'Time taken for download to complete: {} seconds'.format(time_taken) # Print a list of the times taken for each download

	os.system('rm -f '+str(download_name)) # remove the download

average_time = sum(time_list) / len(time_list) # Calculate the average time per download

print 'The average download time is {} seconds.'.format(average_time) # Print the average time/ download


