import json
from dictionary import dictionary


class Globals:
    name_of_object = None


class ReadOverwritingSeeds:

    @staticmethod
    def read_overwriting_for_init(name: str, creation: int, param: int) -> list:
        bool_is_in_garden = True
        if creation == 0:
            parameters = []
            if param == 0:
                del_name = 'vegetables'
            else:
                del_name = 'fruits'

            with open("garden_area.json", 'r') as file:
                data = json.load(file)
                for item in data[del_name]:
                    if name in data[del_name][item]:
                        height = data[del_name][item][name]['height']
                        name = data[del_name][item][name]['name']
                        level_water = data[del_name][item][name]['level_water']
                        parameters.append(height)
                        parameters.append(name)
                        parameters.append(level_water)
                        return parameters
        elif creation == 1:
            with open("garden_area.json", 'r') as file:
                data = json.load(file)

            if param == 0:
                del_name = 'vegetables'
                height = dictionary["seed_stage_1"]
            else:
                del_name = 'fruits'
                height = dictionary["fruit_stage_1"]
            name = name
            level_water = 5

            if name in data[del_name]:

                name_del = name + str(len(data[del_name][name]) + 1)

                while bool_is_in_garden:
                    names = []
                    for item in data[del_name][name]:
                        names.append(item)
                    if name_del in names:
                        name_del = name_del + str(len(data[del_name][name]) + 1)
                    else:
                        bool_is_in_garden = False

                data[del_name][name][name_del] = {
                    "name": name_del,
                    "height": height,
                    "level_water": level_water
                }

                Globals.name_of_object = name_del
            else:

                name_del = name + '1'
                data[del_name][name] = {
                    name_del: {
                        "name": name_del,
                        "height": height,
                        "level_water": level_water
                    }
                }

                Globals.name_of_object = name_del

        with open("garden_area.json", 'w') as file:
            json.dump(data, file, indent=3)

    @staticmethod
    def overwriting(height: str, name: str, level_water: int, param: int) -> None:
        with open("garden_area.json", 'r') as file:
            data = json.load(file)
        if param == 0:
            del_name = 'vegetables'
        else:
            del_name = 'fruits'
        for item in data[del_name]:
            if name in data[del_name][item]:
                data[del_name][item][name]["height"] = height
                data[del_name][item][name]["level_water"] = level_water

        with open("garden_area.json", 'w') as file:
            json.dump(data, file, indent=3)


class ReadOverwritingGrowthAndDeath:

    @staticmethod
    def read_overwriting_for_init(name: str, creation: int, param: int, days_to_grow: int = 0,
                                  days_until_the_next_stage: int = 0) -> list:

        if creation == 0:
            parameters = []
            if param == 0:
                del_name = 'vegetables'
            else:
                del_name = 'fruits'
            with open("garden_area.json", 'r') as file:
                data = json.load(file)
                for item in data[del_name]:
                    if name in data[del_name][item]:
                        day = data[del_name][item][name]["day"]
                        days_to_grow = data[del_name][item][name]["days_to_grow"]
                        days_until_the_next_stage = data[del_name][item][name][
                            "days_until_the_next_stage"]
                        hp = data[del_name][item][name]["hp"]
                        parameters.append(day)
                        parameters.append(days_to_grow)
                        parameters.append(days_until_the_next_stage)
                        parameters.append(hp)
                        return parameters
        elif creation == 1:
            with open("garden_area.json", 'r') as file:
                data = json.load(file)
            if param == 0:
                del_name = 'vegetables'
            else:
                del_name = 'fruits'
            day = 0
            hp = 9

            for item in data[del_name]:
                if Globals.name_of_object in data[del_name][item]:
                    data[del_name][item][Globals.name_of_object]["day"] = day
                    data[del_name][item][Globals.name_of_object]["days_to_grow"] = days_to_grow
                    data[del_name][item][Globals.name_of_object][
                        "days_until_the_next_stage"] = days_until_the_next_stage
                    data[del_name][item][Globals.name_of_object]["hp"] = hp

            with open("garden_area.json", 'w') as file:
                json.dump(data, file, indent=3)

    @staticmethod
    def deletion(name: str, param: int) -> None:

        with open("garden_area.json", 'r') as file:
            data = json.load(file)

        if param == 0:
            del_path = 'vegetables'

            for item in data[del_path]:
                if name in data[del_path][item]:
                    del data[del_path][item][name]

            with open("garden_area.json", 'w') as file:
                json.dump(data, file, indent=3)

        elif param == 1:
            del_path = 'fruits'

            for item in data[del_path]:
                if name in data[del_path][item]:
                    del data[del_path][item][name]

            with open("garden_area.json", 'w') as file:
                json.dump(data, file, indent=3)

    @staticmethod
    def overwriting(path: str, day: int, days_to_grow: int, days_until_the_next_stage: int, hp: int,
                    param: int) -> None:
        with open("garden_area.json", 'r') as file:
            data = json.load(file)
        if param == 0:
            del_name = 'vegetables'
        else:
            del_name = 'fruits'

        for item in data[del_name]:
            if path in data[del_name][item]:
                data[del_name][item][path]["day"] = day
                data[del_name][item][path]["days_to_grow"] = days_to_grow
                data[del_name][item][path][
                    "days_until_the_next_stage"] = days_until_the_next_stage
                data[del_name][item][path]["hp"] = hp

        with open("garden_area.json", 'w') as file:
            json.dump(data, file, indent=3)


class ReadOverwritingPoorConditions:

    @staticmethod
    def read_overwriting_for_init(name: str, del_name: str, default: str, creation: int, param: int) -> str:

        with open("garden_area.json", 'r') as file:
            data = json.load(file)

        if param == 0:
            name_end = 'vegetables'
        else:
            name_end = 'fruits'

        if creation == 0:
            for item in data[name_end]:
                if name in data[name_end][item]:
                    condition = data[name_end][item][name][del_name]
                    return condition

        elif creation == 1:
            for item in data[name_end]:
                if name in data[name_end][item]:
                    data[name_end][item][name][del_name] = default

            with open("garden_area.json", 'w') as file:
                json.dump(data, file, indent=3)

    @staticmethod
    def overwriting(name: str, del_name: str, default: str, param: int) -> None:

        with open("garden_area.json", 'r') as file:
            data = json.load(file)

        if param == 0:
            name_end = 'vegetables'
        else:
            name_end = 'fruits'

        for item in data[name_end]:
            if name in data[name_end][item]:
                data[name_end][item][name][del_name] = default

        with open("garden_area.json", 'w') as file:
            json.dump(data, file, indent=3)


class ReadOverwritingGardenBedAndTrees:

    @staticmethod
    def read(way: str) -> list:
        names = []
        with open("garden_area.json", 'r') as file:
            data = json.load(file)
            for item in data[way]:
                for name in data[way][item]:
                    names.append(name)
        return names


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
