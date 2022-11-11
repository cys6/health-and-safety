import json
jsona = {}
"""定义一个空的字典，负责等下的json文件"""
a = json.loads(json.dumps(jsona))
"""把这个空的字典转化为python可以读取的格式"""
a['auto'] = 'NONE'  # 第一层json内容
auto2 = {"爱好": "跑步", "特点": "可以", "write": {}}
write = {'dushu': '66', 'xiezi': '88'}
a['auto2'] = auto2  # 第二层json内容
a['auto2']['write'] = write  # 第三层json内容,用索引的方法找到write并写入
auto = json.dumps(a, ensure_ascii=False)
print(auto)
print(json.dumps({'99': 'aa'}, ensure_ascii=False))
"""
json.loads 把字符串转换为json
json.load 把文件转换未为json
json.dumps 将一个数据结构转换为json
"""