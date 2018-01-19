from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

class CheckCode(object):
	# 随机字母
	def rndchr(self):
		return chr(random.randint(65, 90))
	
	# 背景颜色
	def rndcolor_b(self):
		return random.randint(127, 255), random.randint(127, 255), random.randint(127, 255)
	
	# 字体颜色
	def rndcolor_n(self):
		return random.randint(50, 127), random.randint(50, 127), random.randint(50, 127)
	
	def get_code(self):
		# 100*25
		width = 20 * 4
		height = 20
		code_list = ''
		global image
		image = Image.new('RGB', (width, height), (255, 255, 255))
		# 创建Font
		font = ImageFont.truetype('arial.ttf', 20)
		# 创建Draw
		draw = ImageDraw.Draw(image)
		# 填充像素
		for x in range(width):
			for y in range(height):
				draw.point((x, y), fill=self.rndcolor_b())
		# 输出文字
		for t in range(4):
			code=self.rndchr()
			draw.text((20*t+2, 0), code, font=font, fill=self.rndcolor_n())
			code_list = code_list +code
		# 模糊
		# image = image.filter(ImageFilter.BLUR)
		image.save('code.gif', 'gif')
		# image.show ('code.gif')
		return code_list
		
		# print(code_list)

if __name__ == '__main__':
	code = CheckCode()
	print(code.get_code())
