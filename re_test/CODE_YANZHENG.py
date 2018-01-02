from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndchr():
	return chr(random.randint(65, 90))

# 背景颜色
def rndcolor_b():
	return random.randint(127, 255), random.randint(127, 255), random.randint(127, 255)

# 字体颜色
def rndcolor_n():
	return random.randint(50, 127), random.randint(50, 127), random.randint(50, 127)


# 240*60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font
font = ImageFont.truetype('arial.ttf', 36)
# 创建Draw
draw = ImageDraw.Draw(image)
# 填充像素
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndcolor_b())
# 输出文字
for t in range(4):
	draw.text((60*t+10, 10), rndchr(), font=font, fill=rndcolor_n())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
image.show('code.jpg')
