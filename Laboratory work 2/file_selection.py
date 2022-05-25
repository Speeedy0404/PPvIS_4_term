import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import mvc


class FileSelection(Screen):
    list = []
    i_t = -1
    list_file = []

    def remove_widgets(self):
        try:
            for i in range(0, FileSelection.i_t + 1):
                self.file.remove_widget(FileSelection.list[i])
            FileSelection.list.clear()
            FileSelection.i_t = -1
        except(IndexError):
            pass

    def choice(self):
        mvc.Controller.on_press_chose_file(self)

    def show_file(self):
        mvc.Controller.on_press_show_file(self)


Builder.load_file(os.path.join(os.path.dirname(__file__), "file_selection.kv"))
