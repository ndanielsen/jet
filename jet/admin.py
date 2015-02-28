#!/usr/local/bin/python
 # -*- coding: utf-8 -*-

"""
Test control structure for cleaning and analysis
"""


from analyze.nlp import NLP

from wrangle.cleaner import PageCleaner

class control(object):
	"""
	Main controller for putting all the subsections together
	"""
	def __init__(self, url):
		self.url = url


	def main(self):
		clean_text = PageCleaner(self.url)
		title, text = clean_text.main()
		processing = NLP(title, text)

		return title, processing.NER()



if __name__ == '__main__':
	#test = control("http://www.liberianobserver.com/weird-news/5-found-unconscious-zeon-town-elwa-community")
	#print test.main()

	nytimes = control("http://www.nytimes.com/2015/03/01/world/europe/russian-authorities-say-fellow-opposition-members-may-have-killed-boris-nemtsov.html")
	print nytimes.main()