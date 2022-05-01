from Vegetables_and_trees import *
from view_cli import *
from weeds_vermin_illness import *


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
    def objects_in_garden(position: int, param: int) -> str:
        if param == 0:
            return GardenBedAndTrees.__vegetables_in_garden[position].info_name
        elif param == 1:
            return GardenBedAndTrees.__fruits_in_garden[position].info_name

    @staticmethod
    def check_weeds(position: int) -> int:
        if GardenBedAndTrees.__weeds_of_vegetables[position].info_condition == "Сорняков нет":
            return 0
        else:
            return 1

    @staticmethod
    def regeneration_weeds(position: int, param: int) -> None:
        GardenBedAndTrees.__weeds_of_vegetables[position].remove_condition(param)

    @staticmethod
    def check_illness(position: int, param: int) -> int:
        if param == 0:
            if GardenBedAndTrees.__illness_of_vegetables[position].info_condition == "Болезней нет":
                return 0
            else:
                return 1
        elif param == 1:
            if GardenBedAndTrees.__illness_of_fruits[position].info_condition == "Болезней нет":
                return 0
            else:
                return 1

    @staticmethod
    def regeneration_illness(position: int, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__illness_of_vegetables[position].remove_condition(param)
        elif param == 1:
            GardenBedAndTrees.__illness_of_fruits[position].remove_condition(param)

    @staticmethod
    def check_vermin(position: int, param: int) -> int:
        if param == 0:
            if GardenBedAndTrees.__vermin_of_vegetables[position].info_condition == "Вредителей нет":
                return 0
            else:
                return 1
        elif param == 1:
            if GardenBedAndTrees.__vermin_of_fruits[position].info_condition == "Вредителей нет":
                return 0
            else:
                return 1

    @staticmethod
    def regeneration_vermin(position: int, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vermin_of_vegetables[position].remove_condition(param)
        elif param == 1:
            GardenBedAndTrees.__vermin_of_fruits[position].remove_condition(param)

    @staticmethod
    def check_level_of_water(position: int, param: int) -> int:
        if param == 0:
            number = GardenBedAndTrees.__vegetables_in_garden[position].info_lever_of_water
            if number == 5:
                return 0
            else:
                number = 5 - number
                return number
        elif param == 1:
            number = GardenBedAndTrees.__fruits_in_garden[position].info_lever_of_water
            if number == 5:
                return 0
            else:
                number = 5 - number
                return number

    @staticmethod
    def regenerate_level_of_water(position: int, level_of_water: int, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden[position].change_level_of_water(level_of_water, param)
        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden[position].change_level_of_water(level_of_water, param)

    @staticmethod
    def check_height(position: int, param: int) -> str:
        if param == 0:
            return GardenBedAndTrees.__vegetables_in_garden[position].info_height

        if param == 1:
            return GardenBedAndTrees.__fruits_in_garden[position].info_height

    @staticmethod
    def change_height(position: int, param: int) -> None:
        days_delta: int = 0
        growth_delta: int = 0
        growth_stage = []
        current_height = ''
        days_until_the_next_stage = 0

        if param == 0:
            growth_stage = ("Первые 2-3 настоящих листа", "Рост",
                            "Фаза активного вегетационного роста", "Цветение",
                            "Формирование плода", "Вызревание плода",
                            "Плод созрел")

            current_height = GardenBedAndTrees.__vegetables_in_garden[position].info_height
            days_until_the_next_stage = GardenBedAndTrees.__vegetables_in_garden[
                position].info_about_of_days_until_the_next_stage

        elif param == 1:
            growth_stage = ("Семечко в земле", "Рост",
                            "Первые 2-3 листочка",
                            "Появился не крепкий ствол",
                            "Период роста", "Период вызревания",
                            "Период плодоношения")

            current_height: str = GardenBedAndTrees.__fruits_in_garden[position].info_height
            days_until_the_next_stage: int = GardenBedAndTrees.__fruits_in_garden[
                position].info_about_of_days_until_the_next_stage

        for i in range(0, 7):
            if current_height == growth_stage[i]:
                days_delta: int = days_until_the_next_stage * (i + 1)
                growth_delta: int = i + 1
                break

        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden[position].change_day_today(days_delta, param)
            GardenBedAndTrees.__vegetables_in_garden[position].fetal_growth(growth_delta, param)
        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden[position].change_day_today(days_delta, param)
            GardenBedAndTrees.__fruits_in_garden[position].fetal_growth(growth_delta, param)

    @staticmethod
    def the_objects_is_cured(position: int, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden[position].regeneration_hp(param)
        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden[position].regeneration_hp(param)

    @staticmethod
    def names(way: str) -> list:
        names = ReadOverwritingGardenBedAndTrees.read(way)
        return names

    @staticmethod
    def return_objects_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden.clear()
            for i in names:
                GardenBedAndTrees.__vegetables_in_garden.append(Vegetables(i, 0, param))
        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden.clear()
            for i in names:
                GardenBedAndTrees.__fruits_in_garden.append(Fruits(i, 0, param))

    @staticmethod
    def return_vermin_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vermin_of_vegetables.clear()
            for i in names:
                GardenBedAndTrees.__vermin_of_vegetables.append(Vermin(name=i, creation=0, param=param))
        elif param == 1:
            GardenBedAndTrees.__vermin_of_fruits.clear()
            for i in names:
                GardenBedAndTrees.__vermin_of_fruits.append(Vermin(name=i, creation=0, param=param))

    @staticmethod
    def return_illness_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__illness_of_vegetables.clear()
            for i in names:
                GardenBedAndTrees.__illness_of_vegetables.append(Illness(name=i, creation=0, param=param))
        elif param == 1:
            GardenBedAndTrees.__illness_of_fruits.clear()
            for i in names:
                GardenBedAndTrees.__illness_of_fruits.append(Illness(name=i, creation=0, param=param))

    @staticmethod
    def return_weeds_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__weeds_of_vegetables.clear()
            for i in names:
                GardenBedAndTrees.__weeds_of_vegetables.append(Weeds(name=i, creation=0, param=param))

    @staticmethod
    def new_object(name: str, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden.append(Vegetables(name, 1, param))
            GardenBedAndTrees.__vermin_of_vegetables.append(Vermin(Globals.name_of_object, creation=1, param=param))
            GardenBedAndTrees.__illness_of_vegetables.append(Illness(Globals.name_of_object, creation=1, param=param))
            GardenBedAndTrees.__weeds_of_vegetables.append(Weeds(Globals.name_of_object, creation=1, param=param))

            number = len(GardenBedAndTrees.__vegetables_in_garden) - 1
            GardenBedAndTrees.__vegetables_in_garden[number].info_name = Globals.name_of_object

        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden.append(Fruits(name, 1, param))
            GardenBedAndTrees.__vermin_of_fruits.append(Vermin(Globals.name_of_object, creation=1, param=param))
            GardenBedAndTrees.__illness_of_fruits.append(Illness(Globals.name_of_object, creation=1, param=param))

            number = len(GardenBedAndTrees.__fruits_in_garden) - 1
            GardenBedAndTrees.__fruits_in_garden[number].info_name = Globals.name_of_object

    @staticmethod
    def show_information_about_objects(param: int, gui=False, root=None, list_object=None, label=None) -> None:
        iterations = None
        if gui:
            iterations = len(list_object)
        if gui:
            if param == 0:
                list_object.append(label(text="---------------------------------------"))
                root.inffo.add_widget(list_object[iterations])
                iterations += 1
            elif param == 1:
                list_object.append(label(text="---------------------------------------"))
                root.fruits.add_widget(list_object[iterations])
                iterations += 1
            if param == 0:
                list_object.append(label(text="Вот какие виды растут на грядке: "))
                root.inffo.add_widget(list_object[iterations])
            elif param == 1:
                list_object.append(label(text="Вот какие деревья растут в саду: "))
                root.fruits.add_widget(list_object[iterations])
        if param == 0:
            if gui:
                number: int = len(GardenBedAndTrees.__vegetables_in_garden)
                for i in range(0, number):
                    iterations += 1
                    list_object.append(label(text=GardenBedAndTrees.objects_in_garden(i, param)))
                    root.inffo.add_widget(list_object[iterations])
            elif gui is False:
                message = "Вот какие виды растут на грядке: "
                print("---------------------------------------")
                print(message)
                number: int = len(GardenBedAndTrees.__vegetables_in_garden)
                for i in range(0, number):
                    print(GardenBedAndTrees.objects_in_garden(i, param))
        elif param == 1:
            if gui:
                number: int = len(GardenBedAndTrees.__fruits_in_garden)
                for i in range(0, number):
                    iterations += 1
                    list_object.append(label(text=GardenBedAndTrees.objects_in_garden(i, param)))
                    root.fruits.add_widget(list_object[iterations])
            elif gui is False:
                message = "Вот какие деревья растут в саду: "
                print("---------------------------------------")
                print(message)
                number: int = len(GardenBedAndTrees.__fruits_in_garden)
                for i in range(0, number):
                    print(GardenBedAndTrees.objects_in_garden(i, param))

    def change_of_day(self, param: int, show_next_day_view=None, gui=False) -> None:
        if param == 0:
            if gui:
                name: list[str] = GardenBedAndTrees.names(self.__way)
                count: int = len(name)
                removal: int = 0
                for i in range(0, count):
                    i: int = i + removal
                    error: int = GardenBedAndTrees.__vegetables_in_garden[i].next_day(param)
                    if error == 0:
                        show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                           "Сгнил из-за того что вы его не собрали")
                        GardenBedAndTrees.deleting_information(i, param)
                        removal += -1

                name: list[str] = GardenBedAndTrees.names(self.__way)
                count: int = len(name)
                removal: int = 0
                for i in range(0, count):
                    i: int = i + removal
                    count1: int = 0
                    GardenBedAndTrees.__vermin_of_vegetables[i].changing_condition(param)
                    GardenBedAndTrees.__illness_of_vegetables[i].changing_condition(param)
                    GardenBedAndTrees.__weeds_of_vegetables[i].changing_condition(param)

                    if GardenBedAndTrees.__vermin_of_vegetables[i].info_condition == "Появились вредители":
                        error: int = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                        if error == 0:
                            show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                               "Был утерян из-за вредителей")
                            GardenBedAndTrees.deleting_information(i, param)
                            removal += -1
                            count1 = 1

                    if count1 == 0:
                        if GardenBedAndTrees.__illness_of_vegetables[i].info_condition == "Появилась болезнь":
                            error = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                            if error == 0:
                                show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                   "Был утерян из-за болезней")
                                GardenBedAndTrees.deleting_information(i, param)
                                removal += -1
                                count1 = 1

                    if count1 == 0:
                        if GardenBedAndTrees.__weeds_of_vegetables[i].info_condition == "Появились сорняки":
                            error = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                            if error == 0:
                                show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                   "Был утерян из-за сорняков")
                                GardenBedAndTrees.deleting_information(i, param)
                                removal += -1
                                count1 = 1

                    if count1 == 0:
                        if GardenBedAndTrees.check_weeds(i) == 0 and GardenBedAndTrees.check_vermin(i, param) \
                                == 0 and GardenBedAndTrees.check_illness(i, param) == 0:
                            GardenBedAndTrees.the_objects_is_cured(i, param)
            elif gui is False:
                name: list[str] = GardenBedAndTrees.names(self.__way)
                count: int = len(name)
                removal: int = 0
                for i in range(0, count):
                    i: int = i + removal
                    error: int = GardenBedAndTrees.__vegetables_in_garden[i].next_day(param)
                    if error == 0:
                        show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                           'Сгнил из-за того что вы его не собрали')

                        GardenBedAndTrees.deleting_information(i, param)
                        removal += -1

                name: list[str] = GardenBedAndTrees.names(self.__way)
                count: int = len(name)
                removal: int = 0
                for i in range(0, count):
                    i: int = i + removal
                    count1: int = 0
                    GardenBedAndTrees.__vermin_of_vegetables[i].changing_condition(param)
                    GardenBedAndTrees.__illness_of_vegetables[i].changing_condition(param)
                    GardenBedAndTrees.__weeds_of_vegetables[i].changing_condition(param)

                    if GardenBedAndTrees.__vermin_of_vegetables[i].info_condition == "Появились вредители":
                        error: int = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                        if error == 0:
                            show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                               'Был утерян из-за вредителей')
                            GardenBedAndTrees.deleting_information(i, param)
                            removal += -1
                            count1 = 1

                    if count1 == 0:
                        if GardenBedAndTrees.__illness_of_vegetables[i].info_condition == "Появилась болезнь":
                            error = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                            if error == 0:
                                show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                   'Был утерян из-за болезней')
                                GardenBedAndTrees.deleting_information(i, param)
                                removal += -1
                                count1 = 1

                    if count1 == 0:
                        if GardenBedAndTrees.__weeds_of_vegetables[i].info_condition == "Появились сорняки":
                            error = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                            if error == 0:
                                show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                   'Был утерян из-за сорняков')
                                GardenBedAndTrees.deleting_information(i, param)
                                removal += -1
                                count1 = 1

                    if count1 == 0:
                        if GardenBedAndTrees.check_weeds(i) == 0 and GardenBedAndTrees.check_vermin(i, param) \
                                == 0 and GardenBedAndTrees.check_illness(i, param) == 0:
                            GardenBedAndTrees.the_objects_is_cured(i, param)
        elif param == 1:
            if gui:
                name: list[str] = GardenBedAndTrees.names(self.__way)
                count: int = len(name)
                removal: int = 0
                for i in range(0, count):
                    i: int = i + removal
                    error: int = GardenBedAndTrees.__fruits_in_garden[i].next_day(param)
                    if error == 0:
                        show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                           "Вы долго не собирали созревшие плоды с дерева из-за этого оно увяло")
                        GardenBedAndTrees.deleting_information(i, param)
                        removal += -1

                name: list[str] = GardenBedAndTrees.names(self.__way)
                count: int = len(name)
                removal: int = 0
                for i in range(0, count):
                    i: int = i + removal
                    count1: int = 0
                    GardenBedAndTrees.__vermin_of_fruits[i].changing_condition(param)
                    GardenBedAndTrees.__illness_of_fruits[i].changing_condition(param)

                    if GardenBedAndTrees.__vermin_of_fruits[i].info_condition == "Появились вредители":
                        error: int = GardenBedAndTrees.__fruits_in_garden[i].change_hp(param)
                        if error == 0:
                            show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                               "Было утерян из-за вредителей")
                            GardenBedAndTrees.deleting_information(i, param)
                            removal += -1
                            count1 = 1

                    if count1 == 0:
                        if GardenBedAndTrees.__illness_of_fruits[i].info_condition == "Появилась болезнь":
                            error: int = GardenBedAndTrees.__fruits_in_garden[i].change_hp(param)
                            if error == 0:
                                show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                   "Было утерян из-за болезней")
                                GardenBedAndTrees.deleting_information(i, param)
                                removal += -1
                                count1 = 1
                    if count1 == 0:
                        if GardenBedAndTrees.check_vermin(i, param) == 0 and \
                                GardenBedAndTrees.check_illness(i, param) == 0:
                            GardenBedAndTrees.the_objects_is_cured(i, param)
            elif gui is False:
                name: list[str] = GardenBedAndTrees.names(self.__way)
                count: int = len(name)
                removal: int = 0
                for i in range(0, count):
                    i: int = i + removal
                    error: int = GardenBedAndTrees.__fruits_in_garden[i].next_day(param)
                    if error == 0:
                        show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                           'Вы долго не собирали созревшие плоды с дерева из-за этого оно увяло')
                        GardenBedAndTrees.deleting_information(i, param)
                        removal += -1

                name: list[str] = GardenBedAndTrees.names(self.__way)
                count: int = len(name)
                removal: int = 0
                for i in range(0, count):
                    i: int = i + removal
                    count1: int = 0
                    GardenBedAndTrees.__vermin_of_fruits[i].changing_condition(param)
                    GardenBedAndTrees.__illness_of_fruits[i].changing_condition(param)

                    if GardenBedAndTrees.__vermin_of_fruits[i].info_condition == "Появились вредители":
                        error: int = GardenBedAndTrees.__fruits_in_garden[i].change_hp(param)
                        if error == 0:
                            show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                               'Было утерян из-за вредителей')
                            GardenBedAndTrees.deleting_information(i, param)
                            removal += -1
                            count1 = 1

                    if count1 == 0:
                        if GardenBedAndTrees.__illness_of_fruits[i].info_condition == "Появилась болезнь":
                            error: int = GardenBedAndTrees.__fruits_in_garden[i].change_hp(param)
                            if error == 0:
                                show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                   'Было утерян из-за болезней')
                                GardenBedAndTrees.deleting_information(i, param)
                                removal += -1
                                count1 = 1
                    if count1 == 0:
                        if GardenBedAndTrees.check_vermin(i, param) == 0 and \
                                GardenBedAndTrees.check_illness(i, param) == 0:
                            GardenBedAndTrees.the_objects_is_cured(i, param)

    @staticmethod
    def changing_the_water_from_the_weather(weather, param: int,
                                            show_next_day_view=ViewPrint.show_next_day_view, ) -> None:
        weather_of_the_day = weather.info_weather
        if weather_of_the_day == "Cолнце":
            number: int = -2
            GardenBedAndTrees.changing(number, param, show_next_day_view)
        elif weather_of_the_day == "Дождь":
            number: int = 3
            GardenBedAndTrees.changing(number, param, show_next_day_view)
        elif weather_of_the_day == "Очень сильная жара(засуха)":
            number: int = -3
            GardenBedAndTrees.changing(number, param, show_next_day_view)
        elif weather_of_the_day == "Морось":
            number: int = 1
            GardenBedAndTrees.changing(number, param, show_next_day_view)
        elif weather_of_the_day == "Пасмурно":
            number: int = -1
            GardenBedAndTrees.changing(number, param, show_next_day_view)

    @staticmethod
    def changing(number: int, param: int, show_next_day_view=ViewPrint.show_next_day_view) -> None:
        way = None
        message = None

        if param == 0:
            way = 'vegetables'
            message = "Рассада усохла из-за нехватки воды"
        elif param == 1:
            way = 'fruits'
            message = "Дерево усохло из-за нехватки воды"

        name: list[str] = GardenBedAndTrees.names(way)
        count: int = len(name)
        removal: int = 0
        some_object = None

        if param == 0:
            some_object = GardenBedAndTrees.__vegetables_in_garden
        elif param == 1:
            some_object = GardenBedAndTrees.__fruits_in_garden

        for i in range(0, count):
            i = i + removal
            error: int = some_object[i].change_level_of_water(number, param)
            if error == 0:
                show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                   message)
                GardenBedAndTrees.deleting_information(i, param)
                removal += -1

    @staticmethod
    def deleting_information(position: int, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden[position].del_object(param)
            GardenBedAndTrees.__vegetables_in_garden.pop(position)
            GardenBedAndTrees.__vermin_of_vegetables.pop(position)
            GardenBedAndTrees.__illness_of_vegetables.pop(position)
            GardenBedAndTrees.__weeds_of_vegetables.pop(position)

        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden[position].del_object(param)
            GardenBedAndTrees.__fruits_in_garden.pop(position)
            GardenBedAndTrees.__vermin_of_fruits.pop(position)
            GardenBedAndTrees.__illness_of_fruits.pop(position)

    @staticmethod
    def status(param: int, gui=False, root=None, list_objects=None, label=None) -> None:

        name = []
        count = 0
        iterations = None
        if gui:
            iterations = len(list_objects)
        screen = None
        garden = None
        vermin = None
        illness = None

        if param == 0:
            if gui:
                way = 'vegetables'
                list_objects.append(label(text="---------------------------------------"))
                root.inffo.add_widget(list_objects[iterations])
                iterations += 1
                list_objects.append(label(text="Вот информация о состоянии каждого вида: "))
                root.inffo.add_widget(list_objects[iterations])
                name = GardenBedAndTrees.names(way)
                count: int = len(name)

            elif gui is False:
                way = 'vegetables'
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
            if gui:
                way = 'fruits'
                list_objects.append(label(text="---------------------------------------"))
                root.fruits.add_widget(list_objects[iterations])
                iterations += 1
                list_objects.append(label(text="Вот информация о состоянии каждого дерева: "))
                root.fruits.add_widget(list_objects[iterations])
                name = GardenBedAndTrees.names(way)
                count: int = len(name)

            elif gui is False:
                way = 'fruits'
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

        if param == 0:
            if gui:
                screen = root.inffo
                garden = GardenBedAndTrees.__vegetables_in_garden
                vermin = GardenBedAndTrees.__vermin_of_vegetables
                illness = GardenBedAndTrees.__illness_of_vegetables

        elif param == 1:
            if gui:
                screen = root.fruits
                garden = GardenBedAndTrees.__fruits_in_garden
                vermin = GardenBedAndTrees.__vermin_of_fruits
                illness = GardenBedAndTrees.__illness_of_fruits

        if gui:
            for i in range(0, count):
                iterations += 1
                list_objects.append(label(text=name[i]))
                screen.add_widget(list_objects[iterations])
                iterations += 1
                list_objects.append(
                    label(text="Стадия роста: {}".format(garden[i].info_height)))
                screen.add_widget(list_objects[iterations])
                iterations += 1
                list_objects.append(label(
                    text="Уровень воды: {}".format(garden[i].info_lever_of_water)))
                screen.add_widget(list_objects[iterations])
                iterations += 1
                list_objects.append(label(
                    text="Очки здоровья: {}".format(garden[i].info_lever_of_hp)))
                screen.add_widget(list_objects[iterations])
                iterations += 1
                list_objects.append(
                    label(text="Вредители: {}".format(vermin[i].info_condition)))
                screen.add_widget(list_objects[iterations])
                iterations += 1
                list_objects.append(
                    label(text="Болезни: {}".format(illness[i].info_condition)))
                screen.add_widget(list_objects[iterations])
                if screen == root.inffo:
                    iterations += 1
                    list_objects.append(
                        label(text="Сорняки: {}".format(GardenBedAndTrees.__weeds_of_vegetables[i].info_condition)))
                    screen.add_widget(list_objects[iterations])
                iterations += 1
                list_objects.append(
                    label(text="---------------------------------------"))
                screen.add_widget(list_objects[iterations])
            iterations += 1
            list_objects.append(label(text="---------------------------------------"))
            screen.add_widget(list_objects[iterations])


class SeedBed(GardenBedAndTrees):

    def __init__(self, way: str = 'vegetables', param: int = 0) -> None:
        names_of_all_objects = GardenBedAndTrees.names(way)
        GardenBedAndTrees.return_weeds_to_the_garden(names_of_all_objects, param)
        super().__init__(way, param)


class Orchard(GardenBedAndTrees):

    def __init__(self, way: str = 'fruits', param: int = 1) -> None:
        super().__init__(way, param)
