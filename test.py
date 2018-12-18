import sys
import time
from os import walk

from append_music import append_music

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QMainWindow

f = []
for (dirpath, dirnames, filenames) in walk('music'):
    f.extend(filenames)
    break

try:
    zv_q, zv_w, zv_e, zv_r, zv_t, zv_y, zv_u, zv_i, zv_o, zv_p, zv_a, zv_s, zv_d = f[:13]
    zv_f, zv_g, zv_h, zv_j, zv_k, zv_l, zv_z, zv_x, zv_c, zv_v, zv_b, zv_n, zv_m = f[13:26]
except:
    print('Слишком мало семплов')
    exit(0)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.tm = {self.pushButton_q: [0, QSound('music\\{}'.format(zv_q))],
                   self.pushButton_w: [0, QSound('music\\{}'.format(zv_w))],
                   self.pushButton_e: [0, QSound('music\\{}'.format(zv_e))],
                   self.pushButton_r: [0, QSound('music\\{}'.format(zv_r))],
                   self.pushButton_t: [0, QSound('music\\{}'.format(zv_t))],
                   self.pushButton_y: [0, QSound('music\\{}'.format(zv_y))],
                   self.pushButton_u: [0, QSound('music\\{}'.format(zv_u))],
                   self.pushButton_i: [0, QSound('music\\{}'.format(zv_i))],
                   self.pushButton_o: [0, QSound('music\\{}'.format(zv_o))],
                   self.pushButton_p: [0, QSound('music\\{}'.format(zv_p))],
                   self.pushButton_a: [0, QSound('music\\{}'.format(zv_a))],
                   self.pushButton_s: [0, QSound('music\\{}'.format(zv_s))],
                   self.pushButton_d: [0, QSound('music\\{}'.format(zv_d))],
                   self.pushButton_f: [0, QSound('music\\{}'.format(zv_f))],
                   self.pushButton_g: [0, QSound('music\\{}'.format(zv_g))],
                   self.pushButton_h: [0, QSound('music\\{}'.format(zv_h))],
                   self.pushButton_j: [0, QSound('music\\{}'.format(zv_j))],
                   self.pushButton_k: [0, QSound('music\\{}'.format(zv_k))],
                   self.pushButton_l: [0, QSound('music\\{}'.format(zv_l))],
                   self.pushButton_z: [0, QSound('music\\{}'.format(zv_z))],
                   self.pushButton_x: [0, QSound('music\\{}'.format(zv_x))],
                   self.pushButton_c: [0, QSound('music\\{}'.format(zv_c))],
                   self.pushButton_v: [0, QSound('music\\{}'.format(zv_v))],
                   self.pushButton_b: [0, QSound('music\\{}'.format(zv_b))],
                   self.pushButton_n: [0, QSound('music\\{}'.format(zv_n))],
                   self.pushButton_m: [0, QSound('music\\{}'.format(zv_m))],
                   }

        for i in self.tm:
            i.setStyleSheet("background-color: white")

        for button in self.tm:
            if self.tm[button][0] != 0:
                if time.clock() - self.tm[button][0] > 1:
                    button.setStyleSheet("background-color: white")

        self.pushButton_q.clicked.connect(lambda: self.run(self.pushButton_q))
        self.pushButton_w.clicked.connect(lambda: self.run(self.pushButton_w))
        self.pushButton_e.clicked.connect(lambda: self.run(self.pushButton_e))
        self.pushButton_r.clicked.connect(lambda: self.run(self.pushButton_r))
        self.pushButton_t.clicked.connect(lambda: self.run(self.pushButton_t))
        self.pushButton_y.clicked.connect(lambda: self.run(self.pushButton_y))
        self.pushButton_u.clicked.connect(lambda: self.run(self.pushButton_u))
        self.pushButton_i.clicked.connect(lambda: self.run(self.pushButton_i))
        self.pushButton_o.clicked.connect(lambda: self.run(self.pushButton_o))
        self.pushButton_p.clicked.connect(lambda: self.run(self.pushButton_p))
        self.pushButton_a.clicked.connect(lambda: self.run(self.pushButton_a))
        self.pushButton_s.clicked.connect(lambda: self.run(self.pushButton_s))
        self.pushButton_d.clicked.connect(lambda: self.run(self.pushButton_d))
        self.pushButton_f.clicked.connect(lambda: self.run(self.pushButton_f))
        self.pushButton_g.clicked.connect(lambda: self.run(self.pushButton_g))
        self.pushButton_h.clicked.connect(lambda: self.run(self.pushButton_h))
        self.pushButton_j.clicked.connect(lambda: self.run(self.pushButton_j))
        self.pushButton_k.clicked.connect(lambda: self.run(self.pushButton_k))
        self.pushButton_l.clicked.connect(lambda: self.run(self.pushButton_l))
        self.pushButton_z.clicked.connect(lambda: self.run(self.pushButton_z))
        self.pushButton_x.clicked.connect(lambda: self.run(self.pushButton_x))
        self.pushButton_c.clicked.connect(lambda: self.run(self.pushButton_c))
        self.pushButton_v.clicked.connect(lambda: self.run(self.pushButton_v))
        self.pushButton_b.clicked.connect(lambda: self.run(self.pushButton_b))
        self.pushButton_n.clicked.connect(lambda: self.run(self.pushButton_n))
        self.pushButton_m.clicked.connect(lambda: self.run(self.pushButton_m))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.run(self.pushButton_q)
        elif event.key() == Qt.Key_W:
            self.run(self.pushButton_w)
        elif event.key() == Qt.Key_E:
            self.run(self.pushButton_e)
        elif event.key() == Qt.Key_R:
            self.run(self.pushButton_r)
        elif event.key() == Qt.Key_T:
            self.run(self.pushButton_t)
        elif event.key() == Qt.Key_Y:
            self.run(self.pushButton_y)
        elif event.key() == Qt.Key_U:
            self.run(self.pushButton_u)
        elif event.key() == Qt.Key_I:
            self.run(self.pushButton_i)
        elif event.key() == Qt.Key_O:
            self.run(self.pushButton_o)
        elif event.key() == Qt.Key_P:
            self.run(self.pushButton_p)
        elif event.key() == Qt.Key_A:
            self.run(self.pushButton_a)
        elif event.key() == Qt.Key_S:
            self.run(self.pushButton_s)
        elif event.key() == Qt.Key_D:
            self.run(self.pushButton_d)
        elif event.key() == Qt.Key_F:
            self.run(self.pushButton_f)
        elif event.key() == Qt.Key_G:
            self.run(self.pushButton_g)
        elif event.key() == Qt.Key_H:
            self.run(self.pushButton_h)
        elif event.key() == Qt.Key_J:
            self.run(self.pushButton_j)
        elif event.key() == Qt.Key_K:
            self.run(self.pushButton_k)
        elif event.key() == Qt.Key_L:
            self.run(self.pushButton_l)
        elif event.key() == Qt.Key_Z:
            self.run(self.pushButton_z)
        elif event.key() == Qt.Key_X:
            self.run(self.pushButton_x)
        elif event.key() == Qt.Key_C:
            self.run(self.pushButton_c)
        elif event.key() == Qt.Key_V:
            self.run(self.pushButton_v)
        elif event.key() == Qt.Key_B:
            self.run(self.pushButton_b)
        elif event.key() == Qt.Key_N:
            self.run(self.pushButton_n)
        elif event.key() == Qt.Key_M:
            self.run(self.pushButton_m)

    def run(self, button):
        self.tm[button][0] = time.clock()
        button.setStyleSheet("background-color: yellow")

        self.tm[button][1].play()

        append_music(self.tm[button][1].fileName())

        for but in self.tm:
            if self.tm[but][0] != 0:
                if time.clock() - self.tm[but][0] > 0.1:
                    but.setStyleSheet("background-color: white")


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
