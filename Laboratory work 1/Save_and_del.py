import os


class ReadOverwritingSeeds:

    @staticmethod
    def read_overwriting_for_init(name: str, creation: int, param: int) -> list:
        if creation == 0:
            parameters = []
            if param == 0:
                del_name = '_seeds.txt'
            else:
                del_name = '_trees.txt'
            with open(name + del_name, 'r', encoding="utf-8") as f:
                height = f.readline()
                height = height.replace("\n", "")
                name = f.readline()
                name = name.replace("\n", "")
                level_water = int(f.readline())
                parameters.append(height)
                parameters.append(name)
                parameters.append(level_water)
                return parameters
        elif creation == 1:
            if param == 0:
                del_name = '_seeds.txt'
                height = "Первые 2-3 настоящих листа"
            else:
                del_name = '_trees.txt'
                height = "Семечко в земле"
            name = name
            level_water = 5
            with open(name + del_name, 'w', encoding="utf-8") as f:
                f.write("{}\n".format(height))
                f.write("{}\n".format(name))
                f.write("{}".format(level_water))

    @staticmethod
    def overwriting(height: str, name: str, level_water: int, param: int) -> None:
        if param == 0:
            del_name = '_seeds.txt'
        else:
            del_name = '_trees.txt'
        with open(name + del_name, 'w', encoding="utf-8") as f:
            f.write("{}\n".format(height))
            f.write("{}\n".format(name))
            f.write("{}".format(level_water))


class ReadOverwritingGrowthAndDeath:

    @staticmethod
    def read_overwriting_for_init(name: str, creation: int, param: int, how_many_days_to_grow: int = 0,
                                  how_many_days_until_the_next_stage: int = 0) -> list:
        if creation == 0:
            parameters = []
            if param == 0:
                del_name = '_vegetables.txt'
            else:
                del_name = '_fruits.txt'
            with open(name + del_name, 'r', encoding="utf-8") as f:
                day = int(f.readline())
                how_many_days_to_grow = int(f.readline())
                how_many_days_until_the_next_stage = int(f.readline())
                hp = int(f.readline())
                parameters.append(day)
                parameters.append(how_many_days_to_grow)
                parameters.append(how_many_days_until_the_next_stage)
                parameters.append(hp)
                return parameters
        elif creation == 1:
            if param == 0:
                del_name = '_vegetables.txt'
            else:
                del_name = '_fruits.txt'
            day = 0
            hp = 9
            with open(name + del_name, 'w', encoding="utf-8") as f:
                f.write("{}\n".format(day))
                f.write("{}\n".format(how_many_days_to_grow))
                f.write("{}\n".format(how_many_days_until_the_next_stage))
                f.write("{}".format(hp))

    @staticmethod
    def deletion(name: str, param: int) -> None:
        path = '/PyCharm/ППВиС/Laboratory_work_4/'
        if param == 0:
            del_path1 = '_seeds.txt'
            del_path2 = '_vegetables.txt'
            if os.path.isfile(path + name + del_path1):
                os.remove(path + name + del_path1)
                print("success")
            else:
                print("File doesn't exists!")

            if os.path.isfile(path + name + del_path2):
                os.remove(path + name + del_path2)
                print("success")
            else:
                print("File doesn't exists!")
        elif param == 1:
            del_path1 = '_trees.txt'
            del_path2 = '_fruits.txt'
            if os.path.isfile(path + name + del_path1):
                os.remove(path + name + del_path1)
                print("success")
            else:
                print("File doesn't exists!")

            if os.path.isfile(path + name + del_path2):
                os.remove(path + name + del_path2)
                print("success")
            else:
                print("File doesn't exists!")

    @staticmethod
    def overwriting(path: str, day: int, how_many_days_to_grow: int, how_many_days_until_the_next_stage: int, hp: int,
                    param: int) -> None:
        if param == 0:
            del_name = '_vegetables.txt'
        else:
            del_name = '_fruits.txt'
        with open(path + del_name, 'w', encoding="utf-8") as f:
            f.write("{}\n".format(day))
            f.write("{}\n".format(how_many_days_to_grow))
            f.write("{}\n".format(how_many_days_until_the_next_stage))
            f.write("{}".format(hp))


class ReadOverwritingPoorConditions:

    @staticmethod
    def read_overwriting_for_init(name: str, del_name: str, default: str, creation: int, param: int) -> str:
        if param == 0:
            name_end = '_vegetables.txt'
        else:
            name_end = '_fruits.txt'

        if creation == 0:
            with open(name + del_name + name_end, 'r', encoding="utf-8") as f:
                condition = f.read()
                return condition

        elif creation == 1:
            with open(name + del_name + name_end, 'w', encoding="utf-8") as f:
                f.write(default)

    @staticmethod
    def overwriting(name: str, del_name: str, default: str, param: int) -> None:
        if param == 0:
            name_end = '_vegetables.txt'
        else:
            name_end = '_fruits.txt'

        with open(name + del_name + name_end, 'w', encoding="utf-8") as f:
            f.write(default)

    @staticmethod
    def deletion(name: str, del_name: str, param: int) -> None:
        path = '/PyCharm/ППВиС/Laboratory_work_4/'

        if param == 0:
            name_end = '_vegetables.txt'
        else:
            name_end = '_fruits.txt'

        if os.path.isfile(path + name + del_name + name_end):
            os.remove(path + name + del_name + name_end)
            print("success")
        else:
            print("File doesn't exists!")


class ReadOverwritingGardenBedAndTrees:

    @staticmethod
    def read(way: str) -> list:
        names = []
        with open(way, 'r', encoding="utf-8") as f:
            for line in f:
                word = line
                word = word.replace("\n", "")
                names.append(word)
        return names

    @staticmethod
    def overwriting(way: str, length: int, names: list) -> None:
        with open(way, 'w', encoding="utf-8") as f:
            for i in range(0, length):
                f.write(names[i] + '\n')


class ReadOverwritingWeather:

    @staticmethod
    def read_for_init() -> str:
        with open('Weather.txt', 'r', encoding="utf-8") as f:
            weather = f.read()
        return weather

    @staticmethod
    def overwriting(weather: str) -> None:
        with open('Weather.txt', 'w', encoding="utf-8") as f:
            f.write(weather)
