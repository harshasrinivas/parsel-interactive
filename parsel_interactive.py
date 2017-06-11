import webbrowser
import os

class interactive(object):
	def __init__(self):
		pass

	def show(self, selector_list, htmlsample):
	    x = selector_list.extract()
	    y = ['<div style="background-color: yellow; font-weight:bold;">' + i + '</div>' for i in x]

	    for i, j in zip(x, y):
	        htmlsample = htmlsample.replace(i, j)

	    newpath = os.path.realpath('./modified.html')
	    
	    with open(newpath, 'w') as f:
	        f.write(htmlsample)
	    
	    webbrowser.open('file://' + newpath)
