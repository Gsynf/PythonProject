'''
Function:
	图片批量重命名
'''
import os


target_path = 'pictures'
for idx, each in enumerate(os.listdir(target_path)):
	os.rename(os.path.join(target_path, each), os.path.join(target_path, '%s.jpg' % idx))
