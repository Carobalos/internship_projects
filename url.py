#!/usr/bin/python


#start button

        		   
        
    def initUI(self):
      
        self.parent.title("Start button")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Start",
            command=self.start)
        quitButton.place(x=50, y=50)


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop(
        
#download button

    class button(object):
        	"""docstring for button"""
        	def __init__(self, arg):
        		super(button, self).__init__()
        		self.arg = arg


      def initUI(self):
      
        self.parent.title("Download button")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        downloadButton = Button(self, text="Download",
            command=self.download)
        downloadButton.place(x=50, y=50)



##delete button


     class button(object):
        	"""docstring for button"""
        	def __init__(self, arg):
        		super(button, self).__init__()
        		self.arg = arg
        		   
    def initUI(self):
      
        self.parent.title("Delete button")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        deleteButton = Button(self, text="Delete",
            command=self.delete)




	