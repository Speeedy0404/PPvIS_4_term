from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager

import garden
from garden_bed_and_trees import SeedBed, Orchard

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 800)


class ScreenManagerMy(ScreenManager):
    pass


screen_manager = ScreenManager()

screen_manager.add_widget(garden.Garden(name="screen_one"))


class ScreenApp(App):

    def build(self):
        return screen_manager


if __name__ == "__main__":
    sample_app = ScreenApp()
    SeedBed()
    Orchard()
    sample_app.run()
