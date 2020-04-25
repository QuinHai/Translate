# -*- coding: utf-8 -*-
import sys
import requests
import json
from  urllib.parse import quote 

raw_handle = open(sys.argv[1], 'r',encoding='UTF-8')
translate_api = "http://fanyi.youdao.com/translate?&doctype=json&type=%s&i=%s"

raw_data = json.load(raw_handle)
for key, value in raw_data.items():
	r = requests.get(translate_api % ('EN2ZH_CN', quote(value)))
	if r.status_code != 200:
		continue
	tran_val = json.loads(r.text)
	raw_data[key] = tran_val['translateResult'][0][0]['tgt']

outfile_handle = open(sys.argv[2], 'w', encoding="UTF-8")
json.dump(raw_data, outfile_handle, ensure_ascii=False, sort_keys=False, indent=4)

raw_handle.close()
outfile_handle.close()
