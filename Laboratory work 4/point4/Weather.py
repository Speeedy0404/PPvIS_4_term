import random
from Save_and_del import *


class Weather:

    def __init__(self) -> None:
        self.__weather: str = ReadOverwritingWeather.read_for_init()
        self.__status: tuple[str, ...] = "Cолнце", "Дождь", "Очень сильная жара(засуха)", "Морось", "Пасмурно"

    @property
    def info_weather(self) -> str:
        return self.__weather

    def changing_the_weather(self) -> None:
        self.__weather = random.choice(self.__status)
        ReadOverwritingWeather.overwriting(self.__weather)
