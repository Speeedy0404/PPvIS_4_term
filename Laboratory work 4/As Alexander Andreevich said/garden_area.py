from actions import *
from Weather import *
from garden_bed_and_trees import *


class GardenArea:

    def __init__(self, tag: str, collect, weed, water, cure, pests, fertilizer, seedlingsnew, treenew, seedlingsdel,
                 treedel, info, newday, gui=False, show_info_view=None, show_next_day_view=None,
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
            while value != True:
                if gui:
                    try:
                        del_name: str = input_gui
                        name: list[str] = SeedBed.names('vegetables')
                        count: int = len(name)
                        value = True
                        for i in range(0, count):
                            if del_name != name[i]:
                                continue
                            else:
                                raise NameError
                        garden.new_object(name=del_name, param=0)
                        show_status_view("Посадка произошла успешно")

                    except(NameError):
                        show_status_view("Такая рассада уже присутствует посадите другую")
                elif gui == False:
                    try:
                        del_name: str = input("Введите имя рассады которую вы хотите посадить: ")
                        name: list[str] = SeedBed.names('vegetables')
                        count: int = len(name)
                        value = True
                        for i in range(0, count):
                            if del_name != name[i]:
                                continue
                            else:
                                raise NameError
                        garden.new_object(name=del_name, param=0)
                        print("---------------------------------------")
                        print("Посадка произошла успешно")
                        print("---------------------------------------")

                    except(NameError):
                        print("---------------------------------------")
                        print("Такая рассада уже присутствует посадите другую")
                        print("---------------------------------------")
        elif treenew:
            value: bool = False
            while value != True:
                if gui:
                    try:
                        del_name: str = input_gui
                        name: list[str] = Orchard.names('fruits')
                        count: int = len(name)
                        value = True
                        for i in range(0, count):
                            if del_name != name[i]:
                                continue
                            else:
                                raise NameError
                        trees.new_object(name=del_name, param=1)
                        show_status_view("Посадка произошла успешно")

                    except(NameError):
                        show_status_view("Такое дерево уже присутствует посадите другое")


                elif gui == False:
                    try:
                        del_name: str = input("Введите имя дерева которое вы хотите посадить: ")
                        name: list[str] = Orchard.names('fruits')
                        count: int = len(name)
                        value = True
                        for i in range(0, count):
                            if del_name != name[i]:
                                continue
                            else:
                                raise NameError
                        trees.new_object(name=del_name, param=1)
                        print("---------------------------------------")
                        print("Посадка произошла успешно")
                        print("---------------------------------------")

                    except(NameError):
                        print("---------------------------------------")
                        print("Такое дерево уже присутствует посадите другое")
                        print("---------------------------------------")
        elif seedlingsdel:
            value: bool = False
            i_d: int = 0
            while value != True:
                if gui:
                    try:
                        del_name: str = input_gui
                        name: list[str] = SeedBed.names('vegetables')
                        count: int = len(name)
                        for i in range(0, count):
                            if del_name == name[i]:
                                value = True
                                i_d = i
                                break
                        if value == False:
                            raise NameError
                        SeedBed.deleting_information(i_d, param=0)
                        show_status_view("Успешно выкопали рассаду")

                    except(NameError):
                        value = True
                        show_status_view("Такой рассады нет на вашем участке")

                elif gui == False:
                    try:
                        del_name: str = input("Введите имя рассады которую вы хотите выкопать из своего участка: ")
                        name: list[str] = SeedBed.names('vegetables')
                        count: int = len(name)
                        for i in range(0, count):
                            if del_name == name[i]:
                                value = True
                                i_d = i
                                break
                        if value == False:
                            raise NameError
                        SeedBed.deleting_information(i_d, param=0)
                        print("---------------------------------------")
                        print("Успешно выкопали рассаду")
                        print("---------------------------------------")

                    except(NameError):
                        value = True
                        print("---------------------------------------")
                        print("Такой рассады нет на вашем участке")
                        print("---------------------------------------")
        elif treedel:
            value: bool = False
            i_t: int = 0
            while value != True:
                if gui:
                    try:
                        del_name: str = input_gui
                        name: list[str] = Orchard.names('fruits')
                        count: int = len(name)
                        for i in range(0, count):
                            if del_name == name[i]:
                                value = True
                                i_t = i
                                break
                        if value == False:
                            raise NameError
                        Orchard.deleting_information(i_t, param=1)
                        show_status_view("Успешно выкорчевали дерево")

                    except(NameError):
                        value = True
                        show_status_view("Такого дерева нет на вашем участке")
                elif gui == False:
                    try:
                        del_name: str = input(
                            "Введите имя дерева которое вы хотите выкорчевать из своего участка: ")
                        name: list[str] = Orchard.names('fruits')
                        count: int = len(name)
                        for i in range(0, count):
                            if del_name == name[i]:
                                value = True
                                i_t = i
                                break
                        if value == False:
                            raise NameError
                        Orchard.deleting_information(i_t, param=1)
                        print("---------------------------------------")
                        print("Успешно выкорчевали дерево")
                        print("---------------------------------------")

                    except(NameError):
                        value = True
                        print("---------------------------------------")
                        print("Такого дерева нет на вашем участке")
                        print("---------------------------------------")
        elif info:
            if gui:
                show_info_view(self.__tag, weather, SeedBed.show_information_about_objects, SeedBed.status,
                                   Orchard.show_information_about_objects, Orchard.status)
            elif gui == False:
                print(self.__tag)
                print("Погода сегодня: {}".format(weather.info_weather))
                SeedBed.show_information_about_objects(param=0)
                SeedBed.status(param=0)
                Orchard.show_information_about_objects(param=1)
                Orchard.status(param=1)
        elif newday:
            if gui:
                GardenArea.garden_plot_next_day(weather, garden, trees, show_next_day_view, gui)
            elif gui == False:
                GardenArea.garden_plot_next_day(weather, garden, trees)
                print("Погода сегодня: {}".format(weather.info_weather))
                SeedBed.show_information_about_objects(param=0)
                SeedBed.status(param=0)
                Orchard.show_information_about_objects(param=1)
                Orchard.status(param=1)

    @staticmethod
    def collection(gui=False, show_status_view=None, input_gui=None) -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            if gui:
                try:
                    delta_name: str = input_gui

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_height(i_g, param=0) == "Плод созрел":
                        show_status_view("Рассада успешно собрана")
                        SeedBed.deleting_information(i_g, param=0)
                    else:

                        show_status_view("Эта рассада еще не выросла")

                    if i_t == None:
                        pass
                    elif Orchard.check_height(i_t, param=1) == "Период плодоношения":

                        show_status_view("Плоды дерева успешно собраны")

                        Orchard.deleting_information(i_t, param=1)

                    else:

                        show_status_view("Это дерево еще не созрело")

                except(NameError):

                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке ")

            elif gui == False:
                try:
                    delta_name: str = input("Какую рассаду или плоды дерева которые вы хотите собрать? -> ")

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_height(i_g, param=0) == "Плод созрел":
                        print("---------------------------------------")
                        print("Рассада успешно собрана")
                        SeedBed.deleting_information(i_g, param=0)
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        print("Эта рассада еще не выросла")
                        print("---------------------------------------")

                    if i_t == None:
                        pass
                    elif Orchard.check_height(i_t, param=1) == "Период плодоношения":
                        print("---------------------------------------")
                        print("Плоды дерева успешно собраны")
                        Orchard.deleting_information(i_t, param=1)
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        print("Это дерево еще не созрело")
                        print("---------------------------------------")

                except(NameError):
                    print("---------------------------------------")
                    print("Вы должны выбрать рассаду или дерево которые растут на вашем участке  ")
                    print("---------------------------------------")

    @staticmethod
    def weeding_seedlings(weeding, gui=False, show_status_view=None, input_gui=None) -> None:
        i = None
        value: bool = False
        while (not value):
            if gui:
                try:
                    delta_name: str = input_gui
                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    value = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i = delta_i
                            break
                    if i == None:
                        raise NameError

                    if SeedBed.check_weeds(i) == 0:
                        show_status_view("Этой рассаде прополка не требуется")

                    else:
                        weeding.using_actions(gui, show_status_view)
                        SeedBed.regeneration_weeds(i, param=0)

                except(NameError):
                    show_status_view("Вы должны выбрать рассаду которая растёт на вашем участке")

            elif gui == False:
                try:
                    delta_name: str = input("Какую рассаду вы хотите прополоть? -> ")
                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    value = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i = delta_i
                            break
                    if i == None:
                        raise NameError

                    if SeedBed.check_weeds(i) == 0:
                        print("---------------------------------------")
                        print("Этой рассаде прополка не требуется")
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        weeding.using_actions()
                        SeedBed.regeneration_weeds(i, param=0)
                        print("---------------------------------------")

                except(NameError):
                    print("---------------------------------------")
                    print("Вы должны выбрать рассаду которая растёт на вашем участке  ")
                    print("---------------------------------------")

    @staticmethod
    def watering_the_garden_plot(watering, gui=False, show_status_view=None, input_gui=None) -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            if gui:
                try:
                    delta_name: str = input_gui

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_level_of_water(i_g, param=0) == 0:

                        show_status_view("Этой рассаде поливка не требуется. Земля полностью пропитана водой")

                    else:
                        watering.using_actions(gui, show_status_view)
                        SeedBed.regenerate_level_of_water(i_g, SeedBed.check_level_of_water(i_g, param=0),
                                                          param=0)

                    if i_t == None:
                        pass
                    elif Orchard.check_level_of_water(i_t, param=1) == 0:
                        show_status_view("Этому дереву поливка не требуется. Земля полностью пропитана водой")

                    else:

                        watering.using_actions(gui, show_status_view)
                        Orchard.regenerate_level_of_water(i_t, Orchard.check_level_of_water(i_t, param=1),
                                                          param=1)

                except(NameError):
                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")

            elif gui == False:
                try:
                    delta_name: str = input("Какую рассаду или дерево вы хотите полить? -> ")

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_level_of_water(i_g, param=0) == 0:
                        print("---------------------------------------")
                        print("Этой рассаде поливка не требуется. Земля полностью пропитана водой")
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        watering.using_actions()
                        SeedBed.regenerate_level_of_water(i_g, SeedBed.check_level_of_water(i_g, param=0),
                                                          param=0)
                        print("---------------------------------------")

                    if i_t == None:
                        pass
                    elif Orchard.check_level_of_water(i_t, param=1) == 0:
                        print("---------------------------------------")
                        print("Этому дереву поливка не требуется. Земля полностью пропитана водой")
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        watering.using_actions()
                        Orchard.regenerate_level_of_water(i_t, Orchard.check_level_of_water(i_t, param=1),
                                                          param=1)
                        print("---------------------------------------")

                except(NameError):
                    print("---------------------------------------")
                    print("Вы должны выбрать рассаду или дерево которые растут на вашем участке  ")
                    print("---------------------------------------")

    @staticmethod
    def cure_something_in_a_garden_plot(gui=False, show_status_view=None, input_gui=None) -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            if gui:
                try:
                    delta_name: str = input_gui

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_illness(i_g, param=0) == 0:
                        show_status_view("Этой рассаде лечение не требуется")

                    else:

                        show_status_view("Рассада успешно вылечена")

                        SeedBed.regeneration_illness(i_g, param=0)

                    if i_t is None:
                        pass
                    elif Orchard.check_illness(i_t, param=1) == 0:
                        show_status_view("Этому дереву лечение не требуется")
                    else:

                        show_status_view("Дерево успешно вылечено")

                        Orchard.regeneration_illness(i_t, param=1)

                except NameError:

                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")

            elif gui == False:
                try:
                    delta_name: str = input("Какую рассаду или дерево вы хотите вылечить? -> ")

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_illness(i_g, param=0) == 0:
                        print("---------------------------------------")
                        print("Этой рассаде лечение не требуется")
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        print("Рассада успешно вылечена")
                        SeedBed.regeneration_illness(i_g, param=0)
                        print("---------------------------------------")

                    if i_t == None:
                        pass
                    elif Orchard.check_illness(i_t, param=1) == 0:
                        print("---------------------------------------")
                        print("Этому дереву лечение не требуется")
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        print("Дерево успешно вылечено")
                        Orchard.regeneration_illness(i_t, param=1)
                        print("---------------------------------------")

                except(NameError):
                    print("---------------------------------------")
                    print("Вы должны выбрать рассаду или дерево которые растут на вашем участке  ")
                    print("---------------------------------------")

    @staticmethod
    def get_rid_of_pests(gui=False, show_status_view=None, input_gui=None) -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            if gui:
                try:
                    delta_name: str = input_gui

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_vermin(i_g, param=0) == 0:
                        show_status_view("Этой рассаде не требуется избавление от вредителей")

                    else:

                        show_status_view("Рассада успешно избавлена от вредителей")

                        SeedBed.regeneration_vermin(i_g, param=0)

                    if i_t == None:
                        pass
                    elif Orchard.check_vermin(i_t, param=1) == 0:

                        show_status_view("Этому дереву не требуется избавление от вредителей")

                    else:

                        show_status_view("Дерево успешно избавдено от вредителей")

                        Orchard.regeneration_vermin(i_t, param=1)

                except(NameError):

                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")

            elif gui == False:
                try:
                    delta_name: str = input("Какую рассаду или дерево вы хотите избавить от вредителей? -> ")

                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_vermin(i_g, param=0) == 0:
                        print("---------------------------------------")
                        print("Этой рассаде не требуется избавление от вредителей")
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        print("Рассада успешно избавлена от вредителей")
                        SeedBed.regeneration_vermin(i_g, param=0)
                        print("---------------------------------------")

                    if i_t == None:
                        pass
                    elif Orchard.check_vermin(i_t, param=1) == 0:
                        print("---------------------------------------")
                        print("Этому дереву не требуется избавление от вредителей")
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        print("Дерево успешно избавдено от вредителей")
                        Orchard.regeneration_vermin(i_t, param=1)
                        print("---------------------------------------")

                except(NameError):
                    print("---------------------------------------")
                    print("Вы должны выбрать рассаду или дерево которые растут на вашем участке  ")
                    print("---------------------------------------")

    @staticmethod
    def use_fertillizer(fertillizer, gui=False, show_status_view=None, input_gui=None) -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            if gui:
                try:
                    delta_name: str = input_gui
                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_height(i_g, param=0) == "Плод созрел":

                        show_status_view("Рассада уже созрела и не нуждаеться в удобрении")

                    else:

                        fertillizer.using_actions(gui, show_status_view)
                        SeedBed.change_height(i_g, param=0)


                    if i_t == None:
                        pass
                    elif Orchard.check_height(i_t, param=1) == "Период плодоношения":

                        show_status_view("Плоды дерева уже созрели. Дерево не нуждаеться в удобрении")

                    else:

                        fertillizer.using_actions(gui, show_status_view)
                        Orchard.change_height(i_t, param=1)


                except(NameError):

                    show_status_view("Вы должны выбрать рассаду или дерево которые растут на вашем участке")


            elif gui ==False:
                try:
                    delta_name: str = input("Какую рассаду или дерево вы хотите удобрить? -> ")
                    name: list[str] = SeedBed.names('vegetables')
                    count: int = len(name)
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_g = delta_i
                            break

                    name: list[str] = Orchard.names('fruits')
                    count: int = len(name)
                    value: bool = True
                    for delta_i in range(0, count):
                        if delta_name == name[delta_i]:
                            i_t = delta_i
                            break

                    if i_g == None and i_t == None:
                        raise NameError

                    if i_g == None:
                        pass
                    elif SeedBed.check_height(i_g, param=0) == "Плод созрел":
                        print("---------------------------------------")
                        print("Рассада уже созрела и не нуждаеться в удобрении")
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        fertillizer.using_actions()
                        SeedBed.change_height(i_g, param=0)
                        print("---------------------------------------")

                    if i_t == None:
                        pass
                    elif Orchard.check_height(i_t, param=1) == "Период плодоношения":
                        print("---------------------------------------")
                        print("Плоды дерева уже созрели. Дерево не нуждаеться в удобрении")
                        print("---------------------------------------")
                    else:
                        print("---------------------------------------")
                        fertillizer.using_actions()
                        Orchard.change_height(i_t, param=1)
                        print("---------------------------------------")

                except(NameError):
                    print("---------------------------------------")
                    print("Вы должны выбрать рассаду или дерево которые растут на вашем участке  ")
                    print("---------------------------------------")

    @staticmethod
    def garden_plot_next_day(weather, garden, trees, show_next_day_view=None, gui=False) -> None:
        weather.changing_the_weather()
        garden.change_of_day(param=0, show_next_day_view=show_next_day_view, gui=gui)
        SeedBed.changing_the_water_from_the_weather(weather, param=0, show_next_day_view=show_next_day_view,
                                                    gui=gui)
        trees.change_of_day(param=1, show_next_day_view=show_next_day_view, gui=gui)
        Orchard.changing_the_water_from_the_weather(weather, param=1, show_next_day_view=show_next_day_view,
                                                    gui=gui)
