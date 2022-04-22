import random
from Save_and_del import *


class PoorConditions:

    def __init__(self, name: str, del_name: str, default: str, bad_status: str, creation: int = 0,
                 param: int = 0) -> None:
        self.__del_name: str = del_name
        self.__default: str = default
        self.__bad_status: str = bad_status
        if creation == 0:
            self.__name: str = name
            self.__condition: str = ReadOverwritingPoorConditions.read_overwriting_for_init(name, del_name,
                                                                                            default, creation,
                                                                                            param)
        elif creation == 1:
            self.__name: str = name
            self.__condition: str = default
            ReadOverwritingPoorConditions.read_overwriting_for_init(name, del_name,
                                                                    default, creation,
                                                                    param)

    @property
    def info_condition(self) -> str:
        return self.__condition

    def remove_condition(self, param: int) -> None:
        self.__condition = self.__default
        ReadOverwritingPoorConditions.overwriting(self.__name, self.__del_name,
                                                  self.__default,
                                                  param)

    def changing_condition(self, param: int) -> None:
        status = range(1, 22)
        condition_appearance: tuple[int, int, int, int, int, int, int, int] = 1, 3, 4, 7, 12, 17, 20, 21
        i = random.choice(status)
        if self.__condition == self.__bad_status:
            pass
        elif self.__condition != self.__bad_status:
            for w in condition_appearance:
                if i == w:
                    self.__condition = self.__bad_status
                    ReadOverwritingPoorConditions.overwriting(self.__name, self.__del_name,
                                                              self.__bad_status,
                                                              param)
                    break

    def del_condition(self, param: int) -> None:
        ReadOverwritingPoorConditions.deletion(self.__name, self.__del_name, param)


class Weeds(PoorConditions):

    def __init__(self, name: str, del_name: str = "condition_weeds", default: str = "Все хорошо, никаких сорняков",
                 bad_status: str = "Появились сорняки, требуется прополка", creation: int = 0,
                 param: int = 0) -> None:
        super().__init__(name, del_name, default, bad_status, creation, param)


class Vermin(PoorConditions):

    def __init__(self, name: str, del_name: str = "condition_vermin", default: str = "Все хорошо, никаких вредителей",
                 bad_status: str = "Появились вредители, требуется попшыкать специальным средством", creation: int = 0,
                 param: int = 0) -> None:
        super().__init__(name, del_name, default, bad_status, creation, param)


class Illness(PoorConditions):

    def __init__(self, name: str, del_name: str = "condition_illness", default: str = "Все хорошо, никаких болезней",
                 bad_status: str = "Появилась болезнь, требуется опрыскивание специальным средством", creation: int = 0,
                 param: int = 0) -> None:
        super().__init__(name, del_name, default, bad_status, creation, param)


if __name__ == '__main__':
    test1 = Weeds(name="морковка", creation=0, param=0)
    test2 = Vermin(name="морковка", creation=0, param=0)
    test2_2 = Vermin(name="груша", creation=0, param=1)
    test3 = Illness(name="морковка", creation=0, param=0)
    test3_3 = Illness(name="груша", creation=0, param=1)
