import random
from typing import List
from save_and_del import *
from dictionary import dictionary


class Weather:

    def __init__(self) -> None:
        self.__weather: str = ReadOverwritingWeather.read_for_init()
        self.__status: List[str] = [dictionary["weather_1"],
                                    dictionary["weather_2"], dictionary["weather_3"],
                                    dictionary["weather_4"], dictionary["weather_5"]]

    @property
    def info_weather(self) -> str:
        return self.__weather

    def changing_the_weather(self) -> None:
        self.__weather = random.choice(self.__status)
        ReadOverwritingWeather.overwriting(self.__weather)
