class Actions:

    def __init__(self, action: str) -> None:
        self.__offer = action

    def using_actions(self) -> None:
        print(self.__offer)


class Fertilizer(Actions):

    def __init__(self, action: str = "Удобрение применено. Пошёл активный рост") -> None:
        super().__init__(action)


class Watering(Actions):

    def __init__(self, action: str = "Произведён полив. Плод обогащён водой") -> None:
        super().__init__(action)


class Weeding(Actions):

    def __init__(self, action: str = "Произведенна прополка. Сорняки обезвреженны") -> None:
        super().__init__(action)
