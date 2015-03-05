"""
Working through several methods of importing and cleaning html. 

This is the source of this code
https://github.com/ndanielsen/A-Smattering-of-NLP-in-Python
"""

from urllib import urlopen

from readability.readability import Document
from bs4 import BeautifulSoup


class PageCleaner(object):
	"""
	Takes an html and returns the Title and Main Content.

	Next version to include author, post-date, image URL, image caption and other unique information. 

	"""
	def __init__(self, url):
		self.url = urlopen(url).read() 
		self.json = {}

	def _extract(self):
		"""
		Takes a URL and returns the Title and the Main Content
		"""

		html = self.url
		readable_article = Document(html).summary()
		readable_title = Document(html).title()
		soup = BeautifulSoup(readable_article)
		


		#author = title.find_next("a", href=True)	



		return readable_title, soup.text


	
	def main(self):
		"""
		Cleans and returns values
		"""
		title, text = self._extract()

		return title, text






if __name__ == '__main__':
	testy = PageCleaner("http://www.liberianobserver.com/news/%E2%80%9Cjudiciary-c%E2%80%99ttee-will-be-vibrant-resourceful%E2%80%A6%E2%80%9D")

	print testy