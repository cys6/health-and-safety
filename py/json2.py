import json
jsonfile = {}
json_a = json.loads(json.dumps(jsonfile))#转换为python结构
bag_name = {
    'bag_name': 'PLAFC6993_event_cpi_cpd_recording_20220722-213957_0.bag',
    'md5': 'aa',
    'mviz_Link': 'http://www.***com',
    'car': {}
}
json_a["bag"] = bag_name
car = {
    '名称': '宝马',
    '型号': 'suv',
    '价格': '中等'
}
json_a["bag"]['car'] = car
md5 = {
    '下载链接地址': 'mdi fetch -o PLAFC6993***',
    '有效期': '无限制'}
json_a['md5'] = md5
#bag = json.dumps(json_a, ensure_ascii=False)#转换为json
json_lict=[json_a for i in range(50)]
with open('D:/aamomenta.json', 'w') as f:
    try:
        json.dump(json_lict,f,indent=9)
        print('json文件创建成功')
    except:
        print('文件创建失败')
"""dumps是将dict转化成str格式，loads是将str转化成dict格式,dump和load也是类似的功能，只是与文件操作结合起来了。"""