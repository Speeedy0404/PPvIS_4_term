from kivy.uix.label import Label

import garden
from garden_area import GardenArea


class Controller:
    root = None

    @staticmethod
    def on_press_show_info(self):
        Controller.root = self
        garden.Garden.info = True
        Model.add_info_model()

    @staticmethod
    def on_press_next_day(self):
        Controller.root = self
        garden.Garden.newday = True
        Model.next_day_model()

    @staticmethod
    def on_press_seedlingsnew(self):
        Controller.root = self
        garden.Garden.seedlingsnew = True
        Model.get_on_press_seedlingsnew_model()

    @staticmethod
    def on_press_treenew(self):
        Controller.root = self
        garden.Garden.treenew = True
        Model.get_on_press_treenew_model()

    @staticmethod
    def on_press_seedlingsdel(self):
        Controller.root = self
        garden.Garden.seedlingsdel = True
        Model.get_on_press_seedlingsdel_model()

    @staticmethod
    def on_press_treedel(self):
        Controller.root = self
        garden.Garden.treedel = True
        Model.get_on_press_treedel_model()

    @staticmethod
    def on_press_collect(self):
        Controller.root = self
        garden.Garden.collect = True
        Model.get_on_press_collect_model()

    @staticmethod
    def on_press_weed(self):
        Controller.root = self
        garden.Garden.weed = True
        Model.get_on_press_weed_model()

    @staticmethod
    def on_press_water(self):
        Controller.root = self
        garden.Garden.water = True
        Model.get_on_press_water_model()

    @staticmethod
    def on_press_cure(self):
        Controller.root = self
        garden.Garden.cure = True
        Model.get_on_press_cure_model()

    @staticmethod
    def on_press_pests(self):
        Controller.root = self
        garden.Garden.pests = True
        Model.get_on_press_pests_model()

    @staticmethod
    def on_press_fertilizer(self):
        Controller.root = self
        garden.Garden.fertilizer = True
        Model.get_on_press_fertilizer_model()


class Model:

    @staticmethod
    def add_info_model():
        GardenArea.make_action("info", garden.Garden.gui, View.show_info_view)

    @staticmethod
    def next_day_model():
        GardenArea.make_action("new_day", garden.Garden.gui, View.show_next_day_view)

    @staticmethod
    def get_on_press_seedlingsnew_model():
        GardenArea.make_action("seedlings_new", garden.Garden.gui, View.show_status_view,
                               input_gui=Controller.root.seedlingsnew.text)

    @staticmethod
    def get_on_press_treenew_model():
        GardenArea.make_action("tree_new", garden.Garden.gui, View.show_status_view, input_gui=Controller.root.treenew.text)

    @staticmethod
    def get_on_press_seedlingsdel_model():
        GardenArea.make_action("seedlings_del", garden.Garden.gui, View.show_status_view,
                               input_gui=Controller.root.seedlingsdel.text)

    @staticmethod
    def get_on_press_treedel_model():
        GardenArea.make_action("tree_del", garden.Garden.gui, View.show_status_view,
                               input_gui=Controller.root.treedel.text)

    @staticmethod
    def get_on_press_collect_model():
        GardenArea.make_action("collect", garden.Garden.gui, View.show_status_view,
                               input_gui=Controller.root.collect.text)

    @staticmethod
    def get_on_press_weed_model():
        GardenArea.make_action("weed", garden.Garden.gui, View.show_status_view,
                               input_gui=Controller.root.weed.text)

    @staticmethod
    def get_on_press_water_model():
        GardenArea.make_action("water", garden.Garden.gui, View.show_status_view,
                               input_gui=Controller.root.water.text)

    @staticmethod
    def get_on_press_cure_model():
        GardenArea.make_action("cure", garden.Garden.gui, View.show_status_view,
                               input_gui=Controller.root.cure.text)

    @staticmethod
    def get_on_press_pests_model():
        GardenArea.make_action("pests", garden.Garden.gui, View.show_status_view,
                               input_gui=Controller.root.pests.text)

    @staticmethod
    def get_on_press_fertilizer_model():
        GardenArea.make_action("fertilizer", garden.Garden.gui, View.show_status_view,
                               input_gui=Controller.root.fertilizer.text)


class View:

    @staticmethod
    def show_info_view(name, weather, seed_bed_show_information_about_objects, seed_bed_status,
                       orchard_show_information_about_objects, orchard_status):
        vegetables = 0
        garden.Garden.list.append(Label(text='Садовый участок: {}'.format(name)))
        Controller.root.inffo.add_widget(garden.Garden.list[vegetables])
        vegetables += 1
        garden.Garden.list.append(Label(text='Погода {}'.format(weather.info_weather)))
        Controller.root.inffo.add_widget(garden.Garden.list[vegetables])

        seed_bed_show_information_about_objects(param=0, gui=garden.Garden.gui, root=Controller.root, list_object=garden.Garden.list,
                                                label=Label)
        seed_bed_status(param=0, gui=garden.Garden.gui, root=Controller.root, list_objects=garden.Garden.list, label=Label)
        orchard_show_information_about_objects(param=1, gui=garden.Garden.gui, root=Controller.root,
                                               list_object=garden.Garden.list_fruits,
                                               label=Label)
        orchard_status(param=1, gui=garden.Garden.gui, root=Controller.root, list_objects=garden.Garden.list_fruits, label=Label)
        garden.Garden.info = False

    @staticmethod
    def show_next_day_view(name, some_string):
        it = len(garden.Garden.list)
        garden.Garden.list.append(Label(text=name))
        Controller.root.inffo.add_widget(garden.Garden.list[it])
        it += 1
        garden.Garden.list.append(Label(text=some_string))
        Controller.root.inffo.add_widget(garden.Garden.list[it])
        garden.Garden.newday = False

    @staticmethod
    def show_status_view(some_string):
        Controller.root.status.text = some_string
        garden.Garden.collect = False
        garden.Garden.weed = False
        garden.Garden.water = False
        garden.Garden.cure = False
        garden.Garden.pests = False
        garden.Garden.fertilizer = False
        garden.Garden.seedlingsnew = False
        garden.Garden.treenew = False
        garden.Garden.seedlingsdel = False
        garden.Garden.treedel = False