"""
A collector module for JET.

Uses spiders and other collector agents to scape a list of jouranlism sites and save the results to DB. 


Author:
Nathan Danielsen
nathan.danielsen@irex.org
"""

SITES = SITES # import from list of sites by type


class RSSSpider(object):
	"""
	Visits a list of RSS feeds- harvests urls, title, teaser and author info.

	"""
	def __init__(self):
		pass
