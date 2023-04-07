import os

path = 'D:\Desktop\python学习\cpp'
dest_path = 'D:\Desktop\python学习\c_codes'
files = os.listdir(path)
from shutil import copyfile

for f in files:
    string = f.split('.')[-1]
    if string == 'cpp':
        copyfile(path + '\\' + f, dest_path + '\\' + f)
    # print(str)
