# -*- coding:utf-8 -*-
import UI, MyOCR, Update, ProcessImg, Tools
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class OMG(QWidget):
    def __init__(self, parent=None):

        super(OMG, self).__init__()

    def initUI(self):
        # 设置点击表头排序

        ui.SkillTableView.setSortingEnabled(True)
        ui.ComboTableView.setSortingEnabled(True)
        # 设置禁止编辑

        ui.SkillTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        ui.ComboTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置自适应列宽

        ui.SkillTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        ui.ComboTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置隐藏列表头

        ui.SkillTableView.verticalHeader().setVisible(False)
        ui.ComboTableView.verticalHeader().setVisible(False)
        # 设置图标大小

        ui.SkillTableView.setIconSize(QSize(64, 64))
        ui.ComboTableView.setIconSize(QSize(64, 64))

        # 点击按钮展示数据
        ui.startBtn.clicked.connect(lambda: self.showData(1))
        ui.start2Btn.clicked.connect(lambda: self.showData(2))
        ui.updateBtn.clicked.connect(self.update)


    def getSkillInfo(self, idList, skNameList):
        #技能信息列表
        infoList = []
        #读取全部信息
        dict = Tools.rdJson(Tools.SKILL_INFO_JSON_PATH)

        for id in idList:
            infoList.append(dict[id])
            skNameList.append(dict[id]['skName'])
        return infoList

    def getComboList(self):
        comboList = []
        f = open(Tools.COMBO_PATH, "r", encoding='UTF-8')
        for x in f:
            x = x[:-1]
            combo = x.split('+')
            comboList.append(combo)
        f.close()
        return comboList

    def update(self):
        Update.update()
        QMessageBox.information(self, '提醒', '数据更新成功!')



    # 展示数据
    def showData(self, num):
        # 表格模型
        self.skillModel = QStandardItemModel(0, 0)
        self.skillModel.setHorizontalHeaderLabels(['图标', '技能', '蓝耗', '冷却', 'A杖'])
        self.comboModel = QStandardItemModel(0, 0)
        self.comboModel.setHorizontalHeaderLabels(['技能1', '技能2'])
        # 模型绑定表格
        ui.SkillTableView.setModel(self.skillModel)
        ui.ComboTableView.setModel(self.comboModel)

        # 获取预设的组合
        comboList = self.getComboList()

        # 图片处理

        ProcessImg.window_capture(num)  #截图
        ProcessImg.reviseImg()          # 梯形修正
        ProcessImg.extractIcon()        # 截取图标

        #图片识别，获取技能id列表

        skillIdList = MyOCR.getSkillIdList()
        #技能名列表
        skNameList = []

        #45个技能信息列表，顺便获取技能名列表
        skillList = self.getSkillInfo(skillIdList, skNameList)

        for sn in range(0, len(skillList)):
            skillPath = skillList[sn]['skIcon']
            skillName = skillList[sn]['skName']
            # print(skillName)
            skillIcon = QIcon(skillPath)
            skillItem = QStandardItem(skillIcon, '')
            self.skillModel.setItem(sn, 0, skillItem)
            nameItem = QStandardItem(skillName)
            self.skillModel.setItem(sn, 1, nameItem)





            if (skillList[sn]['manaCost'] == ''):
                pass
            else:
                skillMana = float(skillList[sn]['manaCost'])
                manaItem = QStandardItem()
                manaItem.setData(skillMana, Qt.DisplayRole)
                self.skillModel.setItem(sn, 2, manaItem)
                # print(skillMana)




            if (skillList[sn]['coolDown'] == ''):
                pass
            else:
                skillCD = float(skillList[sn]['coolDown'])
                CDItem = QStandardItem()
                CDItem.setData(skillCD, Qt.DisplayRole)
                self.skillModel.setItem(sn, 3, CDItem)
                # print(skillCD)

            if (skillList[sn]['Agha'] == 'Yes'):
                isAItem = QStandardItem(skillList[sn]['Agha'])
                self.skillModel.setItem(sn, 4, isAItem)


            # if (skillList[sn]['Info'] != ''):
            #     infoItem = QStandardItem(skillList[sn]['Info'])
            #     self.skillModel.setItem(sn, 5, infoItem)
            #
            # if (skillList[sn]['Tag'] != ''):
            #     tagItem = QStandardItem(skillList[sn]['Tag'])
            #     self.skillModel.setItem(sn, 6, tagItem)
            # ui.SkillTableView.setRowHeight(sn, 64)

        ui.SkillTableView.setColumnWidth(0, 140)
        ui.SkillTableView.setColumnWidth(1, 58)
        ui.SkillTableView.setColumnWidth(2, 58)
        ui.SkillTableView.setColumnWidth(3, 58)

        #combo表格
        count = 0
        for cbn in range(0, len(comboList)):

            if (set(comboList[cbn]) < set(skNameList)):
                for sk in skillList:
                    skillName = sk['skName']
                    skillPath = sk['skIcon']
                    skillIcon = QIcon(skillPath)
                    skillItem = QStandardItem(skillIcon, '')
                    ui.ComboTableView.setRowHeight(count, 64)
                    if (comboList[cbn][0] == skillName):
                        self.comboModel.setItem(count, 0, skillItem)
                    if (comboList[cbn][1] == skillName):
                        self.comboModel.setItem(count, 1, skillItem)
                count += 1

        ui.ComboTableView.setColumnWidth(0, 64)
        ui.ComboTableView.setColumnWidth(1, 64)
        QMessageBox.information(self, '提醒', '成功获取数据')

        ProcessImg.savePic(skillIdList)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    omg = OMG()
    omg.setWindowIcon(QIcon(Tools.LOGO_PATH))
    ui = UI.Ui_MainWidget()
    ui.setupUi(omg)
    omg.initUI()
    omg.show()
    sys.exit(app.exec_())
