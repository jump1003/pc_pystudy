# -*- coding: utf-8 -*-
import base64, struct
def safe_base64_decode(s):
	if isinstance(s, bytes):
		s = str(s, encoding='utf-8')
	# 长度不足4的倍数，补足=符号
	blank = len(s) % 4
	return base64.b64decode(s+'='*blank)


# 测试：
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode(b'YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode(b'YWJjZA')
# print('pass')


def bmp_info(data):
	with open(data, 'rb') as p:
		# b = base64.b64decode(p.read(30))
		bmp = struct.unpack('<ccIIIIIIHH', p.read(30))
		if bmp[0] == b'B' and bmp[1] == b'M':
			print('This is a bmp!')
			print(bmp)
			print('This\'s bmp size is [%d],color is [%d] ' % (bmp[2], bmp[-1]))
			print('Width: [%d], Height: [%d]' % (bmp[-4], bmp[-3]))
		else:
			print('This is not a bmp!')
			print(bmp)


if __name__ == '__main__':
	bmp_info(r'F:\Python_study\photo.bmp')
