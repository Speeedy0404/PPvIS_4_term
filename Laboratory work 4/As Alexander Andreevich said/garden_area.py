from actions import *
from Weather import *
from garden_bed_and_trees import *
from view_cli import *


class GardenArea:

    def __init__(self, tag: str, collect, weed, water, cure, pests, fertilizer, seedlingsnew, treenew, seedlingsdel,
                 treedel, info, newday, gui=False, show_info_view=None, show_next_day_view=View.show_next_day_view,
                 show_status_view=None, input_gui=None) -> None:
        self.__tag = tag
        garden = SeedBed()
        trees = Orchard()
        weather = Weather()
        weeding = Weeding()
        watering = Watering()
        fertillizer = Fertilizer()
        self.processing(garden, trees, weather, weeding, watering, fertillizer, collect, weed, water, cure, pests,
                        fertilizer, seedlingsnew, treenew, seedlingsdel, treedel, info, newday, gui, show_info_view,
                        show_next_day_view, show_status_view, input_gui)

    def processing(self, garden, trees, weather, weeding, watering, fertillizer, collect, weed, water, cure, pests,
                   fertilizer, seedlingsnew, treenew, seedlingsdel, treedel, info, newday, gui,
                   show_info_view, show_next_day_view, show_status_view, input_gui) -> None:

        if collect:
            GardenArea.collection(gui, show_status_view, input_gui)
        elif weed:
            GardenArea.weeding_seedlings(weeding, gui, show_status_view, input_gui)
        elif water:
            GardenArea.watering_the_garden_plot(watering, gui, show_status_view, input_gui)
        elif cure:
            GardenArea.cure_something_in_a_garden_plot(gui, show_status_view, input_gui)
        elif pests:
            GardenArea.get_rid_of_pests(gui, show_status_view, input_gui)
        elif fertilizer:
            GardenArea.use_fertillizer(fertillizer, gui, show_status_view, input_gui)
        elif seedlingsnew:
            value: bool = False
            while not value:
                name: list[str] = SeedBed.names('vegetables')
                if gui:
                    try:
                        object_of_the_plot: str = input_gui
                        count: int = len(name)
                        value = True
                        for i in range(0, count):
                            if object_of_the_plot != name[i]:
                                continue
                            else:
                                raise NameError
                        garden.new_object(name=object_of_the_plot, param=0)
                        show_status_view("Посадка произошла успешно")

                    except NameError:
                        show_status_view("Такая рассада уже присутствует посадите другую")
                elif gui is False:
                    try:
                        object_of_the_plot: str = input("Введите имя рассады которую вы хотите посадить: ")
                        count: int = len(name)
                        value = True
                        for i in range(0, count):
                            if object_of_the_plot != name[i]:
                                continue
                            else:
                                raise NameError
                        garden.new_object(name=object_of_the_plot, param=0)
                        View.show_status_view("---------------------------------------",
                                              "Посадка произошла успешно",
                                              "---------------------------------------")

                    except NameError:
                        View.show_status_view("---------------------------------------",
                                              "Такая рассада уже присутствует посадите другую",
                                              "---------------------------------------")
        elif treenew:
            value: bool = False
            while not value:
                name: list[str] = Orchard.names('fruits')
                if gui:
                    try:
                        object_of_the_plot: str = input_gui
                        count: int = len(name)
                        value = True
                        for i in range(0, count):
                            if object_of_the_plot != name[i]:
                                continue
                            else:
                                raise NameError
                        trees.new_object(name=object_of_the_plot, param=1)
                        show_status_view("Посадка произошла успешно")

                    except NameError:
                        show_status_view("Такое дерево уже присутствует посадите другое")

                elif gui is False:
                    try:
                        object_of_the_plot: str = input("Введите имя дерева которое вы хотите посадить: ")
                        count: int = len(name)
                        value = True
                        for i in range(0, count):
                            if object_of_the_plot != name[i]:
                                continue
                            else:
                                raise NameError
                        trees.new_object(name=object_of_the_plot, param=1)
                        View.show_status_view("---------------------------------------",
                                              "Посадка произошла успешно",
                                              "---------------------------------------")

                    except NameError:
                        View.show_status_view("---------------------------------------",
                                              "Такое дерево уже присутствует посадите другое",
                                              "---------------------------------------")
        elif seedlingsdel:
            value: bool = False
            position_of_vegetable: int = 0
            name: list[str] = SeedBed.names('vegetables')
            count: int = len(name)
            while not value:
                if gui:
                    try:
                        object_of_the_plot: str = input_gui
                        for i in range(0, count):
                            if object_of_the_plot == name[i]:
                                value = True
                                position_of_vegetable = i
                                break
                        if value is False:
                            raise NameError
                        SeedBed.deleting_information(position_of_vegetable, param=0)
                        show_status_view("Успешно выкопали рассаду")

                    except NameError:
                        value = True
                        show_status_view("Такой рассады нет на вашем участке")

                elif gui is False:
                    try:
                        object_of_the_plot: str = input(
                            "Введите имя рассады которую вы хотите выкопать из своего участка: ")
                        for i in range(0, count):
                            if object_of_the_plot == name[i]:
                                value = True
                                position_of_vegetable = i
                                break
                        if value is False:
                            raise NameError
                        SeedBed.deleting_information(position_of_vegetable, param=0)
                        View.show_status_view("---------------------------------------",
                                              "Успешно выкопали рассаду",
                                              "---------------------------------------")
                    except NameError:
                        value = True
                        View.show_status_view("---------------------------------------",
                                              "Такой рассады нет на вашем участке",
                                              "---------------------------------------")
        elif treedel:
            value: bool = False
            position_of_fruits: int = 0
            name: list[str] = Orchard.names('fruits')
            count: int = len(name)
            while not value:
                if gui:
                    try:
                        object_of_the_plot: str = input_gui
                        for i in range(0, count):
                            if object_of_the_plot == name[i]:
                                value = True
                                position_of_fruits = i
                                break
                        if value is False:
                            raise NameError
                        Orchard.deleting_information(position_of_fruits, param=1)
                        show_status_view("Успешно выкорчевали дерево")

                    except NameError:
                        value = True
                        show_status_view("Такого дерева нет на вашем участке")
                elif gui is False:
                    try:
                        object_of_the_plot: str = input(
                            "Введите имя дерева которое вы хотите выкорчевать из своего участка: ")
                        for i in range(0, count):
                            if object_of_the_plot == name[i]:
                                value = True
                                position_of_fruits = i
                                break
                        if value is False:
                            raise NameError
                        Orchard.deleting_information(position_of_fruits, param=1)
                        View.show_status_view("---------------------------------------",
                                              "Успешно выкорчевали дерево",
                                              "---------------------------------------")

                    except NameError:
                        value = True
                        View.show_status_view("---------------------------------------",
                                              "Такого дерева нет на вашем участке",
                                              "---------------------------------------")
        elif info:
            if gui:
                show_info_view(self.__tag, weather, SeedBed.show_information_about_objects, SeedBed.status,
                               Orchard.show_information_about_objects, Orchard.status)
            elif gui is False:
                View.show_status_view("",
                                      self.__tag,
                                      "Погода сегодня: {}".format(weather.info_weather))
                View.show_info_view(SeedBed.show_information_about_objects, SeedBed.status,
                                    Orchard.show_information_about_objects, Orchard.status)
        elif newday:
            if gui:
                GardenArea.garden_plot_next_day(weather, garden, trees, show_next_day_view, gui)
            elif gui is False:
                GardenArea.garden_plot_next_day(weather, garden, trees)

    @staticmethod
    def collection(gui=False, show_status_view=None, input_gui=None) -> None:
        position_of_vegetable = None
        position_of_fruits = None
        value: bool = False
        object_of_the_plot: str = input_gui
        while not value:
            if gui:
                try:
                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
                        raise NameError

                    if position_of_vegetable is None:
                        pass
                    elif SeedBed.check_height(position_of_vegetable, param=0) == "Плод созрел":
                        show_status_view("Рассада успешно собрана")
                        SeedBed.deleting_information(position_of_vegetable, param=0)
                    else:

                        show_status_view("Эта рассада еще не выросла")

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_height(position_of_fruits, param=1) == "Период плодоношения":

                        show_status_view("Плоды дерева успешно собраны")

                        Orchard.deleting_information(position_of_fruits, param=1)

                    else:

                        show_status_view("Это дерево еще не созрело")

                except NameError:

                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке ")

            elif gui is False:
                try:
                    object_of_the_plot: str = input("Какую рассаду или плоды дерева которые вы хотите собрать? -> ")

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
                        raise NameError

                    if position_of_vegetable is None:
                        pass
                    elif SeedBed.check_height(position_of_vegetable, param=0) == "Плод созрел":

                        View.show_status_view("---------------------------------------", "Рассада успешно собрана",
                                              "---------------------------------------")
                        SeedBed.deleting_information(position_of_vegetable, param=0)

                    else:
                        View.show_status_view("---------------------------------------", "Эта рассада еще не выросла",
                                              "---------------------------------------")

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_height(position_of_fruits, param=1) == "Период плодоношения":

                        View.show_status_view("---------------------------------------", "Плоды дерева успешно собраны",
                                              "---------------------------------------")

                        Orchard.deleting_information(position_of_fruits, param=1)

                    else:
                        View.show_status_view("---------------------------------------", "Это дерево еще не созрело",
                                              "---------------------------------------")

                except NameError:
                    View.show_status_view("---------------------------------------",
                                          "Вы должны выбрать рассаду или дерево которые растут на вашем участке",
                                          "---------------------------------------")

    @staticmethod
    def weeding_seedlings(weeding, gui=False, show_status_view=None, input_gui=None) -> None:
        position_of_vegetable = None
        value: bool = False
        while not value:
            if gui:
                try:
                    object_of_the_plot: str = input_gui
                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    value = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break
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
                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    value = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break
                    if position_of_vegetable is None:
                        raise NameError

                    if SeedBed.check_weeds(position_of_vegetable) == 0:
                        View.show_status_view("---------------------------------------",
                                              "Этой рассаде прополка не требуется",
                                              "---------------------------------------")
                    else:

                        View.show_status_view("---------------------------------------",
                                              "",
                                              "---------------------------------------")
                        weeding.using_actions()
                        SeedBed.regeneration_weeds(position_of_vegetable, param=0)

                except NameError:
                    View.show_status_view("---------------------------------------",
                                          "Вы должны выбрать рассаду которая растёт на вашем участке",
                                          "---------------------------------------")

    @staticmethod
    def watering_the_garden_plot(watering, gui=False, show_status_view=None, input_gui=None) -> None:
        position_of_vegetable = None
        position_of_fruits = None
        value: bool = False
        object_of_the_plot: str = input_gui
        while not value:
            if gui:
                try:

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
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

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_level_of_water(position_of_fruits, param=1) == 0:
                        show_status_view("Этому дереву поливка не требуется. Земля полностью пропитана водой")

                    else:

                        watering.using_actions(gui, show_status_view)
                        Orchard.regenerate_level_of_water(position_of_fruits,
                                                          Orchard.check_level_of_water(position_of_fruits, param=1),
                                                          param=1)

                except NameError:
                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")

            elif gui is False:
                try:
                    object_of_the_plot: str = input("Какую рассаду или дерево вы хотите полить? -> ")

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
                        raise NameError

                    if position_of_vegetable is None:
                        pass
                    elif SeedBed.check_level_of_water(position_of_vegetable, param=0) == 0:
                        View.show_status_view("---------------------------------------",
                                              "Этой рассаде поливка не требуется. Земля полностью пропитана водой",
                                              "---------------------------------------")
                    else:
                        View.show_status_view("---------------------------------------",
                                              "",
                                              "---------------------------------------")
                        watering.using_actions()
                        SeedBed.regenerate_level_of_water(position_of_vegetable,
                                                          SeedBed.check_level_of_water(position_of_vegetable, param=0),
                                                          param=0)

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_level_of_water(position_of_fruits, param=1) == 0:
                        View.show_status_view("---------------------------------------",
                                              "Этому дереву поливка не требуется. Земля полностью пропитана водой",
                                              "---------------------------------------")
                    else:
                        View.show_status_view("---------------------------------------",
                                              "",
                                              "---------------------------------------")

                        watering.using_actions()
                        Orchard.regenerate_level_of_water(position_of_fruits,
                                                          Orchard.check_level_of_water(position_of_fruits, param=1),
                                                          param=1)

                except NameError:
                    View.show_status_view("---------------------------------------",
                                          "Вы должны выбрать рассаду или дерево которые растут на вашем участке",
                                          "---------------------------------------")

    @staticmethod
    def cure_something_in_a_garden_plot(gui=False, show_status_view=None, input_gui=None) -> None:
        position_of_vegetable = None
        position_of_fruits = None
        value: bool = False
        object_of_the_plot: str = input_gui
        while not value:
            if gui:
                try:

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
                        raise NameError

                    if position_of_vegetable is None:
                        pass
                    elif SeedBed.check_illness(position_of_vegetable, param=0) == 0:
                        show_status_view("Этой рассаде лечение не требуется")

                    else:

                        show_status_view("Рассада успешно вылечена")

                        SeedBed.regeneration_illness(position_of_vegetable, param=0)

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_illness(position_of_fruits, param=1) == 0:
                        show_status_view("Этому дереву лечение не требуется")
                    else:

                        show_status_view("Дерево успешно вылечено")

                        Orchard.regeneration_illness(position_of_fruits, param=1)

                except NameError:

                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")

            elif gui is False:
                try:
                    object_of_the_plot: str = input("Какую рассаду или дерево вы хотите вылечить? -> ")

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
                        raise NameError

                    if position_of_vegetable is None:
                        pass
                    elif SeedBed.check_illness(position_of_vegetable, param=0) == 0:
                        View.show_status_view("---------------------------------------",
                                              "Этой рассаде лечение не требуется",
                                              "---------------------------------------")
                    else:
                        View.show_status_view("---------------------------------------",
                                              "Рассада успешно вылечена",
                                              "---------------------------------------")
                        SeedBed.regeneration_illness(position_of_vegetable, param=0)

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_illness(position_of_fruits, param=1) == 0:
                        View.show_status_view("---------------------------------------",
                                              "Этому дереву лечение не требуется",
                                              "---------------------------------------")
                    else:
                        View.show_status_view("---------------------------------------",
                                              "Дерево успешно вылечено",
                                              "---------------------------------------")
                        Orchard.regeneration_illness(position_of_fruits, param=1)

                except NameError:
                    View.show_status_view("---------------------------------------",
                                          "Вы должны выбрать рассаду или дерево которые растут на вашем участке",
                                          "---------------------------------------")

    @staticmethod
    def get_rid_of_pests(gui=False, show_status_view=None, input_gui=None) -> None:
        position_of_vegetable = None
        position_of_fruits = None
        value: bool = False
        object_of_the_plot: str = input_gui
        while not value:
            if gui:
                try:

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
                        raise NameError

                    if position_of_vegetable is None:
                        pass
                    elif SeedBed.check_vermin(position_of_vegetable, param=0) == 0:
                        show_status_view("Этой рассаде не требуется избавление от вредителей")

                    else:

                        show_status_view("Рассада успешно избавлена от вредителей")

                        SeedBed.regeneration_vermin(position_of_vegetable, param=0)

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_vermin(position_of_fruits, param=1) == 0:

                        show_status_view("Этому дереву не требуется избавление от вредителей")

                    else:

                        show_status_view("Дерево успешно избавдено от вредителей")

                        Orchard.regeneration_vermin(position_of_fruits, param=1)

                except NameError:

                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")

            elif gui is False:
                try:
                    object_of_the_plot: str = input("Какую рассаду или дерево вы хотите избавить от вредителей? -> ")

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
                        raise NameError

                    if position_of_vegetable is None:
                        pass
                    elif SeedBed.check_vermin(position_of_vegetable, param=0) == 0:
                        View.show_status_view("---------------------------------------",
                                              "Этой рассаде не требуется избавление от вредителей",
                                              "---------------------------------------")
                    else:
                        View.show_status_view("---------------------------------------",
                                              "Рассада успешно избавлена от вредителей",
                                              "---------------------------------------")

                        SeedBed.regeneration_vermin(position_of_vegetable, param=0)

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_vermin(position_of_fruits, param=1) == 0:
                        View.show_status_view("---------------------------------------",
                                              "Этому дереву не требуется избавление от вредителей",
                                              "---------------------------------------")
                    else:
                        View.show_status_view("---------------------------------------",
                                              "Дерево успешно избавлено от вредителей",
                                              "---------------------------------------")
                        Orchard.regeneration_vermin(position_of_fruits, param=1)

                except NameError:
                    View.show_status_view("---------------------------------------",
                                          "Вы должны выбрать рассаду или дерево которые растут на вашем участке",
                                          "---------------------------------------")

    @staticmethod
    def use_fertillizer(fertillizer, gui=False, show_status_view=None, input_gui=None) -> None:
        position_of_vegetable = None
        position_of_fruits = None
        value: bool = False
        while not value:
            if gui:
                try:
                    object_of_the_plot: str = input_gui
                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
                        raise NameError

                    if position_of_vegetable is None:
                        pass
                    elif SeedBed.check_height(position_of_vegetable, param=0) == "Плод созрел":

                        show_status_view("Рассада уже созрела и не нуждаеться в удобрении")

                    else:

                        fertillizer.using_actions(gui, show_status_view)
                        SeedBed.change_height(position_of_vegetable, param=0)

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_height(position_of_fruits, param=1) == "Период плодоношения":

                        show_status_view("Плоды дерева уже созрели. Дерево не нуждаеться в удобрении")

                    else:

                        fertillizer.using_actions(gui, show_status_view)
                        Orchard.change_height(position_of_fruits, param=1)

                except NameError:
                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")

            elif gui is False:
                try:
                    object_of_the_plot: str = input("Какую рассаду или дерево вы хотите удобрить? -> ")
                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_vegetable = changed_position
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for changed_position in range(0, count):
                        if object_of_the_plot == name[changed_position]:
                            position_of_fruits = changed_position
                            break

                    if position_of_vegetable is None and position_of_fruits is None:
                        raise NameError

                    if position_of_vegetable is None:
                        pass
                    elif SeedBed.check_height(position_of_vegetable, param=0) == "Плод созрел":
                        View.show_status_view("---------------------------------------",
                                              "Рассада уже созрела и не нуждаеться в удобрении",
                                              "---------------------------------------")
                    else:
                        View.show_status_view("---------------------------------------",
                                              "",
                                              "---------------------------------------")
                        fertillizer.using_actions()
                        SeedBed.change_height(position_of_vegetable, param=0)

                    if position_of_fruits is None:
                        pass
                    elif Orchard.check_height(position_of_fruits, param=1) == "Период плодоношения":
                        View.show_status_view("---------------------------------------",
                                              "Плоды дерева уже созрели. Дерево не нуждаеться в удобрении",
                                              "---------------------------------------")
                    else:
                        View.show_status_view("---------------------------------------",
                                              "",
                                              "---------------------------------------")
                        fertillizer.using_actions()
                        Orchard.change_height(position_of_fruits, param=1)

                except NameError:
                    View.show_status_view("---------------------------------------",
                                          "Вы должны выбрать рассаду или дерево которые растут на вашем участке",
                                          "---------------------------------------")

    @staticmethod
    def garden_plot_next_day(weather, garden, trees, show_next_day_view=View.show_next_day_view, gui=False) -> None:
        weather.changing_the_weather()
        garden.change_of_day(param=0, show_next_day_view=show_next_day_view, gui=gui)
        SeedBed.changing_the_water_from_the_weather(weather, param=0, show_next_day_view=show_next_day_view,
                                                    gui=gui)
        trees.change_of_day(param=1, show_next_day_view=show_next_day_view, gui=gui)
        Orchard.changing_the_water_from_the_weather(weather, param=1, show_next_day_view=show_next_day_view,
                                                    gui=gui)
