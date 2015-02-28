"""
A collector module for JET.

Uses spiders and other collector agents to scape a list of jouranlism sites and save the results to DB. 


Author:
Nathan Danielsen
nathan.danielsen@irex.org
"""

#SITES = SITES # import from list of sites by type

import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.item import Item, Field

class TorrentItem(Item):
	url = Field()
	title = Field()
	# name = Field()
	# description = Field()
	# size = Field()



class LOBSpider(CrawlSpider):

	name = "LOB"
	allowed_domains = ['http://www.liberianobserver.com/']
	start_urls = ['http://www.liberianobserver.com/news-security/']
	Rule(LinkExtractor(allow=('liberianobserver.com',), callback='parse_item)

	def parse_item(self, response):
		sel = Selector(response)
		torrent = TorrentItem()
		torrent['url'] = response.url
		torrent['title'] = sel.xpath("//title.text()")
		return torrent


        # torrent['name'] = sel.xpath("//h1/text()").extract()
        # torrent['description'] = sel.xpath("//div[@id='description']").extract()
        # torrent['size'] = sel.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
        #return torrent

if __name__ == "__main__":

	test = LOBSpider()

	test.url
	test.title
















class RSSSpider(object):
	"""
	Visits a list of RSS feeds- harvests urls, title, teaser and author info.

	"""
	def __init__(self):
		pass
