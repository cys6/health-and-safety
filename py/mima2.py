import random
import json
import datetime


def get_UPPer():
    """获取大写的字母"""
    count = random.randint(1, 3)  # 随机生成的数量
    UPPer = random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=count)  # 随机生成的区间，在A-Z
    return UPPer


def get_tesguzifu():
    """获取特殊字符"""
    count = random.randint(1, 3)
    TSZF = random.choices('!@#$%^&*_+{}:"<>?,./\}', k=count)
    return TSZF


def get_lower(count):
    '''
    生成小写字母和数字
    :param count:
    :return:
    '''
    # count=random.choices(1,6)
    string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    str = random.choices(string, k=count)
    return str


def password(changdu):
    """生成密码，调用前面生成的字符"""
    if changdu > 6:
        changdu = 6
    if changdu < 6:
        changdu = 6
    lict = []
    lict_UPPer = get_UPPer()
    lict_teshuzifu = get_tesguzifu()

    lict.extend(lict_UPPer)  # 把大写字母加入列表
    lict.extend(lict_teshuzifu)  # 把特殊字符加入列表

    surplus_count = changdu - len(lict)  # 小写字母/数字个数=长度-已经存在列表里的大写字母和特殊字符
    lower = get_lower(surplus_count)
    lict.extend(lower)  # 小写字母和数字加入列表

    random.shuffle(lict)
    """打乱密码顺序"""
    return ''.join(lict)  # 把列表转换成字符串


if __name__ == '__main__':
    a = password(3)
    with open('json/mima.json', 'w', encoding='utf-8') as f:
        json.dump(a, f, ensure_ascii=False, indent=4)
        print(datetime.datetime.now())

"""
先随机生成大写字母，随机生成1-3个，在随机生成特殊字符，随机生成1-3个，
在随机生成小写字母和数字，随机生成剩下的，在把3个函数转换成一个列表，最后转换为字符串
"""
