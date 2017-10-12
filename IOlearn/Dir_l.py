import os,sys
from datetime import datetime
dict_os={'C':'OS','E':'软件','F':'文档'}
def Dir_l(path_dir=os.path.abspath('.')):
	pwd = path_dir
	dir_num = 0
	file_num = 0
	dir_size = 0
	file_size = 0
	os.chdir(pwd)
	print('驱动器 %s 中的卷是 %s\n'% (pwd.split(':')[0],dict_os[pwd.split(':')[0]]))
	print('%s 的目录'%pwd)
	print('%s%11s%10s%12s'%('最后修改日期','类型','size','文件名'))

	for f in os.listdir(pwd):
		f_size = os.path.getsize( f ) #文件大小
		f_type = '<DIR>' if os.path.isdir(f) else os.path.splitext(f)[1] #如果是子目录，<DIR>，如果是文件，返回文件类型
		modified_time = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y/%m/%d  %H:%M')
		print('%s%8s%10d        %s'%(modified_time,f_type,f_size,f))
		if os.path.isdir(f):
			dir_size += f_size
			dir_num += 1
		else:
			file_size += f_size
			file_num += 1
	print('%11d 个文件%22d 字节'%(file_num,file_size))
	print('%11d 个目录%22d 字节'%(dir_num, dir_size))

if __name__ == '__main__':
#Dir_l('F:/Python_study/function')
	Dir_l()