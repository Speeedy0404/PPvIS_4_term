from actions import *
from Weather import *
from garden_bed_and_trees import *
from view_cli import *
from dictionary import dictionary


class GardenArea:

    @staticmethod
    def make_action(action_name: str, gui=False, show_status_view=None, input_gui=None):
        action = action_map.get(action_name)
        if action_name.__eq__("info") or action_name.__eq__("new_day"):
            action(gui, show_status_view)
        else:
            action(gui, show_status_view, input_gui)

    @staticmethod
    def collection(gui=False, show_status_view=None, input_gui=None) -> None:
        object_of_the_plot: str = input_gui
        if gui:
            try:
                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_height(position_of_vegetable, param=0) == dictionary.get("fruit_is_ripe"):
                    show_status_view("Рассада успешно собрана")
                    SeedBed.deleting_information(position_of_vegetable, param=0)
                else:
                    show_status_view("Эта рассада еще не выросла")

                if position_of_fruit is None:
                    pass
                elif Orchard.check_height(position_of_fruit, param=1) == "Период плодоношения":
                    show_status_view("Плоды дерева успешно собраны")
                    Orchard.deleting_information(position_of_fruit, param=1)
                else:
                    show_status_view("Это дерево еще не созрело")

            except NameError:
                show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке ")

        else:
            try:
                object_of_the_plot: str = input("Какую рассаду или плоды дерева которые вы хотите собрать? -> ")

                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_height(position_of_vegetable, param=0) == "Плод созрел":
                    ViewPrint.show_status_view("---------------------------------------", "Рассада успешно собрана",
                                               "---------------------------------------")
                    SeedBed.deleting_information(position_of_vegetable, param=0)
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Эта рассада еще не выросла",
                                               "---------------------------------------")
                if position_of_fruit is None:
                    pass
                elif Orchard.check_height(position_of_fruit, param=1) == "Период плодоношения":
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Плоды дерева успешно собраны",
                                               "---------------------------------------")
                    Orchard.deleting_information(position_of_fruit, param=1)
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Это дерево еще не созрело",
                                               "---------------------------------------")

            except NameError:
                ViewPrint.show_status_view("---------------------------------------",
                                           "Вы должны выбрать рассаду или дерево которые растут на вашем участке",
                                           "---------------------------------------")

    @staticmethod
    def weeding_seedlings(gui=False, show_status_view=None, input_gui=None) -> None:
        weeding = Weeding()
        if gui:
            try:
                object_of_the_plot: str = input_gui
                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)

                if position_of_vegetable is None:
                    raise NameError

                if SeedBed.check_weeds(position_of_vegetable) == 0:
                    show_status_view("Этой рассаде прополка не требуется")
                else:
                    weeding.using_actions(gui, show_status_view)
                    SeedBed.regeneration_weeds(position_of_vegetable, param=0)

            except NameError:
                show_status_view("Вы должны выбрать рассаду которая растёт на вашем участке")

        elif gui is False:
            try:
                object_of_the_plot: str = input("Какую рассаду вы хотите прополоть? -> ")

                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)

                if position_of_vegetable is None:
                    raise NameError

                if SeedBed.check_weeds(position_of_vegetable) == 0:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Этой рассаде прополка не требуется",
                                               "---------------------------------------")
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "",
                                               "---------------------------------------")
                    weeding.using_actions()
                    SeedBed.regeneration_weeds(position_of_vegetable, param=0)

            except NameError:
                ViewPrint.show_status_view("---------------------------------------",
                                           "Вы должны выбрать рассаду которая растёт на вашем участке",
                                           "---------------------------------------")

    @staticmethod
    def watering_the_garden_plot(gui=False, show_status_view=None, input_gui=None) -> None:
        watering = Watering()
        object_of_the_plot: str = input_gui
        if gui:
            try:
                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_level_of_water(position_of_vegetable, param=0) == 0:
                    show_status_view("Этой рассаде поливка не требуется. Земля полностью пропитана водой")
                else:
                    watering.using_actions(gui, show_status_view)
                    SeedBed.regenerate_level_of_water(position_of_vegetable,
                                                      SeedBed.check_level_of_water(position_of_vegetable, param=0),
                                                      param=0)

                if position_of_fruit is None:
                    pass
                elif Orchard.check_level_of_water(position_of_fruit, param=1) == 0:
                    show_status_view("Этому дереву поливка не требуется. Земля полностью пропитана водой")
                else:
                    watering.using_actions(gui, show_status_view)
                    Orchard.regenerate_level_of_water(position_of_fruit,
                                                      Orchard.check_level_of_water(position_of_fruit, param=1),
                                                      param=1)

            except NameError:
                show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")

        elif gui is False:
            try:
                object_of_the_plot: str = input("Какую рассаду или дерево вы хотите полить? -> ")

                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_level_of_water(position_of_vegetable, param=0) == 0:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Этой рассаде поливка не требуется. Земля полностью пропитана водой",
                                               "---------------------------------------")
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "",
                                               "---------------------------------------")
                    watering.using_actions()
                    SeedBed.regenerate_level_of_water(position_of_vegetable,
                                                      SeedBed.check_level_of_water(position_of_vegetable, param=0),
                                                      param=0)

                if position_of_fruit is None:
                    pass
                elif Orchard.check_level_of_water(position_of_fruit, param=1) == 0:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Этому дереву поливка не требуется. Земля полностью пропитана водой",
                                               "---------------------------------------")
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "",
                                               "---------------------------------------")

                    watering.using_actions()
                    Orchard.regenerate_level_of_water(position_of_fruit,
                                                      Orchard.check_level_of_water(position_of_fruit, param=1),
                                                      param=1)

            except NameError:
                ViewPrint.show_status_view("---------------------------------------",
                                           "Вы должны выбрать рассаду или дерево которые растут на вашем участке",
                                           "---------------------------------------")

    @staticmethod
    def cure_something_in_a_garden_plot(gui=False, show_status_view=None, input_gui=None) -> None:
        object_of_the_plot: str = input_gui
        if gui:
            try:
                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_illness(position_of_vegetable, param=0) == 0:
                    show_status_view("Этой рассаде лечение не требуется")
                else:
                    show_status_view("Рассада успешно вылечена")
                    SeedBed.regeneration_illness(position_of_vegetable, param=0)

                if position_of_fruit is None:
                    pass
                elif Orchard.check_illness(position_of_fruit, param=1) == 0:
                    show_status_view("Этому дереву лечение не требуется")
                else:
                    show_status_view("Дерево успешно вылечено")
                    Orchard.regeneration_illness(position_of_fruit, param=1)

            except NameError:
                show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")
        else:
            try:
                object_of_the_plot: str = input("Какую рассаду или дерево вы хотите вылечить? -> ")
                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_illness(position_of_vegetable, param=0) == 0:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Этой рассаде лечение не требуется",
                                               "---------------------------------------")
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Рассада успешно вылечена",
                                               "---------------------------------------")
                    SeedBed.regeneration_illness(position_of_vegetable, param=0)

                if position_of_fruit is None:
                    pass
                elif Orchard.check_illness(position_of_fruit, param=1) == 0:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Этому дереву лечение не требуется",
                                               "---------------------------------------")
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Дерево успешно вылечено",
                                               "---------------------------------------")
                    Orchard.regeneration_illness(position_of_fruit, param=1)

            except NameError:
                ViewPrint.show_status_view("---------------------------------------",
                                           "Вы должны выбрать рассаду или дерево которые растут на вашем участке",
                                           "---------------------------------------")

    @staticmethod
    def get_rid_of_pests(gui=False, show_status_view=None, input_gui=None) -> None:
        object_of_the_plot: str = input_gui
        if gui:
            try:
                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_vermin(position_of_vegetable, param=0) == 0:
                    show_status_view("Этой рассаде не требуется избавление от вредителей")
                else:
                    show_status_view("Рассада успешно избавлена от вредителей")
                    SeedBed.regeneration_vermin(position_of_vegetable, param=0)

                if position_of_fruit is None:
                    pass
                elif Orchard.check_vermin(position_of_fruit, param=1) == 0:
                    show_status_view("Этому дереву не требуется избавление от вредителей")
                else:
                    show_status_view("Дерево успешно избавдено от вредителей")
                    Orchard.regeneration_vermin(position_of_fruit, param=1)

            except NameError:
                show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")
        else:
            try:
                object_of_the_plot: str = input("Какую рассаду или дерево вы хотите избавить от вредителей? -> ")

                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_vermin(position_of_vegetable, param=0) == 0:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Этой рассаде не требуется избавление от вредителей",
                                               "---------------------------------------")
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Рассада успешно избавлена от вредителей",
                                               "---------------------------------------")
                    SeedBed.regeneration_vermin(position_of_vegetable, param=0)

                if position_of_fruit is None:
                    pass
                elif Orchard.check_vermin(position_of_fruit, param=1) == 0:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Этому дереву не требуется избавление от вредителей",
                                               "---------------------------------------")
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Дерево успешно избавлено от вредителей",
                                               "---------------------------------------")
                    Orchard.regeneration_vermin(position_of_fruit, param=1)

            except NameError:
                ViewPrint.show_status_view("---------------------------------------",
                                           "Вы должны выбрать рассаду или дерево которые растут на вашем участке",
                                           "---------------------------------------")

    @staticmethod
    def use_fertilizer(gui=False, show_status_view=None, input_gui=None) -> None:
        fertilizer = Fertilizer()
        if gui:
            try:
                object_of_the_plot: str = input_gui
                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_height(position_of_vegetable, param=0) == "Плод созрел":

                    show_status_view("Рассада уже созрела и не нуждаеться в удобрении")

                else:

                    fertilizer.using_actions(gui, show_status_view)
                    SeedBed.change_height(position_of_vegetable, param=0)

                if position_of_fruit is None:
                    pass
                elif Orchard.check_height(position_of_fruit, param=1) == "Период плодоношения":

                    show_status_view("Плоды дерева уже созрели. Дерево не нуждаеться в удобрении")

                else:

                    fertilizer.using_actions(gui, show_status_view)
                    Orchard.change_height(position_of_fruit, param=1)

            except NameError:
                show_status_view(dictionary["no_name"])
        else:
            try:
                object_of_the_plot: str = input("Какую рассаду или дерево вы хотите удобрить? -> ")

                position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
                position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

                if position_of_vegetable is None and position_of_fruit is None:
                    raise NameError

                if position_of_vegetable is None:
                    pass
                elif SeedBed.check_height(position_of_vegetable, param=0) == "Плод созрел":
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Рассада уже созрела и не нуждаеться в удобрении",
                                               "---------------------------------------")
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "",
                                               "---------------------------------------")
                    fertilizer.using_actions()
                    SeedBed.change_height(position_of_vegetable, param=0)

                if position_of_fruit is None:
                    pass
                elif Orchard.check_height(position_of_fruit, param=1) == "Период плодоношения":
                    ViewPrint.show_status_view("---------------------------------------",
                                               "Плоды дерева уже созрели. Дерево не нуждаеться в удобрении",
                                               "---------------------------------------")
                else:
                    ViewPrint.show_status_view("---------------------------------------",
                                               "",
                                               "---------------------------------------")
                    fertilizer.using_actions()
                    Orchard.change_height(position_of_fruit, param=1)

            except NameError:
                ViewPrint.show_status_view(dictionary["line"], dictionary["no_name"], dictionary["line"])

    @staticmethod
    def garden_plot_next_day(gui=False, show_next_day_view=ViewPrint.show_next_day_view) -> None:
        weather = Weather()
        weather.changing_the_weather()
        garden = SeedBed()
        trees = Orchard()
        garden.change_of_day(param=0, show_next_day_view=show_next_day_view, gui=gui)
        SeedBed.changing_the_water_from_the_weather(weather, param=0, show_next_day_view=show_next_day_view,
                                                    gui=gui)
        trees.change_of_day(param=1, show_next_day_view=show_next_day_view, gui=gui)
        Orchard.changing_the_water_from_the_weather(weather, param=1, show_next_day_view=show_next_day_view,
                                                    gui=gui)

    @staticmethod
    def create_seedlings(gui=False, show_status_view=None, input_gui=None):
        garden = SeedBed()
        name: list[str] = SeedBed.names('vegetables')
        if gui:
            try:
                object_of_the_plot: str = input_gui
                for i in range(0, len(name)):
                    if object_of_the_plot != name[i]:
                        continue
                    else:
                        raise NameError
                garden.new_object(name=object_of_the_plot, param=0)
                show_status_view("Посадка произошла успешно")

            except NameError:
                show_status_view("Такая рассада уже присутствует посадите другую")
        else:
            try:
                object_of_the_plot: str = input("Введите имя рассады которую вы хотите посадить: ")
                for i in range(0, len(name)):
                    if object_of_the_plot != name[i]:
                        continue
                    else:
                        raise NameError
                garden.new_object(name=object_of_the_plot, param=0)
                ViewPrint.show_status_view("---------------------------------------",
                                           "Посадка произошла успешно",
                                           "---------------------------------------")

            except NameError:
                ViewPrint.show_status_view("---------------------------------------",
                                           "Такая рассада уже присутствует посадите другую",
                                           "---------------------------------------")

    @staticmethod
    def del_seedlings(gui=False, show_status_view=None, input_gui=None):
        value: bool = False
        position_of_vegetable: int = 0
        name: list[str] = SeedBed.names('vegetables')
        if gui:
            try:
                object_of_the_plot: str = input_gui
                for i in range(0, len(name)):
                    if object_of_the_plot == name[i]:
                        value = True
                        position_of_vegetable = i
                        break
                if value is False:
                    raise NameError
                SeedBed.deleting_information(position_of_vegetable, param=0)
                show_status_view("Успешно выкопали рассаду")

            except NameError:
                show_status_view("Такой рассады нет на вашем участке")
        else:
            try:
                object_of_the_plot: str = input(
                    "Введите имя рассады которую вы хотите выкопать из своего участка: ")
                for i in range(0, len(name)):
                    if object_of_the_plot == name[i]:
                        value = True
                        position_of_vegetable = i
                        break
                if value is False:
                    raise NameError
                SeedBed.deleting_information(position_of_vegetable, param=0)
                ViewPrint.show_status_view("---------------------------------------",
                                           "Успешно выкопали рассаду",
                                           "---------------------------------------")
            except NameError:
                ViewPrint.show_status_view("---------------------------------------",
                                           "Такой рассады нет на вашем участке",
                                           "---------------------------------------")

    @staticmethod
    def create_tree(gui=False, show_status_view=None, input_gui=None):
        trees = Orchard()
        name: list[str] = Orchard.names('fruits')
        if gui:
            try:
                object_of_the_plot: str = input_gui
                for i in range(0, len(name)):
                    if object_of_the_plot != name[i]:
                        continue
                    else:
                        raise NameError
                trees.new_object(name=object_of_the_plot, param=1)
                show_status_view("Посадка произошла успешно")

            except NameError:
                show_status_view("Такое дерево уже присутствует посадите другое")
        else:
            try:
                object_of_the_plot: str = input("Введите имя дерева которое вы хотите посадить: ")
                for i in range(0, len(name)):
                    if object_of_the_plot != name[i]:
                        continue
                    else:
                        raise NameError
                trees.new_object(name=object_of_the_plot, param=1)
                ViewPrint.show_status_view("---------------------------------------",
                                           "Посадка произошла успешно",
                                           "---------------------------------------")

            except NameError:
                ViewPrint.show_status_view("---------------------------------------",
                                           "Такое дерево уже присутствует посадите другое",
                                           "---------------------------------------")

    @staticmethod
    def del_tree(gui=False, show_status_view=None, input_gui=None):
        value: bool = False
        position_of_fruits: int = 0
        name: list[str] = Orchard.names('fruits')
        if gui:
            try:
                object_of_the_plot: str = input_gui
                for i in range(0, len(name)):
                    if object_of_the_plot == name[i]:
                        value = True
                        position_of_fruits = i
                        break
                if value is False:
                    raise NameError
                Orchard.deleting_information(position_of_fruits, param=1)
                show_status_view("Успешно выкорчевали дерево")

            except NameError:
                show_status_view("Такого дерева нет на вашем участке")
        else:
            try:
                object_of_the_plot: str = input(
                    "Введите имя дерева которое вы хотите выкорчевать из своего участка: ")
                for i in range(0, len(name)):
                    if object_of_the_plot == name[i]:
                        value = True
                        position_of_fruits = i
                        break
                if value is False:
                    raise NameError
                Orchard.deleting_information(position_of_fruits, param=1)
                ViewPrint.show_status_view("---------------------------------------",
                                           "Успешно выкорчевали дерево",
                                           "---------------------------------------")

            except NameError:
                ViewPrint.show_status_view("---------------------------------------",
                                           "Такого дерева нет на вашем участке",
                                           "---------------------------------------")

    @staticmethod
    def info(gui=False, show_info_view=None):
        weather = Weather()
        if gui:
            show_info_view("Престиж", weather, SeedBed.show_information_about_objects, SeedBed.status,
                           Orchard.show_information_about_objects, Orchard.status)
        elif gui is False:
            ViewPrint.show_status_view("", "Престиж", "Погода сегодня: {}".format(weather.info_weather))
            ViewPrint.show_info_view(SeedBed.show_information_about_objects, SeedBed.status,
                                     Orchard.show_information_about_objects, Orchard.status)

    @staticmethod
    def new_day(gui=False, show_next_day_view=None):
        if gui:
            GardenArea.garden_plot_next_day(gui, show_next_day_view)
        elif gui is False:
            GardenArea.garden_plot_next_day(gui)

    @staticmethod
    def position(culture: str, name: str):
        names: list[str] = names_map[culture]
        if names is None:
            return None
        for changed_position in range(0, len(names)):
            if name == names[changed_position]:
                return changed_position
        return None


action_map = {
    'collect': GardenArea.collection,
    'weed': GardenArea.weeding_seedlings,
    'water': GardenArea.watering_the_garden_plot,
    'cure': GardenArea.cure_something_in_a_garden_plot,
    'pests': GardenArea.get_rid_of_pests,
    'fertilizer': GardenArea.use_fertilizer,
    'seedlings_new': GardenArea.create_seedlings,
    'seedlings_del': GardenArea.del_seedlings,
    'tree_new': GardenArea.create_tree,
    'tree_del': GardenArea.del_tree,
    'info': GardenArea.info,
    'new_day': GardenArea.new_day
}

names_map = {
    'fruits': Orchard.names('fruits'),
    'vegetables': SeedBed.names('vegetables')
}
