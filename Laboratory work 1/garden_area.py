from actions import *
from dictionary import dictionary
from garden_bed_and_trees import *
from view_cli import *
from weather import *


class GardenArea:

    @staticmethod
    def make_action(action_name: str, user_input=None) -> None:
        action = action_map.get(action_name)

        if action_name.__eq__("info") or action_name.__eq__("new_day"):
            action()
        else:
            action(user_input)

    @staticmethod
    def collection(user_input) -> None:
        try:
            object_of_the_plot: str = user_input
            position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
            position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

            if position_of_vegetable is None and position_of_fruit is None:
                raise NameError

            if position_of_vegetable is None:
                pass
            elif SeedBed.check_height(position_of_vegetable, param=0) == dictionary["ripe"]:

                ViewPrint.show_status_view(dictionary["line"],
                                           dictionary["collect_seed"], dictionary["line"])

                SeedBed.deleting_information(position_of_vegetable, param=0)
            else:
                ViewPrint.show_status_view(dictionary["line"],
                                           dictionary["no_grow_seed"], dictionary["line"])

            if position_of_fruit is None:
                pass
            elif Orchard.check_height(position_of_fruit, param=1) == dictionary["fruiting"]:

                ViewPrint.show_status_view(dictionary["line"],
                                           dictionary["collect_fruit"], dictionary["line"])

                Orchard.deleting_information(position_of_fruit, param=1)
            else:
                ViewPrint.show_status_view(dictionary["line"],
                                           dictionary["no_grow_fruit"], dictionary["line"])
        except NameError:
            ViewPrint.show_status_view(dictionary["line"],
                                       dictionary["no_name"], dictionary["line"])

    @staticmethod
    def weeding_seedlings(user_input) -> None:
        weeding = Weeding()

        try:
            object_of_the_plot: str = user_input
            position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)

            if position_of_vegetable is None:
                raise NameError

            if SeedBed.check_weeds(position_of_vegetable) == 0:
                ViewPrint.show_status_view(dictionary["line"],
                                           dictionary["weeding_non"], dictionary["line"])
            else:

                ViewPrint.show_status_view(dictionary["line"],
                                           "", dictionary["line"])

                weeding.using_actions()
                SeedBed.regeneration_weeds(position_of_vegetable, param=0)
        except NameError:
            ViewPrint.show_status_view(dictionary["line"],
                                       dictionary["no_seed"], dictionary["line"])

    @staticmethod
    def watering_the_garden_plot(user_input) -> None:
        watering = Watering()

        try:
            object_of_the_plot: str = user_input
            position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
            position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

            if position_of_vegetable is None and position_of_fruit is None:
                raise NameError

            if position_of_vegetable is None:
                pass
            elif SeedBed.check_level_of_water(position_of_vegetable, param=0) == 0:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['water_non_seed'], dictionary['line'])
            else:
                ViewPrint.show_status_view(dictionary['line'],
                                           "", dictionary['line'])

                watering.using_actions()
                SeedBed.regenerate_level_of_water(position_of_vegetable,
                                                  SeedBed.check_level_of_water(position_of_vegetable, param=0), param=0)

            if position_of_fruit is None:
                pass
            elif Orchard.check_level_of_water(position_of_fruit, param=1) == 0:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['water_non_fruit'], dictionary['line'])
            else:
                ViewPrint.show_status_view(dictionary['line'],
                                           "", dictionary['line'])
                watering.using_actions()
                Orchard.regenerate_level_of_water(position_of_fruit,
                                                  Orchard.check_level_of_water(position_of_fruit, param=1), param=1)
        except NameError:
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['no_name'], dictionary['line'])

    @staticmethod
    def cure_something_in_a_garden_plot(user_input) -> None:
        try:
            object_of_the_plot: str = user_input
            position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
            position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

            if position_of_vegetable is None and position_of_fruit is None:
                raise NameError

            if position_of_vegetable is None:
                pass
            elif SeedBed.check_illness(position_of_vegetable, param=0) == 0:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['cure_non_seed'], dictionary['line'])
            else:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['cure_seed'], dictionary['line'])
                SeedBed.regeneration_illness(position_of_vegetable, param=0)

            if position_of_fruit is None:
                pass
            elif Orchard.check_illness(position_of_fruit, param=1) == 0:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['cure_non_fruit'], dictionary['line'])
            else:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['cure_fruit'], dictionary['line'])
                Orchard.regeneration_illness(position_of_fruit, param=1)
        except NameError:
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['no_name'], dictionary['line'])

    @staticmethod
    def get_rid_of_pests(user_input) -> None:
        try:
            object_of_the_plot: str = user_input

            position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
            position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

            if position_of_vegetable is None and position_of_fruit is None:
                raise NameError

            if position_of_vegetable is None:
                pass
            elif SeedBed.check_vermin(position_of_vegetable, param=0) == 0:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['pests_non_seed'], dictionary['line'])
            else:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['pests_seed'], dictionary['line'])
                SeedBed.regeneration_vermin(position_of_vegetable, param=0)

            if position_of_fruit is None:
                pass
            elif Orchard.check_vermin(position_of_fruit, param=1) == 0:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['pests_non_fruit'], dictionary['line'])
            else:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['pests_fruit'], dictionary['line'])
                Orchard.regeneration_vermin(position_of_fruit, param=1)
        except NameError:
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['no_name'], dictionary['line'])

    @staticmethod
    def use_fertilizer(user_input) -> None:
        fertilizer = Fertilizer()
        try:
            object_of_the_plot: str = user_input
            position_of_vegetable = GardenArea.position("vegetables", object_of_the_plot)
            position_of_fruit = GardenArea.position("fruits", object_of_the_plot)

            if position_of_vegetable is None and position_of_fruit is None:
                raise NameError

            if position_of_vegetable is None:
                pass
            elif SeedBed.check_height(position_of_vegetable, param=0) == dictionary['ripe']:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['fertilizer_non_seed'], dictionary['line'])
            else:
                ViewPrint.show_status_view(dictionary['line'],
                                           "", dictionary['line'])
                fertilizer.using_actions()
                SeedBed.change_height(position_of_vegetable, param=0)

            if position_of_fruit is None:
                pass
            elif Orchard.check_height(position_of_fruit, param=1) == dictionary['fruiting']:
                ViewPrint.show_status_view(dictionary['line'],
                                           dictionary['fertilizer_non_fruit'], dictionary['line'])
            else:
                ViewPrint.show_status_view(dictionary['line'],
                                           "", dictionary['line'])
                fertilizer.using_actions()
                Orchard.change_height(position_of_fruit, param=1)
        except NameError:
            ViewPrint.show_status_view(dictionary["line"], dictionary["no_name"], dictionary["line"])

    @staticmethod
    def garden_plot_next_day(show_next_day_view=ViewPrint.show_next_day_view) -> None:
        weather = Weather()
        weather.changing_the_weather()
        garden = SeedBed()
        trees = Orchard()
        garden.change_of_day(param=0)
        SeedBed.changing_the_water_from_the_weather(weather, param=0, show_next_day_view=show_next_day_view)
        trees.change_of_day(param=1)
        Orchard.changing_the_water_from_the_weather(weather, param=1, show_next_day_view=show_next_day_view)

    @staticmethod
    def create_seedlings(user_input) -> None:
        SeedBed()
        Orchard()
        garden = SeedBed()
        name: list[str] = SeedBed.names('vegetables')

        try:
            object_of_the_plot: str = user_input
            for i in range(0, len(name)):
                if object_of_the_plot != name[i]:
                    continue
                else:
                    raise NameError
            garden.new_object(name=object_of_the_plot, param=0)
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['create'], dictionary['line'])
        except NameError:
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['create_non_seed'], dictionary['line'])

    @staticmethod
    def del_seedlings(user_input) -> None:
        SeedBed()
        Orchard()
        value: bool = False
        position_of_vegetable: int = 0
        name: list[str] = SeedBed.names('vegetables')

        try:
            object_of_the_plot: str = user_input
            for i in range(0, len(name)):
                if object_of_the_plot == name[i]:
                    value = True
                    position_of_vegetable = i
                    break

            if value is False:
                raise NameError
            SeedBed.deleting_information(position_of_vegetable, param=0)
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['del'], dictionary['line'])
        except NameError:
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['del_non_seed'], dictionary['line'])

    @staticmethod
    def create_tree(user_input) -> None:
        SeedBed()
        Orchard()
        trees = Orchard()
        name: list[str] = Orchard.names('fruits')

        try:
            object_of_the_plot: str = user_input
            for i in range(0, len(name)):
                if object_of_the_plot != name[i]:
                    continue
                else:
                    raise NameError
            trees.new_object(name=object_of_the_plot, param=1)
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['create'], dictionary['line'])
        except NameError:
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['create_non_fruit'], dictionary['line'])

    @staticmethod
    def del_tree(user_input) -> None:
        SeedBed()
        Orchard()
        value: bool = False
        position_of_fruits: int = 0
        name: list[str] = Orchard.names('fruits')

        try:
            object_of_the_plot: str = user_input
            for i in range(0, len(name)):
                if object_of_the_plot == name[i]:
                    value = True
                    position_of_fruits = i
                    break

            if value is False:
                raise NameError
            Orchard.deleting_information(position_of_fruits, param=1)
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['fruit_del'], dictionary['line'])
        except NameError:
            ViewPrint.show_status_view(dictionary['line'],
                                       dictionary['del_non_fruit'], dictionary['line'])

    @staticmethod
    def info() -> None:
        weather = Weather()

        ViewPrint.show_status_view(dictionary['line'], dictionary['area'],
                                   dictionary['weather'].format(weather.info_weather))

        ViewPrint.show_info_view(SeedBed.show_information_about_objects, SeedBed.status,
                                 Orchard.show_information_about_objects, Orchard.status)

    @staticmethod
    def new_day() -> None:
        GardenArea.garden_plot_next_day()

    @staticmethod
    def position(culture: str, name: str):
        names = []

        if culture == "fruits":
            names: list[str] = Orchard.names('fruits')
        elif culture == "vegetables":
            names: list[str] = SeedBed.names('vegetables')

        if names is None:
            return None
        for changed_position in range(0, len(names)):
            if name == names[changed_position]:
                return changed_position
        return None


action_map = {
    'collect': GardenArea.collection,
    'weed': GardenArea.weeding_seedlings,
    'water': GardenArea.watering_the_garden_plot,
    'cure': GardenArea.cure_something_in_a_garden_plot,
    'pests': GardenArea.get_rid_of_pests,
    'fertilizer': GardenArea.use_fertilizer,
    'seedlings_new': GardenArea.create_seedlings,
    'seedlings_del': GardenArea.del_seedlings,
    'tree_new': GardenArea.create_tree,
    'tree_del': GardenArea.del_tree,
    'info': GardenArea.info,
    'new_day': GardenArea.new_day
}
