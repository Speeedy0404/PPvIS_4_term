from Vegetables_and_trees import *
from weeds_vermin_illness import *
from Save_and_del import *


class GardenBedAndTrees:
    __vegetables_in_garden: list[Vegetables] = []
    __vermin_of_vegetables: list[Vermin] = []
    __illness_of_vegetables: list[Illness] = []
    __weeds_of_vegetables: list[Weeds] = []

    __fruits_in_garden: list[Fruits] = []
    __vermin_of_fruits: list[Vermin] = []
    __illness_of_fruits: list[Illness] = []

    def __init__(self, way: str, param: int) -> None:
        self.__way = way
        names_of_all_objects = GardenBedAndTrees.names(way)
        GardenBedAndTrees.return_objects_to_the_garden(names_of_all_objects, param)
        GardenBedAndTrees.return_vermin_to_the_garden(names_of_all_objects, param)
        GardenBedAndTrees.return_illness_to_the_garden(names_of_all_objects, param)

    @staticmethod
    def objects_in_garden(i: int, param: int) -> str:
        if param == 0:
            return GardenBedAndTrees.__vegetables_in_garden[i].info_name
        elif param == 1:
            return GardenBedAndTrees.__fruits_in_garden[i].info_name

    @staticmethod
    def check_weeds(i: int) -> int:
        if GardenBedAndTrees.__weeds_of_vegetables[i].info_condition == "Все хорошо, никаких сорняков":
            return 0
        else:
            return 1

    @staticmethod
    def regeneration_weeds(i: int, param: int) -> None:
        GardenBedAndTrees.__weeds_of_vegetables[i].remove_condition(param)

    @staticmethod
    def check_illness(i: int, param: int) -> int:
        if param == 0:
            if GardenBedAndTrees.__illness_of_vegetables[i].info_condition == "Все хорошо, никаких болезней":
                return 0
            else:
                return 1
        elif param == 1:
            if GardenBedAndTrees.__illness_of_fruits[i].info_condition == "Все хорошо, никаких болезней":
                return 0
            else:
                return 1

    @staticmethod
    def regeneration_illness(i: int, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__illness_of_vegetables[i].remove_condition(param)
        elif param == 1:
            GardenBedAndTrees.__illness_of_fruits[i].remove_condition(param)

    @staticmethod
    def check_vermin(i: int, param: int) -> int:
        if param == 0:
            if GardenBedAndTrees.__vermin_of_vegetables[i].info_condition == "Все хорошо, никаких вредителей":
                return 0
            else:
                return 1
        elif param == 1:
            if GardenBedAndTrees.__vermin_of_fruits[i].info_condition == "Все хорошо, никаких вредителей":
                return 0
            else:
                return 1

    @staticmethod
    def regeneration_vermin(i: int, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vermin_of_vegetables[i].remove_condition(param)
        elif param == 1:
            GardenBedAndTrees.__vermin_of_fruits[i].remove_condition(param)

    @staticmethod
    def check_level_of_water(i: int, param: int) -> int:
        if param == 0:
            number = GardenBedAndTrees.__vegetables_in_garden[i].info_lever_of_water
            if number == 5:
                return 0
            else:
                number = 5 - number
                return number
        elif param == 1:
            number = GardenBedAndTrees.__fruits_in_garden[i].info_lever_of_water
            if number == 5:
                return 0
            else:
                number = 5 - number
                return number

    @staticmethod
    def regenerate_level_of_water(i_t: int, i: int, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden[i_t].change_level_of_water(i, param)
        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden[i_t].change_level_of_water(i, param)

    @staticmethod
    def check_height(i: int, param: int) -> str:
        if param == 0:
            return GardenBedAndTrees.__vegetables_in_garden[i].info_height

        if param == 1:
            return GardenBedAndTrees.__fruits_in_garden[i].info_height

    @staticmethod
    def change_height(i_t: int, param: int) -> None:
        if param == 0:
            growth_stage: tuple[str, str, str, str, str, str, str] = ("Первые 2-3 настоящих листа", "Рост",
                                                                      "Фаза активного вегетационного роста", "Цветение",
                                                                      "Формирование плода", "Вызревание плода",
                                                                      "Плод созрел")
            i_delta: int = 0
            i_growth: int = 0
            height_delta = GardenBedAndTrees.__vegetables_in_garden[i_t].info_height
            how_many = GardenBedAndTrees.__vegetables_in_garden[i_t].info_how_many_days_until_the_next_stage
            for i in range(0, 7):
                if height_delta == growth_stage[i]:
                    i_delta: int = how_many * (i + 1)
                    i_growth: int = i + 1
                    break
            GardenBedAndTrees.__vegetables_in_garden[i_t].change_day_today(i_delta, param)
            GardenBedAndTrees.__vegetables_in_garden[i_t].fetal_growth(i_growth, param)

        elif param == 1:
            growth_stage: tuple[str, str, str, str, str, str, str] = ("Семечко в земле", "Рост",
                                                                      "Первые 2-3 листочка",
                                                                      "Появился не крепкий ствол",
                                                                      "Период роста", "Период вызревания",
                                                                      "Период плодоношения")
            i_delta: int = 0
            i_growth: int = 0
            height_delta: str = GardenBedAndTrees.__fruits_in_garden[i_t].info_height
            how_many: int = GardenBedAndTrees.__fruits_in_garden[i_t].info_how_many_days_until_the_next_stage
            for i in range(0, 7):
                if height_delta == growth_stage[i]:
                    i_delta: int = how_many * (i + 1)
                    i_growth: int = i + 1
                    break
            GardenBedAndTrees.__fruits_in_garden[i_t].change_day_today(i_delta, param)
            GardenBedAndTrees.__fruits_in_garden[i_t].fetal_growth(i_growth, param)

    @staticmethod
    def the_objects_is_cured(i: int, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden[i].regeneration_hp(param)
        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden[i].regeneration_hp(param)

    @staticmethod
    def names(way: str) -> list:
        names = ReadOverwritingGardenBedAndTrees.read(way)
        return names

    @staticmethod
    def return_objects_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            for i in names:
                GardenBedAndTrees.__vegetables_in_garden.append(Vegetables(i, 0, param))
        elif param == 1:
            for i in names:
                GardenBedAndTrees.__fruits_in_garden.append(Fruits(i, 0, param))

    @staticmethod
    def return_vermin_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            for i in names:
                GardenBedAndTrees.__vermin_of_vegetables.append(Vermin(name=i, creation=0, param=param))
        elif param == 1:
            for i in names:
                GardenBedAndTrees.__vermin_of_fruits.append(Vermin(name=i, creation=0, param=param))

    @staticmethod
    def return_illness_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            for i in names:
                GardenBedAndTrees.__illness_of_vegetables.append(Illness(name=i, creation=0, param=param))
        elif param == 1:
            for i in names:
                GardenBedAndTrees.__illness_of_fruits.append(Illness(name=i, creation=0, param=param))

    @staticmethod
    def return_weeds_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            for i in names:
                GardenBedAndTrees.__weeds_of_vegetables.append(Weeds(name=i, creation=0, param=param))

    def new_object(self, name: str, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden.append(Vegetables(name, 1, param))
            names = GardenBedAndTrees.names(self.__way)
            names.append(name)
            length: int = len(self.__vegetables_in_garden)
            ReadOverwritingGardenBedAndTrees.overwriting(self.__way, length, names)
            GardenBedAndTrees.__vermin_of_vegetables.append(Vermin(name, creation=1, param=param))
            GardenBedAndTrees.__illness_of_vegetables.append(Illness(name, creation=1, param=param))
            GardenBedAndTrees.__weeds_of_vegetables.append(Weeds(name, creation=1, param=param))
        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden.append(Fruits(name, 1, param))
            names = GardenBedAndTrees.names(self.__way)
            names.append(name)
            length: int = len(self.__fruits_in_garden)
            ReadOverwritingGardenBedAndTrees.overwriting(self.__way, length, names)
            GardenBedAndTrees.__vermin_of_fruits.append(Vermin(name, creation=1, param=param))
            GardenBedAndTrees.__illness_of_fruits.append(Illness(name, creation=1, param=param))

    @staticmethod
    def show_information_about_objects(param: int, gui=False, root=None, list=None, label=None) -> None:
        if param == 0:
            if gui:
                it = len(list)
                list.append(label(text="---------------------------------------"))
                root.inffo.add_widget(list[it])
                it += 1
                list.append(label(text="Вот какие виды растут на грядке: "))
                root.inffo.add_widget(list[it])
                number: int = len(GardenBedAndTrees.__vegetables_in_garden)
                for i in range(0, number):
                    it += 1
                    list.append(label(text=GardenBedAndTrees.objects_in_garden(i, param)))
                    root.inffo.add_widget(list[it])
            elif gui == False:
                message = "Вот какие виды растут на грядке: "
                print("---------------------------------------")
                print(message)
                number: int = len(GardenBedAndTrees.__vegetables_in_garden)
                for i in range(0, number):
                    print(GardenBedAndTrees.objects_in_garden(i, param))
        elif param == 1:
            if gui:
                it = len(list)
                list.append(label(text="---------------------------------------"))
                root.inffo.add_widget(list[it])
                it += 1
                list.append(label(text="Вот какие деревья растут в саду: "))
                root.inffo.add_widget(list[it])
                number: int = len(GardenBedAndTrees.__fruits_in_garden)
                for i in range(0, number):
                    it += 1
                    list.append(label(text=GardenBedAndTrees.objects_in_garden(i, param)))
                    root.inffo.add_widget(list[it])
            elif gui == False:
                message = "Вот какие деревья растут в саду: "
                print("---------------------------------------")
                print(message)
                number: int = len(GardenBedAndTrees.__fruits_in_garden)
                for i in range(0, number):
                    print(GardenBedAndTrees.objects_in_garden(i, param))

    def change_of_day(self, param: int) -> None:
        if param == 0:
            name: list[str] = GardenBedAndTrees.names(self.__way)
            count: int = len(name)
            g: int = 0
            for i in range(0, count):
                i: int = i + g
                error: int = GardenBedAndTrees.__vegetables_in_garden[i].next_day(param)
                if error == 0:
                    print(GardenBedAndTrees.objects_in_garden(i, param))
                    print("Сгнил из-за того что вы его не собрали")
                    GardenBedAndTrees.deleting_information(i, param)
                    g += -1

            name: list[str] = GardenBedAndTrees.names(self.__way)
            count: int = len(name)
            g: int = 0
            for i in range(0, count):
                i: int = i + g
                count1: int = 0
                GardenBedAndTrees.__vermin_of_vegetables[i].changing_condition(param)
                GardenBedAndTrees.__illness_of_vegetables[i].changing_condition(param)
                GardenBedAndTrees.__weeds_of_vegetables[i].changing_condition(param)

                if GardenBedAndTrees.__vermin_of_vegetables[i].info_condition == "Появились вредители, требуется" \
                                                                                 " попшыкать специальным средством":
                    error: int = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                    if error == 0:
                        print(GardenBedAndTrees.objects_in_garden(i, param))
                        print("Был утерян из-за вредителей")
                        GardenBedAndTrees.deleting_information(i, param)
                        g += -1
                        count1 = 1

                if count1 == 0:
                    if GardenBedAndTrees.__illness_of_vegetables[i].info_condition == "Появилась болезнь, требуется" \
                                                                                      " опрыскивание специальным средством":
                        error = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                        if error == 0:
                            print(GardenBedAndTrees.objects_in_garden(i, param))
                            print("Был утерян из-за болезней")
                            GardenBedAndTrees.deleting_information(i, param)
                            g += -1
                            count1 = 1

                if count1 == 0:
                    if GardenBedAndTrees.__weeds_of_vegetables[
                        i].info_condition == "Появились сорняки, требуется прополка":
                        error = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                        if error == 0:
                            print(GardenBedAndTrees.objects_in_garden(i, param))
                            print("Был утерян из-за сорняков")
                            GardenBedAndTrees.deleting_information(i, param)
                            g += -1
                            count1 = 1

                if count1 == 0:
                    if GardenBedAndTrees.check_weeds(i) == 0 and GardenBedAndTrees.check_vermin(i, param) \
                            == 0 and GardenBedAndTrees.check_illness(i, param) == 0:
                        GardenBedAndTrees.the_objects_is_cured(i, param)
        elif param == 1:
            name: list[str] = GardenBedAndTrees.names(self.__way)
            count: int = len(name)
            g: int = 0
            for i in range(0, count):
                i: int = i + g
                error: int = GardenBedAndTrees.__fruits_in_garden[i].next_day(param)
                if error == 0:
                    print(GardenBedAndTrees.objects_in_garden(i, param))
                    print("Вы долго не собирали созревшие плоды с дерева из-за этого оно увяло")
                    GardenBedAndTrees.deleting_information(i, param)
                    g += -1

            name: list[str] = GardenBedAndTrees.names(self.__way)
            count: int = len(name)
            g: int = 0
            for i in range(0, count):
                i: int = i + g
                count1: int = 0
                GardenBedAndTrees.__vermin_of_fruits[i].changing_condition(param)
                GardenBedAndTrees.__illness_of_fruits[i].changing_condition(param)

                if GardenBedAndTrees.__vermin_of_fruits[i].info_condition == "Появились вредители, требуется" \
                                                                             " попшыкать специальным средством":
                    error: int = GardenBedAndTrees.__fruits_in_garden[i].change_hp(param)
                    if error == 0:
                        print(GardenBedAndTrees.objects_in_garden(i, param))
                        print("Было утерян из-за вредителей")
                        GardenBedAndTrees.deleting_information(i, param)
                        g += -1
                        count1 = 1

                if count1 == 0:
                    if GardenBedAndTrees.__illness_of_fruits[i].info_condition == "Появилась болезнь, требуется" \
                                                                                  " опрыскивание специальным средством":
                        error: int = GardenBedAndTrees.__fruits_in_garden[i].change_hp(param)
                        if error == 0:
                            print(GardenBedAndTrees.objects_in_garden(i, param))
                            print("Было утерян из-за болезней")
                            GardenBedAndTrees.deleting_information(i, param)
                            g += -1
                            count1 = 1
                if count1 == 0:
                    if GardenBedAndTrees.check_vermin(i, param) == 0 and GardenBedAndTrees.check_illness(i, param) == 0:
                        GardenBedAndTrees.the_objects_is_cured(i, param)

    @staticmethod
    def changing_the_water_from_the_weather(weather, param: int) -> None:
        weather_of_the_day = weather.info_weather
        if weather_of_the_day == "Cолнце":
            number: int = -2
            GardenBedAndTrees.changing(number, param)
        elif weather_of_the_day == "Дождь":
            number: int = 3
            GardenBedAndTrees.changing(number, param)
        elif weather_of_the_day == "Очень сильная жара(засуха)":
            number: int = -3
            GardenBedAndTrees.changing(number, param)
        elif weather_of_the_day == "Морось":
            number: int = 1
            GardenBedAndTrees.changing(number, param)
        elif weather_of_the_day == "Пасмурно":
            number: int = -1
            GardenBedAndTrees.changing(number, param)

    @staticmethod
    def changing(number: int, param: int) -> None:
        if param == 0:
            way = 'vegetables_in_garden.txt'
            message = "Рассада усохла из-за нехватки воды"
            name: list[str] = GardenBedAndTrees.names(way)
            count: int = len(name)
            g: int = 0
            for i in range(0, count):
                i = i + g
                error: int = GardenBedAndTrees.__vegetables_in_garden[i].change_level_of_water(number, param)
                if error == 0:
                    print(GardenBedAndTrees.objects_in_garden(i, param))
                    print(message)
                    GardenBedAndTrees.deleting_information(i, param)
                    g += -1
        elif param == 1:
            way = 'fruits_in_garden.txt'
            message = "Дерево усохло из-за нехватки воды"
            name: list[str] = GardenBedAndTrees.names(way)
            count: int = len(name)
            g: int = 0
            for i in range(0, count):
                i = i + g
                error: int = GardenBedAndTrees.__fruits_in_garden[i].change_level_of_water(number, param)
                if error == 0:
                    print(GardenBedAndTrees.objects_in_garden(i, param))
                    print(message)
                    GardenBedAndTrees.deleting_information(i, param)
                    g += -1

    @staticmethod
    def deleting_information(i: int, param: int) -> None:
        if param == 0:
            way = 'vegetables_in_garden.txt'
            GardenBedAndTrees.__vegetables_in_garden[i].del_object(param)
            GardenBedAndTrees.__vermin_of_vegetables[i].del_condition(param)
            GardenBedAndTrees.__weeds_of_vegetables[i].del_condition(param)
            GardenBedAndTrees.__illness_of_vegetables[i].del_condition(param)
            GardenBedAndTrees.__vegetables_in_garden.pop(i)
            GardenBedAndTrees.__vermin_of_vegetables.pop(i)
            GardenBedAndTrees.__illness_of_vegetables.pop(i)
            GardenBedAndTrees.__weeds_of_vegetables.pop(i)
            length: int = len(GardenBedAndTrees.__vegetables_in_garden)
            names = []
            for i in range(0, length):
                names.append(GardenBedAndTrees.objects_in_garden(i, param=0))
            ReadOverwritingGardenBedAndTrees.overwriting(way, length, names)
        elif param == 1:
            way = 'fruits_in_garden.txt'
            GardenBedAndTrees.__fruits_in_garden[i].del_object(param)
            GardenBedAndTrees.__vermin_of_fruits[i].del_condition(param)
            GardenBedAndTrees.__illness_of_fruits[i].del_condition(param)
            GardenBedAndTrees.__fruits_in_garden.pop(i)
            GardenBedAndTrees.__vermin_of_fruits.pop(i)
            GardenBedAndTrees.__illness_of_fruits.pop(i)
            length: int = len(GardenBedAndTrees.__fruits_in_garden)
            names = []
            for i in range(0, length):
                names.append(GardenBedAndTrees.objects_in_garden(i, param=1))
            ReadOverwritingGardenBedAndTrees.overwriting(way, length, names)

    @staticmethod
    def status(param: int, gui=False, root=None, list=None, label=None) -> None:
        if param == 0:
            way = 'vegetables_in_garden.txt'
            print("---------------------------------------")
            print("Вот информация о состоянии каждого вида: ")
            name: list[str] = GardenBedAndTrees.names(way)
            count: int = len(name)
            for i in range(0, count):
                print("\n")
                print(name[i])
                print("Стадия роста: {}".format(GardenBedAndTrees.__vegetables_in_garden[i].info_height))
                print("Уровень воды: {}".format(GardenBedAndTrees.__vegetables_in_garden[i].info_lever_of_water))
                print("Очков здоровья: {}".format(GardenBedAndTrees.__vegetables_in_garden[i].info_lever_of_hp))
                print("Вредители: {}".format(GardenBedAndTrees.__vermin_of_vegetables[i].info_condition))
                print("Болезни: {}".format(GardenBedAndTrees.__illness_of_vegetables[i].info_condition))
                print("Сорняки: {}".format(GardenBedAndTrees.__weeds_of_vegetables[i].info_condition))
            print("---------------------------------------")
        elif param == 1:
            way = 'fruits_in_garden.txt'
            print("---------------------------------------")
            print("Вот информация о состоянии каждого дерева: ")
            name: list[str] = GardenBedAndTrees.names(way)
            count: int = len(name)
            for i in range(0, count):
                print("\n")
                print(name[i])
                print("Стадия роста: {}".format(GardenBedAndTrees.__fruits_in_garden[i].info_height))
                print("Уровень воды: {}".format(GardenBedAndTrees.__fruits_in_garden[i].info_lever_of_water))
                print("Очки здоровья: {}".format(GardenBedAndTrees.__fruits_in_garden[i].info_lever_of_hp))
                print("Вредители: {}".format(GardenBedAndTrees.__vermin_of_fruits[i].info_condition))
                print("Болезни: {}".format(GardenBedAndTrees.__illness_of_fruits[i].info_condition))
            print("---------------------------------------")


class SeedBed(GardenBedAndTrees):

    def __init__(self, way: str = 'vegetables_in_garden.txt', param: int = 0) -> None:
        names_of_all_objects = GardenBedAndTrees.names(way)
        GardenBedAndTrees.return_weeds_to_the_garden(names_of_all_objects, param)
        super().__init__(way, param)


class Orchard(GardenBedAndTrees):

    def __init__(self, way: str = 'fruits_in_garden.txt', param: int = 1) -> None:
        super().__init__(way, param)
