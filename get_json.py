#!/usr/bin/env python
# -*- coding: utf8 -*-
import json, io

path = 'result.json'
opath = 'test.txt'

chatname = 'Dyvan Riders'
username = 'Mah Boi'
  
with io.open(opath, 'w', encoding='ISO-8859-1') as of:	
	with open(path, encoding='ISO-8859-1') as f:
		data = json.load(f)	
		if data['chats']['list'][0]['name'] == chatname:
			lst = data['chats']['list'][0]['messages']
			for line in lst:
				if 'from' in line:				
					if line['from'] == username:
						if line['type'] == 'message':
							if not isinstance(line['text'],(list,)):
								msg = json.dumps(line['text'], ensure_ascii=True)
								my_bytes = msg.encode()
								asd = my_bytes.decode("unicode-escape").replace('"','') + '\n'
								if asd != '\n':
									of.write(asd)	
							else:
								if len(line['text']) > 2:
									msg = json.dumps(line['text'][2], ensure_ascii=True)
									my_bytes = msg.encode()
									asd = my_bytes.decode("unicode-escape").replace('"','') + '\n'
									if asd != '\n':
										of.write(asd)
