# -*- coding:utf-8 -*-
import win32gui, win32ui, win32con, win32api, os, time, Tools, datetime, shutil,cv2
from PIL import Image
from imutils.perspective import four_point_transform
import numpy as np


# ================================截图=================================
def get_size(file):
    # 获取文件大小:KB
    size = os.path.getsize(file)
    return size / 1024


def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile


def compress_image(infile, outfile, mb=3500, step=10, quality=95):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)
    return outfile, get_size(outfile)


def window_capture(num):
    filename = Tools.SCREEN_PATH
    if (num == 1):
        time.sleep(5)
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # print(MoniterDev[1])
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print(w,h)     #图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    # 压缩图片
    # compress_image(filename, filename)


# ================================梯形修正=================================

def reviseImg():
    image = cv2.imread(Tools.SCREEN_PATH, cv2.IMREAD_COLOR)

    normal_four_points = [[958, 451], [888, 1117], [1600, 451], [1670, 1117]]
    ultimate_four_points = [[894, 186], [913, 453], [1666, 186], [1647, 453]]

    ultimate_img = four_point_transform(image, np.array(ultimate_four_points))
    normal_img = four_point_transform(image, np.array(normal_four_points))

    cv2.imwrite(Tools.ULTIMATE_PATH, ultimate_img)
    cv2.imwrite(Tools.NORMAL_PATH, normal_img)


# ================================截取图标=================================

def extractIcon():
    img1 = cv2.imread(Tools.ULTIMATE_PATH)
    img2 = cv2.imread(Tools.NORMAL_PATH)

    # 裁剪坐标为[y0:y1, x0:x1]
    # ====================================终极技能=============
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[0], img1[34:107, 24:99])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[1], img1[34:107, 154:229])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[2], img1[34:107, 284:360])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[3], img1[34:107, 414:489])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[4], img1[34:107, 545:620])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[5], img1[34:107, 675:750])

    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[6], img1[167:239, 24:99])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[7], img1[167:239, 154:229])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[8], img1[167:239, 284:360])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[9], img1[167:239, 414:489])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[10], img1[167:239, 545:620])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[11], img1[167:239, 675:750])

    # ====================================普通技能=============

    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[12], img2[13:78, 22:103])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[13], img2[13:78, 147:226])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[14], img2[13:78, 271:350])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[15], img2[13:78, 435:516])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[16], img2[13:78, 559:639])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[17], img2[13:78, 683:764])

    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[18], img2[117:181, 22:103])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[19], img2[117:181, 147:226])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[20], img2[117:181, 271:350])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[21], img2[117:181, 435:516])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[22], img2[117:181, 559:639])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[23], img2[117:181, 683:764])

    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[24], img2[219:283, 23:103])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[25], img2[219:283, 147:226])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[26], img2[219:283, 271:350])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[27], img2[219:283, 435:516])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[28], img2[219:283, 559:639])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[29], img2[219:283, 683:764])

    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[30], img2[378:441, 23:103])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[31], img2[378:441, 147:226])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[32], img2[378:441, 271:350])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[33], img2[378:441, 435:516])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[34], img2[378:441, 559:639])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[35], img2[378:441, 683:763])

    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[36], img2[479:543, 24:103])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[37], img2[479:543, 147:226])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[38], img2[479:543, 271:350])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[39], img2[479:543, 435:516])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[40], img2[479:543, 559:638])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[41], img2[479:543, 683:762])

    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[42], img2[581:644, 24:103])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[43], img2[581:644, 147:226])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[44], img2[581:644, 271:350])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[45], img2[581:644, 435:516])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[46], img2[581:644, 559:638])
    cv2.imwrite(Tools.ICONS_PATH + Tools.ICON_LIST[47], img2[581:644, 683:762])


def get_MD5(file_path):
    files_md5 = os.popen('md5 %s' % file_path).read().strip()
    file_md5 = files_md5.replace('MD5 (%s) = ' % file_path, '')
    return file_md5


def copyIcon(path, out):
    for files in os.listdir(path):
        name = os.path.join(path, files)
        back_name = os.path.join(out, files)
        if os.path.isfile(name):
            if os.path.isfile(back_name):
                if get_MD5(name) != get_MD5(back_name):
                    shutil.copy(name, back_name)
            else:
                shutil.copy(name, back_name)
        else:
            if not os.path.isdir(back_name):
                os.makedirs(back_name)
            copyIcon(name, back_name)


def savePic(idList):
    now = str(datetime.datetime.now()).replace('-', '').replace(' ', '').replace(':', '').replace('.', '')
    path1 = Tools.SAVE_IMG_PATH + now + '\\'
    path2 = Tools.SAVE_IMG_PATH + now + '\\' + 'icon' + '\\'
    os.mkdir(path1)
    os.mkdir(path2)
    compress_image(Tools.SCREEN_PATH, path1 + now + '.jpg')
    copyIcon(Tools.ICONS_PATH, path2)

    for n in range(0,len(Tools.ICON_LIST)):
        # print(path2+Tools.ICON_LIST[n])
        # print(path2+idList[n]+'.png')
        try:
            os.rename(path2+Tools.ICON_LIST[n],path2+idList[n]+'.png')
        except:
            pass