class button(object):
   	"""docstring for button"""
	def __init__(self, arg):
		super(button, self).__init__()
		self.arg = arg



for url in urls:
    rssObject = urllib2.urlopen(url)
    data = rssObject.read()
    with open(self.SERVER_PATH+"\\feeds\\"+str(feedID)+str(extension), "w") as requiredData:
        requiredData.write(str(data))
    requiredData.close()


		