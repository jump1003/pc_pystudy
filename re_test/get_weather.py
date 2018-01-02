# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request
import re, enum

#创建枚举便于查询
@enum.unique
class WeekDay(enum.Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6


class WeatherSaxHandler(dict):
	#<yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="Beijing" country="China" region=" Beijing"/>
	#<yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="Fri, 29 Dec 2017 09:00 AM CST" temp="22" text="Mostly Sunny"/>
	#<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="29 Dec 2017" day="Fri" high="41" low="17" text="Partly Cloudy"/>
	def end_element(self, name):
		pass
	
	def char_data(self, text):
		pass
	
	def start_element(self, name, attrs):
		re_weather = re.compile(r'yweather:(\w*)')
		weather_macth = re_weather.match(name)
		if weather_macth:
			group_mark = weather_macth.group(1)
			#取城市
			if group_mark == 'location':
				self['city'] = attrs["city"]
				self['country'] = attrs["country"]
			#取日期
			elif group_mark == 'condition':
				today = str(attrs["date"]).split(',')[0]
				if WeekDay[today]:
					self.__today = WeekDay[today].value
					if self.__today == 6:
						self.__tomorrow = 0
					else:
						self.__tomorrow = self.__today + 1
			elif group_mark == 'forecast':
				attr = dict()
				if WeekDay[attrs['day']].value == self.__today:
					attr['low'] = int(attrs['low'])
					attr['high'] = int(attrs['high'])
					attr['day'] = attrs['day']
					attr['text'] = attrs['text']
					self['today'] = attr
				elif WeekDay[attrs['day']].value == self.__tomorrow:
					attr['low'] = int (attrs['low'])
					attr['high'] = int (attrs['high'])
					attr['day'] = attrs['day']
					attr['text'] = attrs['text']
					self['tomorrow'] = attr
		
def parser_weather(xml):
	handle = WeatherSaxHandler ()
	parser = ParserCreate ()
	parser.StartElementHandler = handle.start_element
	parser.EndElementHandler = handle.end_element
	parser.CharacterDataHandler = handle.char_data
	parser.Parse(xml)
	return handle


# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read().decode('utf-8')

result = parser_weather(data)
assert result['city'] == 'Beijing'
print('weather:',result)