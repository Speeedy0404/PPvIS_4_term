import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import mvc


class Deletion(Screen):
    list_widget = []
    i_w = -1

    def remove_widgets(self):
        try:
            for i in range(0, Deletion.i_w + 1):
                self.del_info.remove_widget(Deletion.list_widget[i])
            Deletion.list_widget.clear()
            Deletion.i_w = -1
        except(IndexError):
            pass

    def add_widget_full_name(self):
        mvc.Controller.on_press_del_full_name(self)

    def add_widget_group(self):
        mvc.Controller.on_press_del_group(self)

    def add_widget_view(self):
        mvc.Controller.on_press_del_view(self)

    def add_widget_view_min_max(self):
        mvc.Controller.on_press_del_view_min_max(self)


Builder.load_file(os.path.join(os.path.dirname(__file__), "deletion.kv"))
