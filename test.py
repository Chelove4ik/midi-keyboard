import sys
from os import walk
from time import clock

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QMainWindow

from Pydub_script import *

try:
    with open('num_sound.txt', 'r', encoding='utf8') as fnum_sound:
        num_sound = fnum_sound.read()
        if num_sound is '':
            num_sound = 1
        else:
            num_sound = int(num_sound)
            num_sound += 1
except Exception:
    num_sound = 1

list_of_song = []


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.start = False
        self.first_start = True

        self.sound_init(1)

        for i in self.tm:
            i.setStyleSheet("background-color: white")

        for button in self.tm:
            if self.tm[button][0] != 0:
                if clock() - self.tm[button][0] > 1:
                    button.setStyleSheet("background-color: white")

        self.pushButton_1.clicked.connect(lambda: self.sound_init(1))
        self.pushButton_2.clicked.connect(lambda: self.sound_init(2))
        self.pushButton_3.clicked.connect(lambda: self.sound_init(3))
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
        self.pushButton_start_record.clicked.connect(lambda: self.start_stop_record())

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
        elif event.key() == Qt.Key_1:
            self.sound_init(1)
        elif event.key() == Qt.Key_2:
            self.sound_init(2)
        elif event.key() == Qt.Key_3:
            self.sound_init(3)
        else:
            for but in self.tm:
                if self.tm[but][0] != 0:
                    if clock() - self.tm[but][0] > 0.1:
                        but.setStyleSheet("background-color: white")

    def run(self, button):
        self.tm[button][0] = clock()
        button.setStyleSheet("background-color: yellow")

        self.tm[button][1].play()

        if self.start and self.first_start:
            self.first_start = False
            self.st_time = clock()

        if self.start:
            list_of_song.append([self.tm[button][1].fileName(), clock() - self.st_time])

        for but in self.tm:
            if self.tm[but][0] != 0:
                if clock() - self.tm[but][0] > 0.1:
                    but.setStyleSheet("background-color: white")

    def start_stop_record(self):
        if not self.start:
            self.start = True
            self.pushButton_start_record.setStyleSheet("background-color: red")
        else:
            self.start = False
            self.pushButton_start_record.setStyleSheet("background-color: white")
            with open('num_sound.txt', 'w') as fnum_sound:
                fnum_sound.write(str(num_sound))
            try:
                start_create_wav(list_of_song[-1][1])
                for song, time in list_of_song:
                    sound_all(song, time)
                save_sound(num_sound)
            except Exception as ex:
                print(ex)
                pass

    def sound_init(self, num):
        f = []
        for (dirpath, dirnames, filenames) in walk('music/part{}'.format(num)):
            self.pyt = dirpath
            f.extend(filenames)
            break

        self.pushButton_1.setStyleSheet("background-color: white")
        self.pushButton_2.setStyleSheet("background-color: white")
        self.pushButton_3.setStyleSheet("background-color: white")

        if num == 1:
            self.pushButton_1.setStyleSheet("background-color: yellow")
        elif num == 2:
            self.pushButton_2.setStyleSheet("background-color: yellow")
        else:
            self.pushButton_3.setStyleSheet("background-color: yellow")

        zv_q, zv_w, zv_e, zv_r, zv_t, zv_y, zv_u, zv_i, zv_o, zv_p, zv_a, zv_s, zv_d = [None for _ in range(13)]
        zv_f, zv_g, zv_h, zv_j, zv_k, zv_l, zv_z, zv_x, zv_c, zv_v, zv_b, zv_n, zv_m = [None for _ in range(13)]

        try:
            zv_q, zv_w, zv_e, zv_r, zv_t, zv_y, zv_u, zv_i, zv_o, zv_p, zv_a, zv_s, zv_d = f[:13]
            zv_f, zv_g, zv_h, zv_j, zv_k, zv_l, zv_z, zv_x, zv_c, zv_v, zv_b, zv_n, zv_m = f[13:26]
        except Exception:
            print('Слишком мало семплов')
            exit(0)

        self.tm = {self.pushButton_q: [0, QSound('music/part{}/{}'.format(num, zv_q))],
                   self.pushButton_w: [0, QSound('music/part{}/{}'.format(num, zv_w))],
                   self.pushButton_e: [0, QSound('music/part{}/{}'.format(num, zv_e))],
                   self.pushButton_r: [0, QSound('music/part{}/{}'.format(num, zv_r))],
                   self.pushButton_t: [0, QSound('music/part{}/{}'.format(num, zv_t))],
                   self.pushButton_y: [0, QSound('music/part{}/{}'.format(num, zv_y))],
                   self.pushButton_u: [0, QSound('music/part{}/{}'.format(num, zv_u))],
                   self.pushButton_i: [0, QSound('music/part{}/{}'.format(num, zv_i))],
                   self.pushButton_o: [0, QSound('music/part{}/{}'.format(num, zv_o))],
                   self.pushButton_p: [0, QSound('music/part{}/{}'.format(num, zv_p))],
                   self.pushButton_a: [0, QSound('music/part{}/{}'.format(num, zv_a))],
                   self.pushButton_s: [0, QSound('music/part{}/{}'.format(num, zv_s))],
                   self.pushButton_d: [0, QSound('music/part{}/{}'.format(num, zv_d))],
                   self.pushButton_f: [0, QSound('music/part{}/{}'.format(num, zv_f))],
                   self.pushButton_g: [0, QSound('music/part{}/{}'.format(num, zv_g))],
                   self.pushButton_h: [0, QSound('music/part{}/{}'.format(num, zv_h))],
                   self.pushButton_j: [0, QSound('music/part{}/{}'.format(num, zv_j))],
                   self.pushButton_k: [0, QSound('music/part{}/{}'.format(num, zv_k))],
                   self.pushButton_l: [0, QSound('music/part{}/{}'.format(num, zv_l))],
                   self.pushButton_z: [0, QSound('music/part{}/{}'.format(num, zv_z))],
                   self.pushButton_x: [0, QSound('music/part{}/{}'.format(num, zv_x))],
                   self.pushButton_c: [0, QSound('music/part{}/{}'.format(num, zv_c))],
                   self.pushButton_v: [0, QSound('music/part{}/{}'.format(num, zv_v))],
                   self.pushButton_b: [0, QSound('music/part{}/{}'.format(num, zv_b))],
                   self.pushButton_n: [0, QSound('music/part{}/{}'.format(num, zv_n))],
                   self.pushButton_m: [0, QSound('music/part{}/{}'.format(num, zv_m))],
                   }


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
