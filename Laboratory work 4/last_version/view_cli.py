class ViewPrint:

    @staticmethod
    def show_info_view(seed_bed_show_information_about_objects, seed_bed_status,
                       orchard_show_information_about_objects, orchard_status):
        seed_bed_show_information_about_objects(param=0)
        seed_bed_status(param=0)
        orchard_show_information_about_objects(param=1)
        orchard_status(param=1)

    @staticmethod
    def show_next_day_view(name, some_string):
        print(name)
        print(some_string)

    @staticmethod
    def show_status_view(string_1, string_2, string_3):
        print(string_1)
        print(string_2)
        print(string_3)
