import json

"""对2个文件进行处理，加到一个列表"""
def jsonread(json1, json2):
    with open(json1) as f:
        jsonfile1 = json.load(f)
    with open(json2) as f:
        jsonfile2 = json.load(f)
    lict = []
    lict.extend(jsonfile1)
    lict.extend(jsonfile2)
    return ''.join(lict)


"""把新文件存储为json格式"""
wenjianhebing = jsonread("json1_dir", "json2_dir")
with open(wenjianhebing.json) as f:
    json.dump(wenjianhebing, f, indent=9)
