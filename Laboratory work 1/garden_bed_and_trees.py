from vegetables_and_trees import *
from weeds_vermin_illness import *
from save_and_del import *
from view_cli import *
from dictionary import dictionary


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
        if GardenBedAndTrees.__weeds_of_vegetables[position].info_condition == dictionary["no_weeds"]:
            return 0
        else:
            return 1

    @staticmethod
    def regeneration_weeds(position: int, param: int) -> None:
        GardenBedAndTrees.__weeds_of_vegetables[position].remove_condition(param)

    @staticmethod
    def check_illness(position: int, param: int) -> int:
        if param == 0:
            if GardenBedAndTrees.__illness_of_vegetables[position].info_condition == dictionary["no_illness"]:
                return 0
            else:
                return 1
        elif param == 1:
            if GardenBedAndTrees.__illness_of_fruits[position].info_condition == dictionary["no_illness"]:
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
            if GardenBedAndTrees.__vermin_of_vegetables[position].info_condition == dictionary["no_vermin"]:
                return 0
            else:
                return 1
        elif param == 1:
            if GardenBedAndTrees.__vermin_of_fruits[position].info_condition == dictionary["no_vermin"]:
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
        i_delta: int = 0
        i_growth: int = 0
        growth_stage = []
        height_delta = ''
        count = 0

        if param == 0:
            growth_stage = (dictionary["seed_stage_1"],
                            dictionary["seed_stage_2"], dictionary["seed_stage_3"],
                            dictionary["seed_stage_4"], dictionary["seed_stage_5"],
                            dictionary["seed_stage_6"], dictionary["seed_stage_7"])

            height_delta = GardenBedAndTrees.__vegetables_in_garden[position].info_height
            count = GardenBedAndTrees.__vegetables_in_garden[position].info_days_until_the_next_stage

        elif param == 1:
            growth_stage = (dictionary["fruit_stage_1"],
                            dictionary["fruit_stage_2"], dictionary["fruit_stage_3"],
                            dictionary["fruit_stage_4"], dictionary["fruit_stage_5"],
                            dictionary["fruit_stage_6"], dictionary["fruit_stage_7"])

            height_delta: str = GardenBedAndTrees.__fruits_in_garden[position].info_height
            count: int = GardenBedAndTrees.__fruits_in_garden[position].info_days_until_the_next_stage

        for i in range(0, 7):
            if height_delta == growth_stage[i]:
                i_delta: int = count * (i + 1)
                i_growth: int = i + 1
                break

        if param == 0:
            GardenBedAndTrees.__vegetables_in_garden[position].change_day_today(i_delta, param)
            GardenBedAndTrees.__vegetables_in_garden[position].fetal_growth(i_growth, param)
        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden[position].change_day_today(i_delta, param)
            GardenBedAndTrees.__fruits_in_garden[position].fetal_growth(i_growth, param)

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
            for some_object in names:
                GardenBedAndTrees.__vegetables_in_garden.append(Vegetables(some_object, 0, param))
        elif param == 1:
            GardenBedAndTrees.__fruits_in_garden.clear()
            for some_object in names:
                GardenBedAndTrees.__fruits_in_garden.append(Fruits(some_object, 0, param))

    @staticmethod
    def return_vermin_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__vermin_of_vegetables.clear()
            for some_object in names:
                GardenBedAndTrees.__vermin_of_vegetables.append(Vermin(name=some_object, creation=0, param=param))
        elif param == 1:
            GardenBedAndTrees.__vermin_of_fruits.clear()
            for some_object in names:
                GardenBedAndTrees.__vermin_of_fruits.append(Vermin(name=some_object, creation=0, param=param))

    @staticmethod
    def return_illness_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__illness_of_vegetables.clear()
            for some_object in names:
                GardenBedAndTrees.__illness_of_vegetables.append(Illness(name=some_object, creation=0, param=param))
        elif param == 1:
            GardenBedAndTrees.__illness_of_fruits.clear()
            for some_object in names:
                GardenBedAndTrees.__illness_of_fruits.append(Illness(name=some_object, creation=0, param=param))

    @staticmethod
    def return_weeds_to_the_garden(names: list, param: int) -> None:
        if param == 0:
            GardenBedAndTrees.__weeds_of_vegetables.clear()
            for some_object in names:
                GardenBedAndTrees.__weeds_of_vegetables.append(Weeds(name=some_object, creation=0, param=param))

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
    def show_information_about_objects(param: int) -> None:

        if param == 0:
            message = dictionary["show_seed_bed"]
            print(dictionary["line"])
            print(message)
            number: int = len(GardenBedAndTrees.__vegetables_in_garden)
            for i in range(0, number):
                print(GardenBedAndTrees.objects_in_garden(i, param))
        elif param == 1:
            message = dictionary["show_orchard"]
            print(dictionary["line"])
            print(message)
            number: int = len(GardenBedAndTrees.__fruits_in_garden)
            for i in range(0, number):
                print(GardenBedAndTrees.objects_in_garden(i, param))

    def change_of_day(self, param: int) -> None:
        if param == 0:
            name: list[str] = GardenBedAndTrees.names(self.__way)
            count: int = len(name)
            removal: int = 0
            for i in range(0, count):
                i: int = i + removal
                error: int = GardenBedAndTrees.__vegetables_in_garden[i].next_day(param)
                if error == 0:
                    ViewPrint.show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                 dictionary["rotted_seed"])

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

                if GardenBedAndTrees.__vermin_of_vegetables[i].info_condition == dictionary["vermin"]:
                    error: int = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                    if error == 0:
                        ViewPrint.show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                     dictionary["killed_by_pests_seed"])
                        GardenBedAndTrees.deleting_information(i, param)
                        removal += -1
                        count1 = 1

                if count1 == 0:
                    if GardenBedAndTrees.__illness_of_vegetables[i].info_condition == dictionary["illness"]:
                        error = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                        if error == 0:
                            ViewPrint.show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                         dictionary["killed_by_disease_seed"])
                            GardenBedAndTrees.deleting_information(i, param)
                            removal += -1
                            count1 = 1

                if count1 == 0:
                    if GardenBedAndTrees.__weeds_of_vegetables[i].info_condition == dictionary["weeds"]:
                        error = GardenBedAndTrees.__vegetables_in_garden[i].change_hp(param)
                        if error == 0:
                            ViewPrint.show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                         dictionary["killed_by_weeds_seed"])
                            GardenBedAndTrees.deleting_information(i, param)
                            removal += -1
                            count1 = 1

                if count1 == 0:
                    if GardenBedAndTrees.check_weeds(i) == 0 and GardenBedAndTrees.check_vermin(i, param) \
                            == 0 and GardenBedAndTrees.check_illness(i, param) == 0:
                        GardenBedAndTrees.the_objects_is_cured(i, param)
        elif param == 1:

            name: list[str] = GardenBedAndTrees.names(self.__way)
            count: int = len(name)
            removal: int = 0
            for i in range(0, count):
                i: int = i + removal
                error: int = GardenBedAndTrees.__fruits_in_garden[i].next_day(param)
                if error == 0:
                    ViewPrint.show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                 dictionary["rotted_fruit"])
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

                if GardenBedAndTrees.__vermin_of_fruits[i].info_condition == dictionary["vermin"]:
                    error: int = GardenBedAndTrees.__fruits_in_garden[i].change_hp(param)
                    if error == 0:
                        ViewPrint.show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                     dictionary["killed_by_pests_fruit"])
                        GardenBedAndTrees.deleting_information(i, param)
                        removal += -1
                        count1 = 1

                if count1 == 0:
                    if GardenBedAndTrees.__illness_of_fruits[i].info_condition == dictionary["illness"]:
                        error: int = GardenBedAndTrees.__fruits_in_garden[i].change_hp(param)
                        if error == 0:
                            ViewPrint.show_next_day_view(GardenBedAndTrees.objects_in_garden(i, param),
                                                         dictionary["killed_by_disease_fruit"])
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
        if weather_of_the_day == dictionary["weather_1"]:
            number: int = -2
            GardenBedAndTrees.changing(number, param, show_next_day_view)
        elif weather_of_the_day == dictionary["weather_2"]:
            number: int = 3
            GardenBedAndTrees.changing(number, param, show_next_day_view)
        elif weather_of_the_day == dictionary["weather_3"]:
            number: int = -3
            GardenBedAndTrees.changing(number, param, show_next_day_view)
        elif weather_of_the_day == dictionary["weather_4"]:
            number: int = 1
            GardenBedAndTrees.changing(number, param, show_next_day_view)
        elif weather_of_the_day == dictionary["weather_5"]:
            number: int = -1
            GardenBedAndTrees.changing(number, param, show_next_day_view)

    @staticmethod
    def changing(number: int, param: int, show_next_day_view=ViewPrint.show_next_day_view) -> None:
        way = None
        message = None

        if param == 0:
            way = 'vegetables'
            message = dictionary["no_water_seed"]
        elif param == 1:
            way = 'fruits'
            message = dictionary["no_water_fruit"]

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
    def status(param: int) -> None:

        if param == 0:

            way = 'vegetables'
            print(dictionary["line"])
            print(dictionary["status_seed"])
            name: list[str] = GardenBedAndTrees.names(way)
            count: int = len(name)
            for i in range(0, count):
                print("\n")
                print(name[i])
                print(dictionary["grow_stage"].format(GardenBedAndTrees.__vegetables_in_garden[i].info_height))
                print(dictionary["level_of_water"].format(
                    GardenBedAndTrees.__vegetables_in_garden[i].info_lever_of_water))
                print(dictionary["heat_point"].format(GardenBedAndTrees.__vegetables_in_garden[i].info_lever_of_hp))
                print(dictionary["status_vermin"].format(GardenBedAndTrees.__vermin_of_vegetables[i].info_condition))
                print(dictionary["status_illness"].format(GardenBedAndTrees.__illness_of_vegetables[i].info_condition))
                print(dictionary["status_weeds"].format(GardenBedAndTrees.__weeds_of_vegetables[i].info_condition))
            print(dictionary["line"])

        elif param == 1:

            way = 'fruits'
            print(dictionary["line"])
            print(dictionary["status_fruit"])
            name: list[str] = GardenBedAndTrees.names(way)
            count: int = len(name)
            for i in range(0, count):
                print("\n")
                print(name[i])
                print(dictionary["grow_stage_fruit"].format(GardenBedAndTrees.__fruits_in_garden[i].info_height))
                print(dictionary["level_of_water_fruit"].format(
                    GardenBedAndTrees.__fruits_in_garden[i].info_lever_of_water))
                print(dictionary["heat_point_fruit"].format(GardenBedAndTrees.__fruits_in_garden[i].info_lever_of_hp))
                print(dictionary["status_vermin_fruit"].format(GardenBedAndTrees.__vermin_of_fruits[i].info_condition))
                print(
                    dictionary["status_illness_fruit"].format(GardenBedAndTrees.__illness_of_fruits[i].info_condition))
            print(dictionary["line"])


class SeedBed(GardenBedAndTrees):

    def __init__(self, way: str = 'vegetables', param: int = 0) -> None:
        names_of_all_objects = GardenBedAndTrees.names(way)
        GardenBedAndTrees.return_weeds_to_the_garden(names_of_all_objects, param)
        super().__init__(way, param)


class Orchard(GardenBedAndTrees):

    def __init__(self, way: str = 'fruits', param: int = 1) -> None:
        super().__init__(way, param)
