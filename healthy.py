import os
def wenjian(path, txt_name, data):
    if os.path.exists(path):
        for i in range(1, 10):
            dir = path + "/yongshun" + str(i)  # 如果目录存在创建10个文件夹
            os.mkdir(dir)
            if os.path.exists(dir):
                wenjian_dir = os.listdir(path)
                for wenjian in wenjian_dir:
                    txt_dir = os.path.join(path, wenjian)
                    txt = txt_dir +'//'+ txt_name + ".txt"
                    with open(txt, "w", encoding="utf-8") as f:
                        f.write(data)
path = r"/mnt/d/Python/test"
txt_name = "test"
data = "曹永顺"
wenjian(path, txt_name, data)