#!/usr/local/bin/python
 # -*- coding: utf-8 -*-

"""
Control structure for cleaning, analysis and loading content & analysis to json.

Work still needs to be done in order to tailor spiders and wranglers to each website.

More robust feature extraction must be done from the cleaning stage.

Analysis modules need to be richer.

But for a MVP --- this is a good start.


Author:
Nathan Danielsen
nathan.danielsen [at] gmail.com

"""
import json
import os


from analyze.nlp import NLP

from wrangle.cleaner import PageCleaner

class control(object):
	"""
	Main controller for putting all the subsections together
	"""
	def __init__(self, publication, url):
		
		self.publication = publication

		self.url = url

		self.cache = {}
		self.title = None
		self.text = None
		self.story = None
		self.filename = "liberian_media.json"



	def _factory(self):  
		clean_text = PageCleaner(self.url)
		self.title, self.text = clean_text.main()
		processing = NLP(self.title, self.text)

		self.story = {self.title:{"mainbody":self.text, "NER":None, "author":None, "datePubished":None, "url":self.url }}
		

	def factory(self, www): #TEST CASE FUNCTION for direct import 
		clean_text = PageCleaner(www)
		self.title, self.text = clean_text.main()
		processing = NLP(self.title, self.text)

		self.story = {self.title:{"mainbody":self.text, "NER":None, "author":None, "datePubished":None, "url":www }}
		

	def updatecache(self):
		""" 
		Checks to see if the publication and story has been collected. If false, it will add the publication and story to CACHE.  
		"""
		key = self.publication
		cache = self.cache
		if key in cache:
			cache[key].update(self.story)

		else:
			cache[key] = self.story

	def loadjson(self):
		"""
		Loads a serialized json file to a memory as the CACHE, otherwise creates file.
		"""

		if os.path.isfile(self.filename):
			with open(self.filename, 'r+') as outfile:
			 	data = json.load(outfile)
			 	self.cache.update(data)
		else:
			print "File %s created" % (self.filename)


	def writejson(self):

		"""Writes the CACHE to JSON serialized file	"""		
		with open(self.filename, 'w+') as outfile:
			json.dump(self.cache, outfile, sort_keys=True, indent=4)




	def main(self):

		self.loadjson()

		self._factory()

		self.updatecache()

		self.writejson()


		return "Success loaded content to File: %s" % (self.filename)


		




if __name__ == '__main__':
	
	test = control("Liberian Observer" ,"http://www.liberianobserver.com/columns-health/liberia-discharges-only-confirmed-ebola-case-today")
	print test.main()



	# test2 = control("http://www.liberianobserver.com/business-investment/gol-urged-revive-tourism")

	# print test2.loadjson()

	# test = control("Title 1")

	# print test.loadjson()

	# test2 = control("Title 2")

	# print test2.loadjson()