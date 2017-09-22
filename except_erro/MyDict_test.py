import unittest
from mydict import Dict


class TestDict(unittest.TestCase):
	def test_init(self):
		d = Dict(a=1, b='text')
		self.assertEquals(d.a,1)
		self.assertEquals(d.b,'text')
		self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d = Dict()
		d['key']= 'value'
		self.assertEquals(d.key,'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'],'value')

	def test_keyerro(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerro(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	def setUp(self):
		print('setup...ing')

	def tearDown(self):
		print('teardown...ing')
# if __name__ == '__main__':
# 	unittest.main()