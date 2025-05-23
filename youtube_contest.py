#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout,QRadioButton, QMessageBox
#from numba import njit,prange,jit
import random
import time
import math
print('Libriry imported')
#@jit(nogil=True, fastmath=True, nopython=True)
def Rex(r):
    if(r <= 0):
        return 0
    else:
        b = 0
        for i in prange(r):
            if(Rex(r-1) != 0):
                b += Rex(r-1) + Rex(r-1) / Rex(r-1)
            else:
                b += Rex(r-1)
        #print('Rex()')
        return b

#@njit()
def cycle(r, a,b):
    for i in prange(r):
        a+=b
        for i in prange(r):
            a+=b
            for i in prange(r):
                a+=b
                for i in prange(r):
                    a+=b
                    for i in prange(r):
                        a+=b


    return a
timer = time.time()
#print(Rex(8))
print(time.time() - timer)

timer = time.time()
#print(cycle(10, 2,2))
print(time.time() - timer)

def ShowWin():
    victoryWindow = QMessageBox()
    window.setWindowTitle('SUS')
    window.resize(3500,2000)
    victoryWindow.setText('SUS')
    victoryWindow.exec()

def ShowLose():
    victoryWindow = QMessageBox()
    window.setWindowTitle('☺')
    window.resize(50,50)
    victoryWindow.setText('☻')
    victoryWindow.exec()

#создание приложения и главного окна
app = QApplication([])
window = QWidget()
window.setWindowTitle('Викторина')
window.resize(350,200)
#создание виджетов главного окна
 
text = QLabel('aSUS')
RButton1 = QRadioButton('AAA')
RButton1.clicked.connect(ShowLose)
RButton2 = QRadioButton('BBB')
RButton2.clicked.connect(ShowLose)
RButton3 = QRadioButton('LLL')
RButton3.clicked.connect(ShowLose)
RButton4 = QRadioButton('HeHeHiHa')
RButton4.clicked.connect(ShowWin)

VLine = QVBoxLayout()
HLine1 = QHBoxLayout()
HLine2 = QHBoxLayout()
HLine3 = QHBoxLayout()

HLine1.addWidget(text, alignment=Qt.AlignCenter)

HLine2.addWidget(RButton1, alignment=Qt.AlignCenter)
HLine2.addWidget(RButton2, alignment=Qt.AlignCenter)

HLine3.addWidget(RButton3, alignment=Qt.AlignCenter)
HLine3.addWidget(RButton4, alignment=Qt.AlignCenter)

VLine.addLayout(HLine1)
VLine.addLayout(HLine2)
VLine.addLayout(HLine3)

window.setLayout(VLine)
#расположение виджетов по лэйаутам

#обработка нажатий на переключатели
 
#отображение окна приложения 


window.show()
app.exec()
