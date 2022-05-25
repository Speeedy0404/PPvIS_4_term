from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 800)

import adding_an_entry
import deletion
import file_selection
import number_of_entries
import search
import table


# ScreenManager управляет перемещением между экранами
class ScreenManagerMy(ScreenManager):
    pass


screen_manager = ScreenManager()

# Добавьте экраны к менеджеру, а затем укажите имя
# используется для переключения экранов

screen_manager.add_widget(table.Table(name="screen_one"))

screen_manager.add_widget(adding_an_entry.AddingAnEntry(name="screen_two"))

screen_manager.add_widget(number_of_entries.NumberOfEntries(name="screen_three"))

screen_manager.add_widget(search.Search(name="screen_four"))

screen_manager.add_widget(deletion.Deletion(name="screen_five"))

screen_manager.add_widget(file_selection.FileSelection(name="screen_six"))


# Создать класс приложения

class ScreenApp(App):

    def build(self):
        return screen_manager


# запустить приложение
if __name__ == "__main__":
    sample_app = ScreenApp()

    sample_app.run()
