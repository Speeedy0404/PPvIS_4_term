import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import mvc


class AddingAnEntry(Screen):
    text = "Добавление произошло успешно"

    def change_status(self):
        self.status.text = AddingAnEntry.text
        AddingAnEntry.text = "Добавление произошло успешно"

    def add_student(self):
        mvc.Controller.on_press_add_student(self)


Builder.load_file(os.path.join(os.path.dirname(__file__), "adding_an_entry.kv"))
