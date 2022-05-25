import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import mvc


class Search(Screen):
    list_info = []
    i_i = -1
    list_widget = []
    i_w = -1

    def remove_widgets(self):
        try:
            for i in range(0, Search.i_w + 1):
                self.search.remove_widget(Search.list_widget[i])
            Search.list_widget.clear()
            Search.i_w = -1
        except(IndexError):
            pass

    def remove_widgets_info(self):
        try:
            for i in range(0, Search.i_i + 1):
                self.info.remove_widget(Search.list_info[i])
            Search.list_info.clear()
            Search.i_i = -1
        except(IndexError):
            pass

    def add_widget_full_name(self):
        mvc.Controller.on_press_by_full_name(self)

    def add_widget_group(self):
        mvc.Controller.on_press_by_group(self)

    def add_widget_view(self):
        mvc.Controller.on_press_by_view(self)

    def add_widget_view_min_max(self):
        mvc.Controller.on_press_by_view_min_max(self)


Builder.load_file(os.path.join(os.path.dirname(__file__), "search.kv"))
