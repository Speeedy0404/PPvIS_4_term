import random
from Save_and_del import *


def how_many_days_to_grow() -> int:
    numbers_of_days = range(12, 30)
    number = random.choice(numbers_of_days)
    numbers = (number // 6)
    numbers = numbers * 6
    variable = number - numbers
    number = number - variable
    return int(number)


def how_many_days_until_the_next_stage(number: int) -> int:
    inteval = number / 6
    return int(inteval)


class SeedsAndTrees:

    def __init__(self, name: str, creation: int, param: int) -> None:
        if creation == 0:
            parameters = ReadOverwritingSeeds.read_overwriting_for_init(name, creation, param)
            self.__height = parameters[0]
            self.__name = parameters[1]
            self.__level_water = parameters[2]
        elif creation == 1:
            if param == 0:
                self.__name = name
                self.__height = "Первые 2-3 настоящих листа"
                self.__level_water = 5
                ReadOverwritingSeeds.read_overwriting_for_init(name, creation, param)
                self.__growth_stage = ("Первые 2-3 настоящих листа", "Рост",
                                       "Фаза активного вегетационного роста", "Цветение",
                                       "Формирование плода", "Вызревание плода", "Плод созрел")
            elif param == 1:
                self.__name = name
                self.__height = "Семечко в земле"
                self.__level_water = 5
                ReadOverwritingSeeds.read_overwriting_for_init(name, creation, param)
                self.__growth_stage = ("Семечко в земле", "Рост",
                                       "Первые 2-3 листочка", "Появился не крепкий ствол",
                                       "Период роста", "Период вызревания", "Период плодоношения")

    @property
    def info_name(self) -> str:
        return self.__name

    @info_name.setter
    def info_name(self, name: str) -> None:
        if isinstance(name, str):
            self.__name = name
        else:
            print("Название должно быть строкой")

    @property
    def info_height(self) -> str:
        return self.__height

    def fetal_growth(self, stage: int, param: int) -> None:
        if param == 0:
            growth_stage = ("Первые 2-3 настоящих листа", "Рост",
                            "Фаза активного вегетационного роста", "Цветение",
                            "Формирование плода", "Вызревание плода", "Плод созрел")
            self.__height = growth_stage[stage]
            ReadOverwritingSeeds.overwriting(self.__height, self.__name, self.__level_water, param)
        elif param == 1:
            growth_stage = ("Семечко в земле", "Рост",
                            "Первые 2-3 листочка", "Появился не крепкий ствол",
                            "Период роста", "Период вызревания", "Период плодоношения")
            self.__height = growth_stage[stage]
            ReadOverwritingSeeds.overwriting(self.__height, self.__name, self.__level_water, param)

    @property
    def info_lever_of_water(self) -> int:
        return self.__level_water

    def change_level_of_water(self, value: int = -1, param: int = 0) -> int:
        self.__level_water = self.__level_water + value
        if self.__level_water < 0:
            self.__level_water = 0
            return 0
        elif self.__level_water > 5:
            self.__level_water = 5
        elif self.__level_water == 0:
            return 0
        ReadOverwritingSeeds.overwriting(self.__height, self.__name, self.__level_water, param)


class GrowthAndDeath(SeedsAndTrees):

    def __init__(self, name: str, creation: int, param: int) -> None:
        if creation == 0:
            parameters = ReadOverwritingGrowthAndDeath.read_overwriting_for_init(name, creation, param)
            self.__day = parameters[0]
            self.__how_many_days_to_grow = parameters[1]
            self.__how_many_days_until_the_next_stage = parameters[2]
            self.__hp = parameters[3]
        elif creation == 1:
            self.__day = 0
            self.__how_many_days_to_grow = how_many_days_to_grow()
            number = self.info_day
            self.__how_many_days_until_the_next_stage = how_many_days_until_the_next_stage(number)
            self.__hp = 9
            ReadOverwritingGrowthAndDeath.read_overwriting_for_init(name, creation, param, self.__how_many_days_to_grow,
                                                                    self.__how_many_days_until_the_next_stage)
        super().__init__(name, creation, param)

    def del_object(self, param: int) -> None:
        name = self.info_name
        ReadOverwritingGrowthAndDeath.deletion(name, param)

    def change_hp(self, param: int) -> int:
        self.__hp += -1
        ReadOverwritingGrowthAndDeath.overwriting(self.info_name, self.__day, self.__how_many_days_to_grow,
                                                  self.__how_many_days_until_the_next_stage, self.__hp, param)
        if self.__hp == 0:
            return 0
        else:
            return 1

    def regeneration_hp(self, param: int) -> None:
        self.__hp = 9
        ReadOverwritingGrowthAndDeath.overwriting(self.info_name, self.__day, self.__how_many_days_to_grow,
                                                  self.__how_many_days_until_the_next_stage, self.__hp, param)

    @property
    def info_lever_of_hp(self) -> int:
        return self.__hp

    @property
    def info_day(self) -> int:
        return self.__how_many_days_to_grow

    @property
    def info_how_many_days_until_the_next_stage(self) -> int:
        return self.__how_many_days_until_the_next_stage

    @property
    def day_today(self) -> int:
        return self.__day

    def change_day_today(self, i: int, param: int) -> None:
        self.__day = i
        ReadOverwritingGrowthAndDeath.overwriting(self.info_name, self.__day, self.__how_many_days_to_grow,
                                                  self.__how_many_days_until_the_next_stage, self.__hp, param)

    def next_day(self, param: int) -> int:
        if param == 0:
            if self.info_height == "Плод созрел":
                self.__day += 1
                ReadOverwritingGrowthAndDeath.overwriting(self.info_name, self.__day, self.__how_many_days_to_grow,
                                                          self.__how_many_days_until_the_next_stage, self.__hp, param)
                count = self.__day - self.__how_many_days_to_grow
                if self.info_height == "Плод созрел" and count == 3:
                    return 0
                else:
                    return 1
            else:
                self.__day += 1
                ReadOverwritingGrowthAndDeath.overwriting(self.info_name, self.__day, self.__how_many_days_to_grow,
                                                          self.__how_many_days_until_the_next_stage, self.__hp, param)
                for i in range(1, 7):
                    if self.__day == self.__how_many_days_until_the_next_stage * i:
                        self.fetal_growth(i, param)
        elif param == 1:

            if self.info_height == "Период плодоношения":
                self.__day += 1
                ReadOverwritingGrowthAndDeath.overwriting(self.info_name, self.__day, self.__how_many_days_to_grow,
                                                          self.__how_many_days_until_the_next_stage, self.__hp, param)
                count = self.__day - self.__how_many_days_to_grow
                if self.info_height == "Период плодоношения" and count == 3:
                    return 0
                else:
                    return 1

            else:
                self.__day += 1
                ReadOverwritingGrowthAndDeath.overwriting(self.info_name, self.__day, self.__how_many_days_to_grow,
                                                          self.__how_many_days_until_the_next_stage, self.__hp, param)
                for i in range(1, 7):
                    if self.__day == self.__how_many_days_until_the_next_stage * i:
                        self.fetal_growth(i, param)


class Vegetables(GrowthAndDeath):

    def __init__(self, name: str, creation: int, param: int) -> None:
        super().__init__(name, creation, param)


class Fruits(GrowthAndDeath):

    def __init__(self, name: str, creation: int, param: int) -> None:
        super().__init__(name, creation, param)
