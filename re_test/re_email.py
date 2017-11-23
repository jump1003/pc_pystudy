# -*- coding: utf-8 -*-
import re


# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#           someone@gmail.com
#			bill.gates@microsoft.com

#re_email = re.compile(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9.]+\.com$')
# re_email = re.compile(r'^[a-zA-Z0-9.]+@(\[?)[a-zA-Z0-9\-.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$')
# def is_email(address):
# 	if re_email.match(address):
# 		print('[%s]...is a email.' % address)
# 	else:
# 		print('[%s]...is not a email.' % address)


# 版本二可以提取出带名字的Email地址:
#    <Tom Paris> tom@voyager.org => Tom Paris
#    bob@example.com => bob

re_email_n = re.compile(r'<?([a-zA-Z0-9\s]*)>?\s?([a-zA-Z0-9]*)@([a-zA-Z0-9]+)\.([a-zA-Z]{2,3}|[0-9]{1,3})$')
def name_email(address):
	print(re_email_n.match(address).group(1))


if __name__ == '__main__':
	# is_email('someone@gmail.net')
	# is_email('bill.gates@microsoft.cn')
	# is_email('bob#example.com')
	# is_email('mr-bob@example.com')
	name_email('<Tom Paris> tom@voyager.org')
	name_email('bob@example.com')
