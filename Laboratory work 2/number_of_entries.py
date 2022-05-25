import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import mvc


class NumberOfEntries(Screen):

    def change_the_nuber_of_entries(self):
        mvc.Controller.on_press_change_the_nuber_of_entries(self)


Builder.load_file(os.path.join(os.path.dirname(__file__), "number_of_entries.kv"))
