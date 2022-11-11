import json

jsonfile = {}
json_file = json.loads(json.dumps(jsonfile))
json_a = {
    "bag_name": "PLQ70VC8_event_cpi_cpd_recording_20220721-113154_0.bag",
    "md5": "04f6167c1d3d5d600da26c221bc0315e",
    "mdi_link": "mdi fetch -o PLQ70VC8_event_cpi_cpd_recording_20220721-113154_0.bag 04f6167c1d3d5d600da26c221bc0315e",
    "maf_version": "maf3.1.0",
    "plate_number": "PLQ70VC8",
    "start_sec": 0,
    "end_sec": 0,
    "is_valid": 0,
    "soft_version": "Devcar-V2.0.1-20220718.88-Release_HNP2.0.1.4_9.tgz",
    "mviz_link": "https://mviz.momenta.works/player/v4/?user=MSD&format=multi_pbe_gz&zip=20&path=//mviz-convert-prod-data-obs.obs.cn-east-3.myhuaweicloud.com/mpilot-highway_20220721-120640_S3YCNR0NB04318M/PLQ70VC8_event_cpi_cpd_recording_20220721-101138/PLQ70VC8_event_cpi_cpd_recording_20220721-113154_0/v4/99914b932bd37a50b983c5e7c90ae93b",
    "left_road_border": "false",
    "right_road_border": "false"
}
json_file[''] = json_a
jsonbag = json.dumps(json_file, ensure_ascii=False, indent=9)
print(jsonbag)