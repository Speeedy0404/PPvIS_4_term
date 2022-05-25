import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import mvc


class Garden(Screen):
    collect = False
    weed = False
    water = False
    cure = False
    pests = False
    fertilizer = False
    seedlingsnew = False
    treenew = False
    seedlingsdel = False
    treedel = False
    info = False
    newday = False
    gui = True
    list = []
    list_fruits = []

    def show_info(self):
        mvc.Controller.on_press_show_info(self)

    def del_info(self):
        try:

            for i in range(len(Garden.list)):
                self.inffo.remove_widget(Garden.list[i])

            for i in range(len(Garden.list_fruits)):
                self.fruits.remove_widget(Garden.list_fruits[i])

            Garden.list.clear()
            Garden.list_fruits.clear()

        except IndexError:

            Garden.list.clear()
            Garden.list_fruits.clear()

    def next_day(self):
        mvc.Controller.on_press_next_day(self)

    def seedlings_new(self):
        mvc.Controller.on_press_seedlingsnew(self)

    def tree_new(self):
        mvc.Controller.on_press_treenew(self)

    def seedlings_del(self):
        mvc.Controller.on_press_seedlingsdel(self)

    def tree_del(self):
        mvc.Controller.on_press_treedel(self)

    def press_collect(self):
        mvc.Controller.on_press_collect(self)

    def press_weed(self):
        mvc.Controller.on_press_weed(self)

    def press_water(self):
        mvc.Controller.on_press_water(self)

    def press_cure(self):
        mvc.Controller.on_press_cure(self)

    def press_pests(self):
        mvc.Controller.on_press_pests(self)

    def press_fertilizer(self):
        mvc.Controller.on_press_fertilizer(self)


Builder.load_file(os.path.join(os.path.dirname(__file__), "garden.kv"))
