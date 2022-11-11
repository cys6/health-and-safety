import os
import json
def readfile(path):
    filename = os.listdir(path)
    jsonfile = dict()
    for filname in filename:
        p = os.path.join(path, filname)
        with open(p, mode='r', encoding='utf-8')as f:
            data = f.read()
        jsonfile[filname.rstrip(".txt")] = data
    return jsonfile
def saveInJsonFile(json_dir):
    with open(json_dir, 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsonfile, ensure_ascii=False, indent=9))
readpath = r"D:\file"
jsonfile = readfile(readpath)
save_path = r"json\1.json"
saveInJsonFile(save_path)