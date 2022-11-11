import os
def file_dir(path, datas):
    datas = os.listdir(path)
    for data in datas:
        print(os.path.join(path, data))
#传入目录所在的位置
path = r"/mnt/d/Python"
file_dir(path, datas=None)