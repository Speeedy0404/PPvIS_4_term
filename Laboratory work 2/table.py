import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import mvc
from parser import *


class Table(Screen):
    i_n = -1
    i_s = -1
    i_m = -1
    i_g = -1
    i_d = -1
    i_o = -1
    i_w = -1
    i_t = -1
    list = []
    all_page = int((globals.size_all / globals.size))
    this_page = 0

    def add_info(self):
        mvc.Controller.on_press_show_info(self)

    def del_info(self):
        try:
            for i in range(0, (globals.size * 6) + 6):
                self.info.remove_widget(Table.list[i])
            Table.list.clear()
        except(IndexError):
            pass

    @staticmethod
    def stabilization():
        Table.i_n = (Table.this_page * globals.size) - 1
        Table.i_s = (Table.this_page * globals.size) - 1
        Table.i_m = (Table.this_page * globals.size) - 1
        Table.i_g = (Table.this_page * globals.size) - 1
        Table.i_d = (Table.this_page * globals.size) - 1
        Table.i_o = (Table.this_page * globals.size) - 1
        Table.i_w = (Table.this_page * globals.size) - 1
        Table.i_t = (Table.this_page * globals.size) - 1

    def next_page(self):
        mvc.Controller.on_press_next_page()

    def previous_page(self):
        mvc.Controller.on_press_previous_page()

    def first_page(self):
        mvc.Controller.on_press_first_page()

    def last_page(self):
        mvc.Controller.on_press_last_page()


Builder.load_file(os.path.join(os.path.dirname(__file__), "table.kv"))
