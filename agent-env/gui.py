import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
import time
import csv

f = open('./Result/Result3.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
result_list = []
for line in rdr:
    result_list.append(line)
f.close()

del result_list[0]

i = 0
for i in range(len(result_list)):
    print(result_list[i])

#시간표 목록생성
test_list = []
i = 0
for i in range(len(result_list)):
    str1 = '%-4d'%i + result_list[i][0] + '     ' + result_list[i][4]
    test_list.append(str1)

#현재 시간표에 넣은 과목이름 저장
tmp_list = []

#현재 시간표에 넣은 과목들의 시간을 저장
#0이면 현재 시간에 과목이 아직 할당되지 않았음을 의미. 1이면 할당됨을 의미

class MyApp(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.list1 = ['                      ', '9시~10시', '10시~11시', '11시~12시', '12시~13시', '13시~14시', '14시~15시', '15시~16시', '16시~17시',
                      '17시~18시']
        self.list11 = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list111 = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list2 = ['월                                                        ', '', '', '', '', '', '', '', '', '']
        self.list22 = ['월', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list222 = ['월', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list3 = ['화                                                        ', '', '', '', '', '', '', '', '', '']
        self.list33 = ['화', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list333 = ['화', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list4 = ['수                                                        ', '', '', '', '', '', '', '', '', '']
        self.list44 = ['수', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list444 = ['수', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list5 = ['목                                                        ', '', '', '', '', '', '', '', '', '']
        self.list55 = ['목', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list555 = ['목', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list6 = ['금                                                        ', '', '', '', '', '', '', '', '', '']
        self.list66 = ['금', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.list666 = ['금', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        self.hbox = QHBoxLayout()

        self.initUI()

    def initUI(self):

        # 오른쪽 시간표 목록 불러오기
        self.list_widget = QtWidgets.QListWidget()
        options = test_list
        self.list_widget.addItems(options)
#        self.list_widget.itemClicked.connect(self.on_itemClicked)

        # 색 추가는 나중에
        # listt = ['color : green', 'color : red', 'color : blue']

        print("시간표 변경됨")

        i = 0
        for i in range(0, 10):
            self.list11[i] = QLabel(self.list1[i])
            self.list11[i].setFrameShape(QFrame.Box)

        i = 0
        for i in range(0, 10):
            self.list22[i] = QLabel(self.list2[i])
            self.list22[i].setFrameShape(QFrame.Box)

        i = 0
        for i in range(0, 10):
            self.list33[i] = QLabel(self.list3[i])
            self.list33[i].setFrameShape(QFrame.Box)

        i = 0
        for i in range(0, 10):
            self.list44[i] = QLabel(self.list4[i])
            self.list44[i].setFrameShape(QFrame.Box)

        i = 0
        for i in range(0, 10):
            self.list55[i] = QLabel(self.list5[i])
            self.list55[i].setFrameShape(QFrame.Box)

        i = 0
        for i in range(0, 10):
            self.list66[i] = QLabel(self.list6[i])
            self.list66[i].setFrameShape(QFrame.Box)

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(QLabel('시간표 목록                                                    '))
        splitter.addWidget(self.list_widget)

        splitter1 = QSplitter(Qt.Vertical)
        i = 0
        for i in range(0, 10):
            splitter1.addWidget(self.list11[i])

        splitter2 = QSplitter(Qt.Vertical)
        i = 0
        for i in range(0, 10):
            splitter2.addWidget(self.list22[i])

        splitter3 = QSplitter(Qt.Vertical)
        i = 0
        for i in range(0, 10):
            splitter3.addWidget(self.list33[i])

        splitter4 = QSplitter(Qt.Vertical)
        i = 0
        for i in range(0, 10):
            splitter4.addWidget(self.list44[i])

        splitter5 = QSplitter(Qt.Vertical)
        i = 0
        for i in range(0, 10):
            splitter5.addWidget(self.list55[i])

        splitter6 = QSplitter(Qt.Vertical)
        i = 0
        for i in range(0, 10):
            splitter6.addWidget(self.list66[i])

        splitter_result = QSplitter(Qt.Horizontal)
        splitter_result.addWidget(splitter)
        splitter_result.addWidget(splitter1)
        splitter_result.addWidget(splitter2)
        splitter_result.addWidget(splitter3)
        splitter_result.addWidget(splitter4)
        splitter_result.addWidget(splitter5)
        splitter_result.addWidget(splitter6)

        splitter_U = QSplitter(Qt.Vertical)
        splitter_U.addWidget(splitter_result)
        s = ['현재 신청한 과목 : ']
        i = 0
        for i in range(len(tmp_list)):
            s[0] = s[0] + str(tmp_list[i]) + '   '

        splitter_U.addWidget(QLabel(s[0]))



        self.hbox.addWidget(splitter_U)
        self.setLayout(self.hbox)
        self.list_widget.itemClicked.connect(self.on_itemClicked)

        self.setWindowTitle('시간표')
        self.setGeometry(300, 100, 800, 600)
        self.show()

    def NameErr(self):
        QMessageBox.about(self, "message", "같은 과목이 이미 들어있습니다.")

    def TimeErr(self):
        QMessageBox.about(self, "message", "다른 과목과 시간이 충돌됩니다.")


    @QtCore.pyqtSlot(QtWidgets.QListWidgetItem)
    def on_itemClicked(self, item):
        result_str = item.text()
        num = int(result_str[0] + result_str[1])

        #시작요일을 띄어쓰기로 나눠서 a리스트에 저장.
        a = []
        a = result_list[num][6].split(' ')
        #강의실을 '-'로 나눠서 b리스트에 저장.
        b = []
        b = result_list[num][5].split('-')

        #선택된 과목 정보 출력
        print(result_list[num])

        #선택된 과목의 이름을 tmp_list에 저장.
        tmp_list.append(result_list[num][0])
        #이름이 같은 과목 추가안됨. 작성중
        i = 0
        #과목이 두개 이상일때부터 체크
        if(len(tmp_list) > 1):
            for i in range(len(tmp_list)-1):
                if(tmp_list[i] == result_list[num][0]):
                    print("같은 이름의 과목이 이미 넣어져있음")
                    self.NameErr()
                    del tmp_list[-1]
                    #이미 이름이 같은 과목이 있으므로 0을 반환.
                    return 0

        # 요일이 하나 일때
        if (len(a) == 1):
            if (a[0][0] == self.list222[0][0]):
                i = 0
                for i in range(1, len(self.list222)):
                    if (a[0][1:] == self.list222[i]):
                        #현재 이 시간에 과목이 존재하는지 확인.
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            if(self.list2[i + j] != ''):
                                print("해당 시간에 이미 다른과목이 존재합니다.")
                                del tmp_list[-1]
                                self.TimeErr()
                                return 0
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            self.list2[i + j] = result_list[num][0] + '   ' + b[0]
                        break
            elif (a[0][0] == self.list333[0][0]):
                i = 0
                for i in range(1, len(self.list333)):
                    if (a[0][1:] == self.list333[i]):
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            if (self.list3[i + j] != ''):
                                print("해당 시간에 이미 다른과목이 존재합니다.")
                                del tmp_list[-1]
                                self.TimeErr()
                                return 0
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            self.list3[i + j] = result_list[num][0] + '   ' + b[0]
                        break
            elif (a[0][0] == self.list444[0][0]):
                i = 0
                for i in range(1, len(self.list444)):
                    if (a[0][1:] == self.list444[i]):
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            if (self.list4[i + j] != ''):
                                print("해당 시간에 이미 다른과목이 존재합니다.")
                                del tmp_list[-1]
                                self.TimeErr()
                                return 0
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            self.list4[i + j] = result_list[num][0] + '   ' + b[0]
                        break
            elif (a[0][0] == self.list555[0][0]):
                i = 0
                for i in range(1, len(self.list555)):
                    if (a[0][1:] == self.list555[i]):
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            if (self.list5[i + j] != ''):
                                print("해당 시간에 이미 다른과목이 존재합니다.")
                                del tmp_list[-1]
                                self.TimeErr()
                                return 0
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            self.list5[i + j] = result_list[num][0] + '   ' + b[0]
                        break
            elif (a[0][0] == self.list666[0][0]):
                i = 0
                for i in range(1, len(self.list666)):
                    if (a[0][1:] == self.list666[i]):
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            if (self.list6[i + j] != ''):
                                print("해당 시간에 이미 다른과목이 존재합니다.")
                                del tmp_list[-1]
                                self.TimeErr()
                                return 0
                        j = 0
                        for j in range(0, int(result_list[num][1])):
                            self.list6[i + j] = result_list[num][0] + '   ' + b[0]
                        break

        #요일이 두개 일때 해당 시간에 이미 다른과목이 있는지 검사
        if (len(a) == 2):
            k = 0
            for k in range(2):
                if(a[k][0] == self.list222[0][0]):
                    i = 0
                    for i in range(1, len(self.list222)):
                        if (a[k][1:] == self.list222[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1+k])):
                                if (self.list2[i + j] != ''):
                                    print("해당 시간에 이미 다른과목이 존재합니다.")
                                    del tmp_list[-1]
                                    self.TimeErr()
                                    return 0
            k = 0
            for k in range(2):
                if(a[k][0] == self.list333[0][0]):
                    i = 0
                    for i in range(1, len(self.list333)):
                        if (a[k][1:] == self.list333[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1 + k])):
                                if (self.list3[i + j] != ''):
                                    print("해당 시간에 이미 다른과목이 존재합니다.")
                                    del tmp_list[-1]
                                    self.TimeErr()
                                    return 0
            k = 0
            for k in range(2):
                if(a[k][0] == self.list444[0][0]):
                    i = 0
                    for i in range(1, len(self.list444)):
                        if (a[k][1:] == self.list444[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1 + k])):
                                if (self.list4[i + j] != ''):
                                    print("해당 시간에 이미 다른과목이 존재합니다.")
                                    del tmp_list[-1]
                                    self.TimeErr()
                                    return 0
            k = 0
            for k in range(2):
                if(a[k][0] == self.list555[0][0]):
                    i = 0
                    for i in range(1, len(self.list555)):
                        if (a[k][1:] == self.list555[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1 + k])):
                                if (self.list5[i + j] != ''):
                                    print("해당 시간에 이미 다른과목이 존재합니다.")
                                    del tmp_list[-1]
                                    self.TimeErr()
                                    return 0
            k = 0
            for k in range(2):
                if(a[k][0] == self.list666[0][0]):
                    i = 0
                    for i in range(1, len(self.list666)):
                        if (a[k][1:] == self.list666[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1 + k])):
                                if (self.list6[i + j] != ''):
                                    print("해당 시간에 이미 다른과목이 존재합니다.")
                                    del tmp_list[-1]
                                    self.TimeErr()
                                    return 0


        # 요일이 두개 일때
        if (len(a) == 2):
            k = 0
            for k in range(2):
                if(a[k][0] == self.list222[0][0]):
                    i = 0
                    for i in range(1, len(self.list222)):
                        if (a[k][1:] == self.list222[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1+k])):
                                self.list2[i + j] = result_list[num][0] + '   ' + b[k]
                            break
            k = 0
            for k in range(2):
                if(a[k][0] == self.list333[0][0]):
                    i = 0
                    for i in range(1, len(self.list333)):
                        if (a[k][1:] == self.list333[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1 + k])):
                                self.list3[i + j] = result_list[num][0] + '   ' + b[k]
                            break
            k = 0
            for k in range(2):
                if(a[k][0] == self.list444[0][0]):
                    i = 0
                    for i in range(1, len(self.list444)):
                        if (a[k][1:] == self.list444[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1 + k])):
                                self.list4[i + j] = result_list[num][0] + '   ' + b[k]
                            break
            k = 0
            for k in range(2):
                if(a[k][0] == self.list555[0][0]):
                    i = 0
                    for i in range(1, len(self.list555)):
                        if (a[k][1:] == self.list555[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1 + k])):
                                self.list5[i + j] = result_list[num][0] + '   ' + b[k]
                            break
            k = 0
            for k in range(2):
                if(a[k][0] == self.list666[0][0]):
                    i = 0
                    for i in range(1, len(self.list666)):
                        if (a[k][1:] == self.list666[i]):
                            j = 0
                            for j in range(0, int(result_list[num][1 + k])):
                                self.list6[i + j] = result_list[num][0] + '   ' + b[k]
                            break


        print("데이터 넣기 완료")
        self.clearLayout(self.hbox)
        self.show()
        self.initUI()


    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    # app = QApplication(sys.argv)
    # ex = MyApp()
    # sys.exit(app.exec_())