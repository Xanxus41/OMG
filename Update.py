# !/usr/bin/python3
# -*- coding: utf-8 -*-
import bs4
import requests, re, os, Tools

# 技能名+图标
def getSkillandIcon(dataList, skDict, hero):
    if (len(dataList) != 0):
        str1 = str(dataList[0])
        nameSkill = re.findall(".*title=\"(.*)\"><img.*", str1)[0]
        urlIconSkill = re.findall(".*src=\"(.*)\" .*", str1)[0]
        enNameSkill=re.findall(".*Spellicons_(.*).png.*", urlIconSkill)[0]

        skillMap = Tools.rdJson(Tools.SKILL_MAP_JSON_PATH)
        idSkill = list(skillMap.keys())[list(skillMap.values()).index(nameSkill)]

        skDict['skName'] = nameSkill
        skDict['skEnName'] = enNameSkill
        skDict['skIcon'] = 'Data\\Image\\' + idSkill + '.png'


        # urlIconSk = urlIconSkill
        # if ('srcset' in urlIconSkill):
        #      urlIconSkill = re.findall(".*srcset=\"(.*) 1\.5.*", urlIconSk)[0]
        # download_img(urlIconSkill, Tools.SKILL_IMAGE_PATH, idSkill)


        return idSkill


# 蓝耗
def getManaCost(list, skDict):
    if (len(list) != 0):
        str1 = str(list[0])
        mc = re.findall(".*title=\"定值魔法消耗\">(.*)</span>.*", str1)[0]
        manaCost = mc.split('/', -1)[-1]
        manaCost = manaCost.strip().replace(')', '').replace('>', '').replace('a', '')
        skDict['manaCost'] = manaCost
        if (manaCost == '无'):
            skDict['manaCost'] = ''
    else:
        skDict['manaCost'] = ''


# CD
def getCoolDown(list, skDict):
    if (len(list) != 0):
        str1 = str(list[0])
        # print(str1)
        if ('Talent.png' in str1):
            cd = re.findall(".*</span>(.*)\(<a.*", str1)[0].strip().replace(')', '')
        else:
            cd = re.findall(".*</span>(.*)</div>.*", str1)[0].strip().replace(')', '')
        coolDown = cd.split('/', -1)[-1]
        skDict['coolDown'] = coolDown
        if (coolDown == '无'):
            skDict['coolDown'] = ''
    else:
        skDict['coolDown'] = ''


# A
def getAgha(list, skDict):
    Agha = ''
    if (len(list) >= 1):
        Agha = 'Yes'
    skDict['Agha'] = Agha





# 保存图片
def download_img(img_url, img_path, img_name):
    if (os.path.exists(img_path + img_name + '.png')):
        pass
    else:
        r = requests.get(img_url, stream=True)
        if r.status_code == 200:
            try:
                open(img_path + img_name + '.png', 'wb').write(r.content)  # 将内容写入图片
                # print(img_name)
            except FileNotFoundError:
                os.makedirs(img_path)
                open(img_path + img_name + '.png', 'wb').write(r.content)  # 将内容写入图片
                # print(img_name)
        del r


def getHeroData(hero, fixSkill):
    #通过url+英雄名得知该英雄的信息界面url
    url = Tools.URL_HERO_PAGE + hero
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    list = soup.find_all('div', class_="abilitybox full-width-xs")
    # 技能
    for i in range(0, len(list)):  # 技能+天赋=12
        str1 = str(list[i])
        soup2 = bs4.BeautifulSoup(''.join(str1), 'lxml')
        list2 = soup2.find_all('div', class_='floatnone')  # 技能名+图标
        list3 = soup2.find_all('span', title="定值魔法消耗")  # 蓝耗
        list4 = soup2.find_all('div', style="padding:0.5em 0.5em 0em 1em;cursor:help;")  # CD
        list5 = soup2.find_all('img', alt="Agha.png")  # A


        listSw = soup2.find_all('div', title="默认按键")
        if (len(listSw) == 1):
            skDict = {}
            idSkill = getSkillandIcon(list2, skDict, hero)  # 技能名+图标
            getManaCost(list3, skDict)  # 蓝耗
            getCoolDown(list4, skDict)  # CD


            #手动修正部分A杖技能
            if (idSkill in fixSkill):
                skDict['Agha'] = 'Yes'

            if (os.path.exists(Tools.SKILL_CACHE_PATH + idSkill + '.json')):
                pass
            else:
                Tools.wtJson(skDict, Tools.SKILL_CACHE_PATH + idSkill + '.json')
    print(hero)



def update():
    #指部分技能在wiki上没有A杖信息，但确实是有A杖效果的技能，需要手动修正；例如：无敌斩，发射钩爪
    #fixSkill为这类技能的id集合
    fixDict = Tools.rdJson(Tools.SKILL_FIX_JSON_PATH)
    fixSkill = fixDict['skillList']
    #遍历所有英雄
    for hero in Tools.HERO_LIST:
        getHeroData(hero, fixSkill)

    files = Tools.list_all_files(Tools.SKILL_CACHE_PATH)
    newDict = {}
    for file in files:
        id = file.replace(Tools.SKILL_CACHE_PATH, '').replace('.json', '')
        dict = Tools.rdJson(file)
        newDict[id] = dict

    # 将新内容更新到旧Json上
    oldDict = Tools.rdJson(Tools.SKILL_INFO_JSON_PATH)
    for k, v in newDict.items():
        oldDict[k] = v
    # 将dict写入Json文件
    Tools.wtJson(oldDict, Tools.SKILL_INFO_JSON_PATH)


    # 删除临时Json文件
    cacheFile = Tools.list_all_files(Tools.SKILL_CACHE_PATH)
    for js in cacheFile:
        os.remove(js)
    print('数据更新成功')

update()