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
	
	pass
