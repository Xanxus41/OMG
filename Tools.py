# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os, json

URL_HERO_PAGE = 'https://dota.huijiwiki.com/wiki/'  # 爬取url

IMG_PATH1 = 'Data\\furion.png'  # laber图片1路径
IMG_PATH2 = 'Data\\axe.png'  # laber图片2路径
IMG_PATH3 = 'Data\\AM.png'  # laber图片3路径
IMG_PATH4 = 'Data\\Earthshaker.png'  # laber图片4路径
IMG_PATH5 = 'Data\\mango.png'  # laber图片5路径



COMBO_PATH = "Data\\combo.txt"  # combo文件路径
LOGO_PATH = 'Data\\omg.ico'  # 图标路径


SCREEN_PATH = 'Cache\\img\\image.jpg'  # 截图文件路径
ULTIMATE_PATH = 'Cache\\img\\ultimate_img.png'  # 终极技能修正后路径
NORMAL_PATH = 'Cache\\img\\normal_img.png'  # 普通技能修正后路径

SKILL_MAP_JSON_PATH = 'Data\\SkillMap.json'  # 技能id对照文件路径
SKILL_FIX_JSON_PATH = 'Data\\SkillFix.json'  # 技能信息修正文件路径
SKILL_INFO_JSON_PATH = 'Data\\SkillInfo.json'  # 技能详情文件路径
SKILL_HASH_JSON_PATH = 'Data\\SkillHash.json'  # 技能hash值文件路径

ICONS_PATH = 'Cache\\icon\\'  # 截取图标目录
SKILL_IMAGE_PATH = 'Data\\Image\\'  # 技能图标目录
SKILL_CACHE_PATH = 'Cache\\json\\'  # json缓存目录
SCREEN_CACHE_PATH = 'Cache\\img\\'
SAVE_IMG_PATH = 'Save\\'



HERO_LIST = ['半人马战行者', '大地之灵', '小小', '巨牙海民', '昆卡', '末日使者', '酒仙', '凤凰', '撼地者', '潮汐猎人', '发条技师', '马格纳斯', '斯拉达', '狼人',
             '食人魔魔法师', '树精卫士', '斧王', '玛尔斯', '军团指挥官', '全能骑士', '混沌骑士', '裂魂人', '帕吉', '龙骑士', '伐木机', '电炎绝手', '斯温', '杰奇洛',
             '哈斯卡', '上古巨神', '术士', '蝙蝠骑士', '孽主', '天穹守望者', '育母蜘蛛', '亚巴顿', '暗夜魔王', '黑暗贤者', '变体精灵', '沙王', '冥魂大帝', '死亡先知',
             '兽王', '钢背兽', '殁境神蚀者', '风行者', '艾欧', '炼金术士', '娜迦海妖', '不朽尸王', '剃刀', '维萨吉', '血魔', '齐天大圣', '熊战士', '寒冬飞龙',
             '暗影恶魔', '祸乱之源', '虚无之灵', '沉默术士', '影魔', '灰烬之灵', '先知', '幽鬼', '噬魂鬼', '矮人直升机', '虚空假面', '巨魔战将', '谜团', '瘟疫法师',
             '赏金猎人', '工程师', '干扰者', '天涯墨客', '冥界亚龙', '德鲁伊', '修补匠', '司夜刺客', '戴泽', '拉席克', '暗影萨满', '莉娜', '神谕者', '石鳞剑士',
             '圣堂刺客', '复仇之魂', '力丸', '祈求者', '帕克', '露娜', '幻影刺客', '巫医', '主宰', '陈', '幻影长矛手', '光之守卫', '宙斯', '水晶室女', '米拉娜',
             '莱恩', '痛苦女王', '巫妖', '剧毒术士', '拉比克', '天怒法师', '风暴之灵', '邪影芳灵', '克林克兹', '帕格纳', '米波', '斯拉克', '远古冰魄', '编织者',
             '卓尔游侠', '狙击手', '魅惑魔女', '恐怖利刃', '敌法师', '美杜莎']

ICON_LIST = ['1-1.png', '1-2.png', '1-3.png', '1-4.png', '1-5.png', '1-6.png',
             '2-1.png', '2-2.png', '2-3.png', '2-4.png', '2-5.png', '2-6.png',
             '3-1.png', '3-2.png', '3-3.png', '3-4.png', '3-5.png', '3-6.png',
             '4-1.png', '4-2.png', '4-3.png', '4-4.png', '4-5.png', '4-6.png',
             '5-1.png', '5-2.png', '5-3.png', '5-4.png', '5-5.png', '5-6.png',
             '6-1.png', '6-2.png', '6-3.png', '6-4.png', '6-5.png', '6-6.png',
             '7-1.png', '7-2.png', '7-3.png', '7-4.png', '7-5.png', '7-6.png',
             '8-1.png', '8-2.png', '8-3.png', '8-4.png', '8-5.png', '8-6.png']


# 列出目录下文件
def list_all_files(rootdir):
    _files = []
    # 列出文件夹下所有的目录与文件
    list_file = os.listdir(rootdir)
    for i in range(0, len(list_file)):
        # 构造路径
        path = os.path.join(rootdir, list_file[i])
        # 判断路径是否是一个文件目录或者文件
        # 如果是文件目录，继续递归
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files


# 将dict类型存为Json文件
def wtJson(dict, path):
    with open(path, 'w', encoding='utf-8') as file_obj:
        json.dump(dict, file_obj, ensure_ascii=False)


# 打开Json文件为dict类型
def rdJson(path):
    with open(path, 'r', encoding='utf-8') as f:
        dict = json.load(fp=f)
        f.close()
    return dict
