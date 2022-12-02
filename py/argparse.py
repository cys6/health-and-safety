"""学习使用模块argparse操作"""
import argparse
import string
import random
import os
import sys
sys.path.append('')
the_str = string.ascii_letters+string.digits
name = ''.join(random.sample(the_str, 8))

def create(args):
    global create_path
    create_path = args.creater_path
    create_num = args.create_number
    # name=args.name
    if not os.path.exists(create_path):
        os.makedirs(create_path)
    for i in range(create_num):
        os.mkdir(create_path+os.sep+name+str(i))
    a = os.listdir(create_path)
    return a


def create_file(wenben_name, document_content):
    for i in create(args):
        file_dir = os.path.join(create_path, i)
        print(file_dir)
        with open(file_dir+os.sep+wenben_name, mode='w', encoding='utf-8')as f:
            f.write(document_content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='args for data filter')
    parser.add_argument('--creater_path', '-c', help='creater_path', type=str)
    parser.add_argument('--create_number', '-n',
                        help='create_number', type=int)
    # parser.add_argument('--name','-a', help='name', type=str)
    args = parser.parse_args()
# create(args)
create_file(wenben_name='a', document_content='1,8,9')