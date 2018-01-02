from xml.parsers.expat import ParserCreate

xml = r'''
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
    <yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="Beijing" country="China" region=" Beijing"/>
</ol>
'''


class DefaultSaxHandler (object):
	def start_element(self, name, attrs):
		print('sax:start_element %s, attrs: %s' % (name, str (attrs)))
		if name== 'a':
			print(attrs["href"])

	def end_element(self, name):
		print('sax:end_element %s' % name)

	def char_data(self, text):
		print('sax:char_element %s' % text)

handle = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handle.start_element
parser.EndElementHandler = handle.end_element
parser.CharacterDataHandler  = handle.char_data
parser.Parse(xml)