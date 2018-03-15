import datetime
import json
import re
import requests
from bs4 import BeautifulSoup
import pymysql

url_address = "http://news.sina.com.cn/china/"
res = requests.get(url_address)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')
dicts = {'data-client': 'headline'}
url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||' \
      '=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}'
news_total = []

def getCommentCounts(url):
	newsid = re.search('doc-i(.*).shtml', url).group(1)
	counturl = 'http://comment5.news.sina.com.cn/cmnt/count?format=json&newslist=gn:comos-' + newsid + ':0'
	count_res = requests.get(counturl)
	jd = json.loads(count_res.text)
	return jd['result']['count']['gn:comos-' + newsid + ':0']['total']


def getNewsDetail(urls):
	result = {}
	news_res = requests.get(urls)
	news_res.encoding = 'utf-8'
	news_soup = BeautifulSoup(news_res.text, 'html.parser')
	date_source = news_soup.select(".date-source")
	if len(date_source):
		date = date_source[0].select('.date')[0].text
		result['dt'] = datetime.datetime.strptime(date, '%Y年%m月%d日 %H:%M')
		result['source'] = date_source[0].select('.source')[0].text
		result['main-title'] = news_soup.select('.main-title')[0].text
		result['nr'] = '\n'.join([p.text.strip() for p in news_soup.select('#article p')[:-1]])
		result['author'] = news_soup.select('.show_author')[0].text.lstrip('责任编辑：')
		result['comment_count'] = getCommentCounts(urls)
		result['href'] = urls
		return result
	else:
		return None

	
def parserListLinks(urls):
	newsdetails = []
	ress = requests.get(urls)
	jd = json.loads(ress.text)
	for ent in jd['result']['data']:
		newsdetails.append(getNewsDetail(ent['url']))
	return newsdetails
	
	
# for news in soup.select('.news-item'):
# 	news_data = []
# 	if len(news.select('h2')) > 0:
# 		title = news.select('h2')[0].text
# 		news_url = news.select('a')[0]['href']
# 		news_data.append(getNewsDetail(news_url))
# 		print(news_data)
# 		news_total.extend(news_data)


for i in range(1, 3):
	newsurl = url.format(i)
	newsary = parserListLinks(newsurl)
	news_total.extend(newsary)

# df = pandas.DataFrame(news_total)
# df.to_excel('news_total.xlsx')

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='jump',
                       password='jump',
                       db='python_db',
                       charset="utf8")
cur = conn.cursor()
news_count = 0
for news in news_total:
	cur.execute("insert into sina_news(title, time, source, author, comment_count, nr, href) VALUES(%s, %s, %s, %s, %s, %s, %s)",
            [news['main-title'], news['dt'], news['source'], news['author'], int(news['comment_count']), news['nr'], news['href']])
	conn.commit()
	news_count += 1
print('**************  共有 %d 条数据  **************' % len(news_total))
print('************** %d  数据保存成功 **************' % news_count)
cur.close()

	