# -*- coding: utf-8 -*-
import re


# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#           someone@gmail.com
#			bill.gates@microsoft.com

#re_email = re.compile(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9.]+\.com$')
re_email = re.compile(r'^[a-zA-Z0-9.]+@(\[?)[a-zA-Z0-9\-.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$')
def is_email(addr):
	if re_email.match(addr):
		print('[%s]...is a email.' % addr)
	else:
		print('[%s]...is not a email.' % addr)


# 版本二可以提取出带名字的Email地址:
#    <Tom Paris> tom@voyager.org => Tom Paris
#    bob@example.com => bob

#re_email_n = re.compile(r'')

if __name__ == '__main__':
	is_email('someone@gmail.net')
	is_email('bill.gates@microsoft.cn')
	is_email('bob#example.com')
	is_email('mr-bob@example.com')
