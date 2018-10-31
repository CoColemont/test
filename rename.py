import os

path_dir = 'G:/数据结构/数据结构/考点精讲'

for file in os.listdir(path_dir):  # os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
    path = path_dir + '/' + file
    new_name = path[0: -25] + path[-4:]  # 选择名字中需要保留的部分
    os.rename(path, new_name)
    

# 敲黑板了：os.rename(path, new_name)，path和new_name的路径要一致，否则会报系统找不到路径这样的错误
# 并且path的路径一定要具体到需要修改的文件名。例：G:/数据结构/数据结构/考点精讲/1.1数据结构的基本概念.mp4。
