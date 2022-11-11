import json

sample_dict = {
    "jira_link": "NA",
    "mdi_download_link": "NA",
    "aws_download_link": "NA",
    "mviz_link": "NA"
}

sample_list = [sample_dict for i in range(50)]#第一种写法
"""
sample_lict=[]
for i in range(50):
    sample_lict.append(sample_dict)
第二种写法
"""
with open('temp.json', 'w') as f:
    json.dump(sample_list, f, indent=4)
