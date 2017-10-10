# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import re

html_doc = """<a href="javascript:;" name="tj_settingicon" class="pf">设置<i class="c-icon c-icon-triangle-down"></i></a>
           <a href="http://i.baidu.com" id="user" class="username">6leaves_<i class="c-icon"></i></a>
           <p class="s-skin-lm s-isindex-wrap">hahahhha</p>"""
soup = BeautifulSoup (html_doc, 'html.parser')
print ('打印所有节点')
links = soup.find_all ('a')
for link in links:
	print (link.name, link['href'], link.get_text ())
print('打印指定节点')
link_node = soup.find('a',href='javascript:;')
print(link_node.name, link_node['href'], link_node.get_text())
print('正则匹配')
link_re = soup.find('a',href=re.compile(r"baidu"))
print(link_re.name, link_re['href'], link_re.get_text())
print('获取p段落文字')
p_node = soup.find('p',class_=re.compile(r"skin"))
print(p_node.name, p_node.get_text())
