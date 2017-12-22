# -*- coding: utf-8 -*-
from urllib import request
import json
def fetch_data(URL):
	with request.urlopen(URL) as u:
		try:
			return json.loads(u.read().decode("utf-8"))
		except ValueError:
			raise ('ValueError:', URL)


# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid' \
	'%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
