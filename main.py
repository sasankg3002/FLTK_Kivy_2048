# Written by GUNDABATHULA SASANK
# GAME 2048 CODE main.py


from kivy.app import App
from kivy.properties import StringProperty, ListProperty, BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
import copy
import random
from math import log2
import pickle


class MainWidget(BoxLayout):
    color = [[1, 204 / 255, 104 / 255, 1], [1, 1, 0, 1], [0.3, 0.4, 1, 1], [0.8, 0, 0.5, 1], [0.2, 1, 1, 1],
             [102 / 255, 255 / 255, 102 / 255, 1], [0, 0, 1, 1], [1, 0, 0, 1], [1, 102 / 255, 1, 1],
             [1, 102 / 255, 0, 1], [153 / 255, 153 / 255, 1, 1], [204 / 255, 1, 1, 1]]
    color_G = [0, 1, 0, 1]
    color_R = [1, 0, 0, 1]
    color_Y = [1, 1, 0, 1]
    text = StringProperty("2048")
    l = ListProperty([' '] * 16)
    l1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    c = ListProperty([[1, 204 / 255, 104 / 255, 1]] * 16)
    init = BooleanProperty(True)
    init_start = BooleanProperty(True)
    Text_start = StringProperty("START")
    Text_indicator = StringProperty('')
    color_indicator = ListProperty([0, 0, 0, 1])
    score = NumericProperty(0)
    text_input_str = StringProperty("ENTER YOUR NAME")
    txt_disabled = BooleanProperty(False)
    text_name = ListProperty([""] * 3)
    text_s = ListProperty([""] * 3)
    starting = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        file_to_read = open("scores.txt", "rb")
        self.diction = dict(pickle.load(file_to_read))
        file_to_read.close()
        j = 0
        for i in self.diction.keys():
            self.text_s[j] = str(i)
            j += 1
        for i in range(3):
            self.text_name[i] = self.diction.get(int(self.text_s[i]))

    def start_board(self):
        self.addnew()
        self.update_l()
        self.update_color()

    def start_game(self):
        if self.init:
            self.Text_indicator = " PLAY NOW"
            self.color_indicator = self.color_G
            self.l1 = [0] * 16
            self.text_name = [""] * 3
            self.text_s = [""] * 3
            if self.starting:
                j = 0
                for i in self.diction.keys():
                    self.text_s[j] = str(i)
                    j += 1
                for i in range(3):
                    self.text_name[i] = self.diction.get(int(self.text_s[i]))
                self.starting = False
            else:
                j = 0
                for i in self.d.keys():
                    self.text_s[j] = str(i)
                    j += 1
                for i in range(3):
                    self.text_name[i] = self.d.get(int(self.text_s[i]))
            self.start_board()
            self.init = False
            self.init_start = True

    def restart(self):
        self.score = 0
        self.Text_start = "RESTART"
        self.init_start = False
        self.init = True

    def on_merge_left(self):
        if self.mergeL():
            self.Text_indicator = "VALID MOVE"
            self.color_indicator = self.color_G
            self.l1 = self.l2
            self.addnew()
            self.update_l()
            self.update_color()
            self.check_won()
        elif self.check_game_over():
            print("GAME OVER")
            return True

        else:
            self.Text_indicator = "WRONG MOVE"
            self.color_indicator = self.color_Y
            print("Try another Command.")
            print("Merging to Left is not possible.")
            print("---------------------------------")

    def on_merge_up(self):
        if self.mergeU():
            self.Text_indicator = "VALID MOVE"
            self.color_indicator = self.color_G
            self.l1 = self.l2
            self.addnew()
            self.update_l()
            self.update_color()
            self.check_won()
        elif self.check_game_over():
            print("GAME OVER")
            return True
        else:
            self.Text_indicator = "WRONG MOVE"
            self.color_indicator = self.color_Y
            print("Try another Command.")
            print("Merging to Up is not possible.")
            print("---------------------------------")

    def on_merge_down(self):
        if self.mergeD():
            self.Text_indicator = "VALID MOVE"
            self.color_indicator = self.color_G
            self.l1 = self.l2
            self.addnew()
            self.update_l()
            self.update_color()
            self.check_won()
        elif self.check_game_over():
            print("GAME OVER")
            return True
        else:
            self.Text_indicator = "WRONG MOVE"
            self.color_indicator = self.color_Y
            print("Try another Command.")
            print("Merging to Down is not possible.")
            print("---------------------------------")

    def on_merge_right(self):
        if self.mergeR():
            self.Text_indicator = "VALID MOVE"
            self.color_indicator = self.color_G
            self.l1 = self.l2
            self.addnew()
            self.update_l()
            self.update_color()
            self.check_won()
        elif self.check_game_over():
            print("GAME OVER")
            return True
        else:
            self.Text_indicator = "WRONG MOVE"
            self.color_indicator = self.color_Y
            print("Try another Command.")
            print("Merging to Right is not possible.")
            print("---------------------------------")

    def mergeL(self):
        l2 = copy.deepcopy(self.l1)
        for i in range(0, 16, 4):
            for k in range(3):
                for j in range(3, 0, -1):
                    if l2[i + j - 1] == 0:
                        l2[i + j - 1] = l2[i + j]
                        l2[i + j] = 0
            for j in range(3):
                if l2[i + j] == l2[i + j + 1]:
                    l2[i + j] *= 2
                    l2[i + j + 1] = 0
            for j in range(3, 0, -1):
                if l2[i + j - 1] == 0:
                    l2[i + j - 1] = l2[i + j]
                    l2[i + j] = 0
        if l2 == self.l1:
            return False
        else:
            self.l2 = l2
            return True

    def mergeU(self):
        l2 = copy.deepcopy(self.l1)
        for i in range(4):
            for k in range(3):
                for j in range(12, 0, -4):
                    if l2[i + j - 4] == 0:
                        l2[i + j - 4] = l2[i + j]
                        l2[i + j] = 0
            for j in range(0, 12, 4):
                if l2[i + j] == l2[i + j + 4]:
                    l2[i + j] *= 2
                    l2[i + j + 4] = 0
            for j in range(12, 0, -4):
                if l2[i + j - 4] == 0:
                    l2[i + j - 4] = l2[i + j]
                    l2[i + j] = 0
        if l2 == self.l1:
            return False
        else:
            self.l2 = l2
            return True

    def mergeD(self):
        l2 = copy.deepcopy(self.l1)
        for i in range(4):
            for k in range(3):
                for j in range(0, 12, 4):
                    if l2[i + j + 4] == 0:
                        l2[i + j + 4] = l2[i + j]
                        l2[i + j] = 0
            for j in range(12, 0, -4):
                if l2[i + j] == l2[i + j - 4]:
                    l2[i + j] *= 2
                    l2[i + j - 4] = 0
            for j in range(0, 12, 4):
                if l2[i + j + 4] == 0:
                    l2[i + j + 4] = l2[i + j]
                    l2[i + j] = 0
        if l2 == self.l1:
            return False
        else:
            self.l2 = l2
            return True

    def mergeR(self):
        l2 = copy.deepcopy(self.l1)
        for i in range(0, 16, 4):
            for k in range(3):
                for j in range(3):
                    if l2[i + j + 1] == 0:
                        l2[i + j + 1] = l2[i + j]
                        l2[i + j] = 0
            for j in range(3, 0, -1):
                if l2[i + j] == l2[i + j - 1]:
                    l2[i + j] *= 2
                    l2[i + j - 1] = 0
            for j in range(3):
                if l2[i + j + 1] == 0:
                    l2[i + j + 1] = l2[i + j]
                    l2[i + j] = 0
        if l2 == self.l1:
            return False
        else:
            self.l2 = l2
            return True

    def addnew(self):
        i = 1
        while i > 0:
            j = random.randint(0, 15)
            if self.l1[j] == 0:
                self.l1[j] = self.randv()
                i = i - 1

    def randv(self):
        if random.randint(1, 8) == 1:
            self.score += 4
            return 4
        else:
            self.score += 2
            return 2

    def update_l(self):
        for i in range(16):
            if self.l1[i] == 0:
                self.l[i] = ""
            else:
                self.l[i] = str(self.l1[i])

    def update_color(self):
        for i in range(16):
            if self.l1[i] == 0:
                self.c[i] = self.color[0]
            else:
                self.c[i] = self.color[int(log2(self.l1[i]))]

    def check_won(self):
        for i in range(16):
            if self.l1[i] == 2048:
                self.Text_indicator = "YOU WON"
                self.color_indicator = self.color_G
                self.add_to_top3()
                self.restart()

    def check_game_over(self):
        if self.mergeL() or self.mergeD() or self.mergeU() or self.mergeR():
            return False
        else:
            self.Text_indicator = "GAME OVER"
            self.color_indicator = self.color_Y
            self.add_to_top3()
            self.restart()
            return True

    def on_button_start_click(self):
        pass

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        self.init_start = False
        self.txt_disabled = True

    def add_to_top3(self):

        d = {self.score: self.text_input_str}
        self.diction[self.score] = self.text_input_str
        self.l3 = list(self.diction.keys())
        self.l3.append(0)
        self.l3.sort()
        self.d = {}
        for i in range(3):
            self.d[self.l3[len(self.l3) - 1 - i]] = self.diction.get(self.l3[len(self.l3) - 1 - i])
        self.filehandler = open("scores.txt", "wb")
        pickle.dump(self.d, self.filehandler)
        self.filehandler.close()


class Game2048App(App):
    pass


Game2048App().run()
