# !usr/bin/env python3
# -*- coding: utf-8 -*-


class Screen(object):

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise ValueError('width must be an integer!')
		if value < 0:
			raise ValueError('width must be greater than 0!')
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		if not isinstance(value, int):
			raise ValueError('height must be an integer!')
		if value < 0:
			raise ValueError('height must be greater than 0!')
		self._height = value

	@property
	def resolution(self):
		return self.width * self.height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
