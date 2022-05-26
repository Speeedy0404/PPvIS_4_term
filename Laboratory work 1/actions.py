from dictionary import dictionary


class Actions:

    def __init__(self, action: str) -> None:
        self.__offer = action

    def using_actions(self) -> None:
        print(self.__offer)


class Fertilizer(Actions):

    def __init__(self, action: str = dictionary["fertilizer"]) -> None:
        super().__init__(action)


class Watering(Actions):

    def __init__(self, action: str = dictionary["watering"]) -> None:
        super().__init__(action)


class Weeding(Actions):

    def __init__(self, action: str = dictionary["weeding"]) -> None:
        super().__init__(action)
