from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from garden_area import GardenArea
from garden_bed_and_trees import SeedBed, Orchard

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 800)

from kivy.uix.textinput import TextInput

Builder.load_string('''
<ItemTextInput@TextInput>:
    multiline: False
    background_color: 'white'
    halign: 'left'
    cursor_blink: True
    cursor_color: 'black'
    foreground_color: 'black'
    font_size: '14'
<ItemButton@Button>:
    font_size: 12
    color: 'black'
    background_color: .32, .85, .94, 1
    background_normal: ''
<ItemLabel@Label>:
    color: 'white'
    halign:'center'
    valign:'middle'
    text_size:self.size

<Garden>:

    inffo:inffo
    fruits:fruits
    status:status
    
    collect:collect
    weed:weed
    water:water
    cure:cure
    pests:pests
    fertilizer:fertilizer
    seedlingsnew:seedlingsnew
    treenew:treenew
    seedlingsdel:seedlingsdel
    treedel:treedel
    
    FloatLayout:
        BoxLayout:
            id:inffo
            orientation: 'vertical'
            size_hint: .35, 0.95
            spacing:10
            padding:10
            pos:0,0
        
        BoxLayout:
            id:fruits
            orientation: 'vertical'
            size_hint: .35, .95
            spacing:10
            padding:10
            pos:465,0
                     
        ItemLabel:
            id:status
            text:' Статус'
            size_hint: .3, 0.1
            pos:630,720
        
        ItemButton:
            text:'Собрать рассаду/плоды'
            size: 170,50
            size_hint: None, None
            pos: 950,660
            on_press:
                root.del_info()
                root.press_collect()
                root.show_info()
        
        ItemTextInput: 
            id:collect
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 950,600
        
        ItemButton:
            text:'Прополоть'
            size: 170,50
            size_hint: None, None
            pos: 950,540
            on_press:
                root.del_info()
                root.press_weed()
                root.show_info()
        
        ItemTextInput: 
            id:weed
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 950,480
        
        ItemButton:
            text:'Полить'
            size: 170,50
            size_hint: None, None
            pos: 950,420
            on_press:
                root.del_info()
                root.press_water()
                root.show_info()
        
        ItemTextInput: 
            id:water
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 950,360
        
        ItemButton:
            text:'Вылечить'
            size: 170,50
            size_hint: None, None
            pos: 950,300
            on_press:
                root.del_info()
                root.press_cure()
                root.show_info()
        
        ItemTextInput: 
            id:cure
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 950,240
        
        ItemButton:
            text:'Избавиться от вредителей'
            size: 170,50
            size_hint: None, None
            pos: 950,180
            on_press:
                root.del_info()
                root.press_pests()
                root.show_info()
        
        ItemTextInput: 
            id:pests
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 950,120
        
        ItemButton:
            text:'Информация о участке'
            size: 170,50
            size_hint: None, None
            pos: 950,60
            on_press:
                root.del_info()
                root.show_info()
                
            
        ItemButton:
            text:'Использовать удобрение'
            size: 170,50
            size_hint: None, None
            pos: 1125,660
            on_press:
                root.del_info()
                root.press_fertilizer()
                root.show_info()
        
        ItemTextInput: 
            id:fertilizer
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 1125,600
        
        ItemButton:
            text:'Посадить новую рассаду'
            size: 170,50
            size_hint: None, None
            pos: 1125,540
            on_press:
                root.del_info()
                root.seedlings_new()
                root.show_info()
        
        ItemTextInput: 
            id:seedlingsnew
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 1125,480
        
        ItemButton:
            text:'Посадить новое дерево'
            size: 170,50
            size_hint: None, None
            pos: 1125,420
            on_press:
                root.del_info()
                root.tree_new()
                root.show_info()
        
        ItemTextInput: 
            id:treenew
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 1125,360
        
        ItemButton:
            text:'Выкопать рассаду'
            size: 170,50
            size_hint: None, None
            pos: 1125,300
            on_press:
                root.del_info()
                root.seedlings_del()
                root.show_info()
        
        ItemTextInput: 
            id:seedlingsdel
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 1125,240
        
        ItemButton:
            text:'Выкорчевать дерево'
            size: 170,50
            size_hint: None, None
            pos: 1125,180
            on_press:
                root.del_info()
                root.tree_del()
                root.show_info()
        
        ItemTextInput: 
            id:treedel
            hint_text:'Название'
            size: 170,50
            size_hint: None, None
            pos: 1125,120
        
        ItemButton:
            text:'Перейти к следующему дню'
            size: 170,50
            size_hint: None, None
            pos: 1125,60
            on_press:
                root.del_info()
                root.next_day()
''')


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
        Controller.on_press_show_info(self)

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
        Controller.on_press_next_day(self)

    def seedlings_new(self):
        Controller.on_press_seedlingsnew(self)

    def tree_new(self):
        Controller.on_press_treenew(self)

    def seedlings_del(self):
        Controller.on_press_seedlingsdel(self)

    def tree_del(self):
        Controller.on_press_treedel(self)

    def press_collect(self):
        Controller.on_press_collect(self)

    def press_weed(self):
        Controller.on_press_weed(self)

    def press_water(self):
        Controller.on_press_water(self)

    def press_cure(self):
        Controller.on_press_cure(self)

    def press_pests(self):
        Controller.on_press_pests(self)

    def press_fertilizer(self):
        Controller.on_press_fertilizer(self)


class Controller:
    root = None

    @staticmethod
    def on_press_show_info(self):
        Controller.root = self
        Garden.info = True
        Model.add_info_model()

    @staticmethod
    def on_press_next_day(self):
        Controller.root = self
        Garden.newday = True
        Model.next_day_model()

    @staticmethod
    def on_press_seedlingsnew(self):
        Controller.root = self
        Garden.seedlingsnew = True
        Model.get_on_press_seedlingsnew_model()

    @staticmethod
    def on_press_treenew(self):
        Controller.root = self
        Garden.treenew = True
        Model.get_on_press_treenew_model()

    @staticmethod
    def on_press_seedlingsdel(self):
        Controller.root = self
        Garden.seedlingsdel = True
        Model.get_on_press_seedlingsdel_model()

    @staticmethod
    def on_press_treedel(self):
        Controller.root = self
        Garden.treedel = True
        Model.get_on_press_treedel_model()

    @staticmethod
    def on_press_collect(self):
        Controller.root = self
        Garden.collect = True
        Model.get_on_press_collect_model()

    @staticmethod
    def on_press_weed(self):
        Controller.root = self
        Garden.weed = True
        Model.get_on_press_weed_model()

    @staticmethod
    def on_press_water(self):
        Controller.root = self
        Garden.water = True
        Model.get_on_press_water_model()

    @staticmethod
    def on_press_cure(self):
        Controller.root = self
        Garden.cure = True
        Model.get_on_press_cure_model()

    @staticmethod
    def on_press_pests(self):
        Controller.root = self
        Garden.pests = True
        Model.get_on_press_pests_model()

    @staticmethod
    def on_press_fertilizer(self):
        Controller.root = self
        Garden.fertilizer = True
        Model.get_on_press_fertilizer_model()


class Model:

    @staticmethod
    def add_info_model():
        GardenArea.make_action("info", Garden.gui, View.show_info_view)

    @staticmethod
    def next_day_model():
        GardenArea.make_action("new_day", Garden.gui, View.show_next_day_view)

    @staticmethod
    def get_on_press_seedlingsnew_model():
        GardenArea.make_action("seedlings_new", Garden.gui, View.show_status_view,
                               input_gui=Controller.root.seedlingsnew.text)

    @staticmethod
    def get_on_press_treenew_model():
        GardenArea.make_action("tree_new", Garden.gui, View.show_status_view, input_gui=Controller.root.treenew.text)

    @staticmethod
    def get_on_press_seedlingsdel_model():
        GardenArea.make_action("seedlings_del", Garden.gui, View.show_status_view,
                               input_gui=Controller.root.seedlingsdel.text)

    @staticmethod
    def get_on_press_treedel_model():
        GardenArea.make_action("tree_del", Garden.gui, View.show_status_view,
                               input_gui=Controller.root.treedel.text)

    @staticmethod
    def get_on_press_collect_model():
        GardenArea.make_action("collect", Garden.gui, View.show_status_view,
                               input_gui=Controller.root.collect.text)

    @staticmethod
    def get_on_press_weed_model():
        GardenArea.make_action("weed", Garden.gui, View.show_status_view,
                               input_gui=Controller.root.weed.text)

    @staticmethod
    def get_on_press_water_model():
        GardenArea.make_action("water", Garden.gui, View.show_status_view,
                               input_gui=Controller.root.water.text)

    @staticmethod
    def get_on_press_cure_model():
        GardenArea.make_action("cure", Garden.gui, View.show_status_view,
                               input_gui=Controller.root.cure.text)

    @staticmethod
    def get_on_press_pests_model():
        GardenArea.make_action("pests", Garden.gui, View.show_status_view,
                               input_gui=Controller.root.pests.text)

    @staticmethod
    def get_on_press_fertilizer_model():
        GardenArea.make_action("fertilizer", Garden.gui, View.show_status_view,
                               input_gui=Controller.root.fertilizer.text)


class View:

    @staticmethod
    def show_info_view(name, weather, seed_bed_show_information_about_objects, seed_bed_status,
                       orchard_show_information_about_objects, orchard_status):
        vegetables = 0
        Garden.list.append(Label(text='Садовый участок: {}'.format(name)))
        Controller.root.inffo.add_widget(Garden.list[vegetables])
        vegetables += 1
        Garden.list.append(Label(text='Погода {}'.format(weather.info_weather)))
        Controller.root.inffo.add_widget(Garden.list[vegetables])

        seed_bed_show_information_about_objects(param=0, gui=Garden.gui, root=Controller.root, list_object=Garden.list,
                                                label=Label)
        seed_bed_status(param=0, gui=Garden.gui, root=Controller.root, list_objects=Garden.list, label=Label)
        orchard_show_information_about_objects(param=1, gui=Garden.gui, root=Controller.root,
                                               list_object=Garden.list_fruits,
                                               label=Label)
        orchard_status(param=1, gui=Garden.gui, root=Controller.root, list_objects=Garden.list_fruits, label=Label)
        Garden.info = False

    @staticmethod
    def show_next_day_view(name, some_string):
        it = len(Garden.list)
        Garden.list.append(Label(text=name))
        Controller.root.inffo.add_widget(Garden.list[it])
        it += 1
        Garden.list.append(Label(text=some_string))
        Controller.root.inffo.add_widget(Garden.list[it])
        Garden.newday = False

    @staticmethod
    def show_status_view(some_string):
        Controller.root.status.text = some_string
        Garden.collect = False
        Garden.weed = False
        Garden.water = False
        Garden.cure = False
        Garden.pests = False
        Garden.fertilizer = False
        Garden.seedlingsnew = False
        Garden.treenew = False
        Garden.seedlingsdel = False
        Garden.treedel = False


class ScreenManagerMy(ScreenManager):
    pass


screen_manager = ScreenManager()

screen_manager.add_widget(Garden(name="screen_one"))


class ScreenApp(App):

    def build(self):
        return screen_manager


if __name__ == "__main__":
    sample_app = ScreenApp()
    SeedBed()
    Orchard()
    sample_app.run()
