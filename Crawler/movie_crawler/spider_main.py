# -*- coding: utf-8 -*-
from Crawler.movie_crawler import html_downloader, url_manager, html_parser, html_output


class SpiderMovie (object):
	def __init__(self):
		self.urls = url_manager.UrlManage()
		self.downloader = html_downloader.Download()
		self.parser = html_parser.Parser()
		self.output = html_output.Output()

	def craw(self, spider_url):
		count = 1
		self.urls.add_new_url(spider_url)
		while self.urls.has_new_url():
			new_url = self.urls.get_new_url()
			print('Craw %d: %s ' % (count, new_url))
			html_cont = self.downloader.download(new_url)
			new_urls, new_data = self.parser.parse(new_url, html_cont)
			self.urls.add_new_urls(new_urls)
			self.output.searchdata(new_data)
			if count == 10:
				break
			count += 1
		self.output.output_html()


if __name__ == "__main__":
	root_url = r'https://movie.douban.com'
	obj_spider = SpiderMovie()
	obj_spider.craw(root_url)
