# !/usr/bin/python3
# -*- coding: utf-8 -*-

import bs4
import requests, re, os, Tools
dict1=Tools.rdJson(Tools.SKILL_MAP_JSON_PATH)
dict2=Tools.rdJson(Tools.SKILL_INFO_JSON_PATH)
dict3=Tools.rdJson(Tools.SKILL_HASH_JSON_PATH)


fl=Tools.list_all_files('Data\\imgfile')
li=[]
for p in fl:
    id=p.replace('Data\\imgfile\\','').replace('.png','')
    li.append(id)



list1=[]
list2=[]
list3=[]
for key in dict1:
    list1.append(key)

for key in dict2:
    list2.append(key)

for key in dict3:
    list3.append(key)



list_diff1=list(set(list1).difference(set(li)))
list_diff2=list(set(list2).difference(set(li)))
list_diff3=list(set(list3).difference(set(li)))


# print(len(dict2),len(dict3))

for i in  list_diff1:
     del dict1[i]
     del dict2[i]
     del dict3[i]

print(len(dict1))
print(len(dict2))
print(len(dict3))
Tools.wtJson(dict1,'skMap.json')
Tools.wtJson(dict2,'skInfo.json')
Tools.wtJson(dict3,'skHash.json')