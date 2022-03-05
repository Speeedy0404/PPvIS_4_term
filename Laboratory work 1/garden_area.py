from actions import *
from Weather import *
from garden_bed_and_trees import *


class GardenArea:

    def __init__(self, tag: str) -> None:
        self.__tag = tag
        garden = SeedBed()
        trees = Orchard()
        weather = Weather()
        weeding = Weeding()
        watering = Watering()
        fertillizer = Fertilizer()
        self.processing(garden, trees, weather, weeding, watering, fertillizer)

    def processing(self, garden, trees, weather, weeding, watering, fertillizer) -> None:
        get_value: bool = False
        print(self.__tag)
        print("Погода сегодня: {}".format(weather.info_weather))
        SeedBed.show_information_about_objects(param=0)
        SeedBed.status(param=0)
        Orchard.show_information_about_objects(param=1)
        Orchard.status(param=1)
        while (not get_value):
            try:
                print("Выберите что хотите сделать: ")
                print("Собрать рассаду или плоды дерева (1)")
                print("Прополоть (2)")
                print("Полить (3)")
                print("Вылечить (4)")
                print("Избавиться от вредителей (5)")
                print("Использовать удобрение (6)")
                print("Посадить новою рассаду (7)")
                print("Посадить новое дерево (8)")
                print("Выкопать рассаду (9)")
                print("Выкорчевать дерево (10)")
                print("Информация о сегодняшнем дне (11)")
                print("Перейти к следующему дню (12)")
                print("Закончить работы с вашим садовым участком (13) ")
                choise: int = int(input("Ваш выбор: "))
                if choise == 1:
                    GardenArea.collection()
                elif choise == 2:
                    GardenArea.weeding_seedlings(weeding)
                elif choise == 3:
                    GardenArea.watering_the_garden_plot(watering)
                elif choise == 4:
                    GardenArea.cure_something_in_a_garden_plot()
                elif choise == 5:
                    GardenArea.get_rid_of_pests()
                elif choise == 6:
                    GardenArea.use_fertillizer(fertillizer)
                elif choise == 7:
                    value: bool = False
                    while value != True:
                        try:
                            del_name: str = input("Введите имя рассады которую вы хотите посадить: ")
                            name: list[str] = SeedBed.names('vegetables_in_garden.txt')
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

                elif choise == 8:
                    value: bool = False
                    while value != True:
                        try:
                            del_name: str = input("Введите имя дерева которое вы хотите посадить: ")
                            name: list[str] = Orchard.names('fruits_in_garden.txt')
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

                elif choise == 9:
                    value: bool = False
                    i_d: int = 0
                    while value != True:
                        try:
                            del_name: str = input("Введите имя рассады которую вы хотите выкопать из своего участка: ")
                            name: list[str] = SeedBed.names('vegetables_in_garden.txt')
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

                elif choise == 10:
                    value: bool = False
                    i_t: int = 0
                    while value != True:
                        try:
                            del_name: str = input(
                                "Введите имя дерева которое вы хотите выкорчевать из своего участка: ")
                            name: list[str] = Orchard.names('fruits_in_garden.txt')
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
                elif choise == 11:
                    print('\n' * 20)
                    print(self.__tag)
                    print("Погода сегодня: {}".format(weather.info_weather))
                    SeedBed.show_information_about_objects(param=0)
                    SeedBed.status(param=0)
                    Orchard.show_information_about_objects(param=1)
                    Orchard.status(param=1)

                elif choise == 12:
                    GardenArea.garden_plot_next_day(weather, garden, trees)
                    print('\n' * 20)
                    print("Погода сегодня: {}".format(weather.info_weather))
                    SeedBed.show_information_about_objects(param=0)
                    SeedBed.status(param=0)
                    Orchard.show_information_about_objects(param=1)
                    Orchard.status(param=1)
                elif choise == 13:
                    get_value = True
                else:
                    raise ValueError

            except(ValueError):
                get_value = False
                print("---------------------------------------")
                print("Вы должны выбрать действия от 1 до 13")
                print("---------------------------------------")

    @staticmethod
    def collection() -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            try:
                delta_name: str = input("Какую рассаду или плоды дерева которые вы хотите собрать? -> ")

                name: list[str] = SeedBed.names('vegetables_in_garden.txt')
                count: int = len(name)
                for delta_i in range(0, count):
                    if delta_name == name[delta_i]:
                        i_g = delta_i
                        break

                name: list[str] = Orchard.names('fruits_in_garden.txt')
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
    def weeding_seedlings(weeding) -> None:
        i = None
        value: bool = False
        while (not value):
            try:
                delta_name: str = input("Какую рассаду вы хотите прополоть? -> ")
                name: list[str] = SeedBed.names('vegetables_in_garden.txt')
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
    def watering_the_garden_plot(watering) -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            try:
                delta_name: str = input("Какую рассаду или дерево вы хотите полить? -> ")

                name: list[str] = SeedBed.names('vegetables_in_garden.txt')
                count: int = len(name)
                for delta_i in range(0, count):
                    if delta_name == name[delta_i]:
                        i_g = delta_i
                        break

                name: list[str] = Orchard.names('fruits_in_garden.txt')
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
    def cure_something_in_a_garden_plot() -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            try:
                delta_name: str = input("Какую рассаду или дерево вы хотите вылечить? -> ")

                name: list[str] = SeedBed.names('vegetables_in_garden.txt')
                count: int = len(name)
                for delta_i in range(0, count):
                    if delta_name == name[delta_i]:
                        i_g = delta_i
                        break

                name: list[str] = Orchard.names('fruits_in_garden.txt')
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
    def get_rid_of_pests() -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            try:
                delta_name: str = input("Какую рассаду или дерево вы хотите избавить от вредителей? -> ")

                name: list[str] = SeedBed.names('vegetables_in_garden.txt')
                count: int = len(name)
                for delta_i in range(0, count):
                    if delta_name == name[delta_i]:
                        i_g = delta_i
                        break

                name: list[str] = Orchard.names('fruits_in_garden.txt')
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
    def use_fertillizer(fertillizer) -> None:
        i_g = None
        i_t = None
        value: bool = False
        while (not value):
            try:
                delta_name: str = input("Какую рассаду или дерево вы хотите удобрить? -> ")
                name: list[str] = SeedBed.names('vegetables_in_garden.txt')
                count: int = len(name)
                for delta_i in range(0, count):
                    if delta_name == name[delta_i]:
                        i_g = delta_i
                        break

                name: list[str] = Orchard.names('fruits_in_garden.txt')
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
    def garden_plot_next_day(weather, garden, trees) -> None:
        weather.changing_the_weather()
        garden.change_of_day(param=0)
        SeedBed.changing_the_water_from_the_weather(weather, param=0)
        trees.change_of_day(param=1)
        Orchard.changing_the_water_from_the_weather(weather, param=1)
