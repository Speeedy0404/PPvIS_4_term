import os
import re

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

import adding_an_entry
import deletion
import file_selection
import search
import table
from parser import globals, XmlParser


class Controller:
    # контролер первого окна
    Search = None
    Delete = None

    @staticmethod
    def on_press_show_info(self):
        Controller.Search = self
        Model.add_info_model()

    @staticmethod
    def on_press_next_page():
        Model.next_page_model()

    @staticmethod
    def on_press_previous_page():
        Model.previous_page_model()

    @staticmethod
    def on_press_first_page():
        Model.first_page_model()

    @staticmethod
    def on_press_last_page():
        Model.last_page_model()

    # контролер второго окна

    @staticmethod
    def on_press_add_student(self):
        Controller.Search = self
        Model.add_student_model()

    # контролер третьего окна

    @staticmethod
    def on_press_change_the_nuber_of_entries(self):
        Controller.Search = self
        Model.change_the_nuber_of_entries_model()

    # контролер четвёртого окна

    @staticmethod
    def on_press_by_full_name(self):
        Controller.Search = self
        View.show_by_full_name()

    @staticmethod
    def on_press_search_full_name(instance):
        Model.search_full_name_model()

    @staticmethod
    def on_press_by_group(self):
        Controller.Search = self
        View.show_by_group()

    @staticmethod
    def on_press_search_by_group(instance):
        Model.search_group_model()

    @staticmethod
    def on_press_by_view(self):
        Controller.Search = self
        View.show_by_view()

    @staticmethod
    def on_press_search_due_to_illness(instance):
        Model.search_due_to_illness_model()

    @staticmethod
    def on_press_search_for_other_reasons(instance):
        Model.search_for_other_reasons_model()

    @staticmethod
    def on_press_search_for_no_good_reason(instance):
        Model.search_for_no_good_reason_model()

    @staticmethod
    def on_press_by_view_min_max(self):
        Controller.Search = self
        View.show_by_view_min_max()

    @staticmethod
    def on_press_search_due_to_illness_min(instance):
        Model.search_due_to_illness_min_model()

    @staticmethod
    def on_press_search_due_to_illness_max(instance):
        Model.search_due_to_illness_max_model()

    @staticmethod
    def on_press_search_for_other_reasons_min(instance):
        Model.search_for_other_reasons_min_model()

    @staticmethod
    def on_press_search_for_other_reasons_max(instance):
        Model.search_for_other_reasons_max_model()

    @staticmethod
    def on_press_search_for_no_good_reason_min(instance):
        Model.search_for_no_good_reason_min_model()

    @staticmethod
    def on_press_search_for_no_good_reason_max(instance):
        Model.search_for_no_good_reason_max_model()

    # контролер пятого окна

    @staticmethod
    def on_press_del_full_name(self):
        Controller.Delete = self
        View.show_by_del_full_name()

    @staticmethod
    def on_press_remove_full_name(instance):
        Model.remove_full_name_model()

    @staticmethod
    def on_press_del_group(self):
        Controller.Delete = self
        View.show_by_del_group()

    @staticmethod
    def on_press_remove_group(instance):
        Model.remove_group_model()

    @staticmethod
    def on_press_del_view(self):
        Controller.Delete = self
        View.show_by_del_view()

    @staticmethod
    def on_press_remove_due_to_illness(instance):
        Model.remove_due_to_illness_model()

    @staticmethod
    def on_press_remove_for_other_reasons(instance):
        Model.remove_for_other_reason_model()

    @staticmethod
    def on_press_remove_for_no_good_reason(instance):
        Model.remove_for_no_good_reason_model()

    @staticmethod
    def on_press_del_view_min_max(self):
        Controller.Delete = self
        View.show_by_del_view_min_max()

    @staticmethod
    def on_press_remove_due_to_illness_min(instance):
        Model.remove_due_to_illness_min_model()

    @staticmethod
    def on_press_remove_due_to_illness_max(instance):
        Model.remove_due_to_illness_max_model()

    @staticmethod
    def on_press_remove_for_other_reasons_min(instance):
        Model.remove_for_other_reasons_min_model()

    @staticmethod
    def on_press_remove_for_other_reasons_max(instance):
        Model.remove_for_other_reasons_max_model()

    @staticmethod
    def on_press_remove_for_no_good_reason_min(instance):
        Model.remove_for_no_good_reason_min_model()

    @staticmethod
    def on_press_remove_for_no_good_reason_max(instance):
        Model.remove_for_no_good_reason_max_model()

    # контролер шестого экрана

    @staticmethod
    def on_press_show_file(self):
        Controller.Search = self
        Model.show_file_model()

    @staticmethod
    def on_press_chose_file(self):
        Controller.Search = self
        Model.chose_file_model()


class Model:
    # модель первого окна

    @staticmethod
    def get_name():
        table.Table.i_n += 1
        table.Table.i_s += 1
        table.Table.i_m += 1
        return globals.name[table.Table.i_n] + " " + globals.surname[table.Table.i_s] + " " + globals.middle_name[
            table.Table.i_m]

    @staticmethod
    def get_group():
        table.Table.i_g += 1
        return globals.group[table.Table.i_g]

    @staticmethod
    def get_diseases():
        table.Table.i_d += 1
        return globals.diseases[table.Table.i_d]

    @staticmethod
    def get_other_reasons():
        table.Table.i_o += 1
        return globals.other_reasons[table.Table.i_o]

    @staticmethod
    def get_without_a_valid():
        table.Table.i_w += 1
        return globals.without_a_valid[table.Table.i_w]

    @staticmethod
    def get_total():
        table.Table.i_t += 1
        return globals.total[table.Table.i_t]

    @staticmethod
    def stabilization_of_iterators():
        table.Table.i_n = -1
        table.Table.i_s = -1
        table.Table.i_m = -1
        table.Table.i_g = -1
        table.Table.i_d = -1
        table.Table.i_o = -1
        table.Table.i_w = -1
        table.Table.i_t = -1

    @staticmethod
    def add_info_model():
        View.show_info_table_view()
        Model.stabilization_of_iterators()

    @staticmethod
    def next_page_model():
        if table.Table.this_page == table.Table.all_page:
            table.Table.this_page = table.Table.all_page
            table.Table.stabilization()
        else:
            table.Table.this_page += 1
            table.Table.stabilization()

    @staticmethod
    def previous_page_model():
        if table.Table.this_page == 0:
            table.Table.this_page = 0
            table.Table.stabilization()
        else:
            table.Table.this_page -= 1
            table.Table.stabilization()

    @staticmethod
    def first_page_model():
        table.Table.this_page = 0
        table.Table.stabilization()

    @staticmethod
    def last_page_model():
        table.Table.this_page = table.Table.all_page
        table.Table.stabilization()

    # модель второго окна

    @staticmethod
    def add_student_model():
        try:
            if re.search(r'[^a-zA-Z]', Controller.Search.named.text):
                raise IndexError
            elif re.search(r'[^a-zA-Z]', Controller.Search.surname.text):
                raise IndexError
            elif re.search(r'[^a-zA-Z]', Controller.Search.middlename.text):
                raise IndexError
            for i in range(0, globals.size_all):
                if Controller.Search.named.text == globals.name[i] and Controller.Search.surname.text == \
                        globals.surname[
                            i] and Controller.Search.middlename.text == \
                        globals.middle_name[i]:
                    raise ValueError

            if Controller.Search.group.text.isnumeric():
                pass
            else:
                Controller.Search.group.text = "000000"

            if Controller.Search.diseases.text.isnumeric():
                pass
            else:
                Controller.Search.diseases.text = "0"

            if Controller.Search.otherreasons.text.isnumeric():
                pass
            else:
                Controller.Search.otherreasons.text = "0"

            if Controller.Search.withoutavalid.text.isnumeric():
                pass
            else:
                Controller.Search.withoutavalid.text = "0"

            totald = str(eval(
                Controller.Search.diseases.text + '+' + Controller.Search.otherreasons.text + '+' + Controller.Search.withoutavalid.text))
            XmlParser.add_student(Controller.Search.named.text, Controller.Search.surname.text,
                                  Controller.Search.middlename.text, Controller.Search.group.text,
                                  Controller.Search.diseases.text, Controller.Search.otherreasons.text,
                                  Controller.Search.withoutavalid.text, totald)

            globals.stabilization()
            table.Table.all_page = int((globals.size_all / globals.size))
            table.Table.this_page = 0

        except(IndexError):
            View.show_status_adding_an_entry_view(
                "Ошибка ввода: имя, фамилия и отчество должны состоять из латинского алфавита")
        except(ValueError):
            View.show_status_adding_an_entry_view("Ошибка: такой студент уже присутствует в списке")

    # модель третьего окна

    @staticmethod
    def change_the_nuber_of_entries_model():
        try:
            del_size = int(Controller.Search.sized.text)
            if del_size > 50:
                del_size = 50
            elif del_size < 0:
                del_size = 10
            globals.size = del_size
            table.Table.all_page = int((globals.size_all / globals.size))
            table.Table.this_page = 0
            Controller.Search.status.text = "Изменения применены"
        except(ValueError):
            del_size = 10
            globals.size = del_size
            table.Table.all_page = int((globals.size_all / globals.size))
            table.Table.this_page = 0
            Controller.Search.status.text = "Изменения применены"

    # модель четвёртого окна

    @staticmethod
    def search_full_name_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            search.Search.list_widget[3].text = 'Найдено {}'.format(number)
            if re.search(r'[^a-zA-Z]', search.Search.list_widget[0].text):
                raise IndexError
            elif re.search(r'[^a-zA-Z]', search.Search.list_widget[1].text):
                raise IndexError
            elif re.search(r'[^a-zA-Z]', search.Search.list_widget[2].text):
                raise IndexError
            View.show_search_by_full_name(number)

        except(IndexError):
            search.Search.list_widget[3].text = 'Фио должно содержать только английские буквы'

    @staticmethod
    def search_group_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            search.Search.list_widget[1].text = 'Найдено {}'.format(number)
            if search.Search.list_widget[0].text.isnumeric():
                pass
            else:
                raise IndexError
            View.show_search_by_group(number)

        except(IndexError):
            search.Search.list_widget[1].text = 'Ввод группы должен быть из чисел'

    @staticmethod
    def search_due_to_illness_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            search.Search.list_widget[6].text = 'Найдено {}'.format(number)
            if search.Search.list_widget[0].text.isnumeric():
                pass
            else:
                raise IndexError
            View.show_search_due_to_illness(number)

        except(IndexError):
            search.Search.list_widget[6].text = 'Ввод  должен быть числовой'

    @staticmethod
    def search_for_other_reasons_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            search.Search.list_widget[6].text = 'Найдено {}'.format(number)
            if search.Search.list_widget[2].text.isnumeric():
                pass
            else:
                raise IndexError
            View.show_search_for_other_reasons(number)

        except(IndexError):
            search.Search.list_widget[6].text = 'Ввод  должен быть числовой'

    @staticmethod
    def search_for_no_good_reason_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            search.Search.list_widget[6].text = 'Найдено {}'.format(number)
            if search.Search.list_widget[4].text.isnumeric():
                pass
            else:
                raise IndexError
            View.show_search_for_no_good_reason(number)

        except(IndexError):
            search.Search.list_widget[6].text = 'Ввод  должен быть числовой'

    @staticmethod
    def search_due_to_illness_min_model():
        number = 0
        Controller.Search.remove_widgets_info()
        search.Search.list_widget[6].text = 'Найдено {}'.format(number)

        for i in range(0, globals.size_all):
            globals.diseases[i] = int(globals.diseases[i])

        min_number = min(globals.diseases)

        for i in range(0, globals.size_all):
            globals.diseases[i] = str(globals.diseases[i])

        View.show_search_due_to_illness_min(number, str(min_number))

    @staticmethod
    def search_due_to_illness_max_model():
        number = 0
        Controller.Search.remove_widgets_info()
        search.Search.list_widget[6].text = 'Найдено {}'.format(number)

        for i in range(0, globals.size_all):
            globals.diseases[i] = int(globals.diseases[i])

        max_number = max(globals.diseases)

        for i in range(0, globals.size_all):
            globals.diseases[i] = str(globals.diseases[i])

        View.show_search_due_to_illness_max(number, str(max_number))

    @staticmethod
    def search_for_other_reasons_min_model():
        number = 0
        Controller.Search.remove_widgets_info()
        search.Search.list_widget[6].text = 'Найдено {}'.format(number)

        for i in range(0, globals.size_all):
            globals.other_reasons[i] = int(globals.other_reasons[i])

        min_number = min(globals.other_reasons)

        for i in range(0, globals.size_all):
            globals.other_reasons[i] = str(globals.other_reasons[i])

        View.show_search_for_other_reasons_min(number, str(min_number))

    @staticmethod
    def search_for_other_reasons_max_model():
        number = 0
        Controller.Search.remove_widgets_info()
        search.Search.list_widget[6].text = 'Найдено {}'.format(number)

        for i in range(0, globals.size_all):
            globals.other_reasons[i] = int(globals.other_reasons[i])

        max_number = max(globals.other_reasons)

        for i in range(0, globals.size_all):
            globals.other_reasons[i] = str(globals.other_reasons[i])

        View.show_search_for_other_reasons_max(number, str(max_number))

    @staticmethod
    def search_for_no_good_reason_min_model():
        number = 0
        Controller.Search.remove_widgets_info()
        search.Search.list_widget[6].text = 'Найдено {}'.format(number)

        for i in range(0, globals.size_all):
            globals.without_a_valid[i] = int(globals.without_a_valid[i])

        min_number = min(globals.without_a_valid)

        for i in range(0, globals.size_all):
            globals.without_a_valid[i] = str(globals.without_a_valid[i])

        View.show_search_for_no_good_reason_min(number, str(min_number))

    @staticmethod
    def search_for_no_good_reason_max_model():
        number = 0
        Controller.Search.remove_widgets_info()
        search.Search.list_widget[6].text = 'Найдено {}'.format(number)

        for i in range(0, globals.size_all):
            globals.without_a_valid[i] = int(globals.without_a_valid[i])

        max_number = max(globals.without_a_valid)

        for i in range(0, globals.size_all):
            globals.without_a_valid[i] = str(globals.without_a_valid[i])

        View.show_search_for_no_good_reason_max(number, str(max_number))

    # модель пятого окна

    @staticmethod
    def remove_full_name_model():
        number = 0
        delta = 0
        if len(globals.name) == 0:
            View.remove_full_name('В списке нет записей')
        else:
            try:
                View.remove_full_name('Удаленно {}'.format(number))
                if re.search(r'[^a-zA-Z]', deletion.Deletion.list_widget[0].text):
                    raise IndexError
                elif re.search(r'[^a-zA-Z]', deletion.Deletion.list_widget[1].text):
                    raise IndexError
                elif re.search(r'[^a-zA-Z]', deletion.Deletion.list_widget[2].text):
                    raise IndexError
                for i in range(0, globals.size_all):
                    i = i + delta
                    if deletion.Deletion.list_widget[0].text == globals.name[i] and deletion.Deletion.list_widget[
                        1].text == \
                            globals.surname[i] and \
                            deletion.Deletion.list_widget[2].text == \
                            globals.middle_name[i]:
                        number += 1
                        View.remove_full_name('Удаленно {}'.format(number))
                        XmlParser.remove_student(i)
                        globals.stabilization()
                        table.Table.all_page = int((globals.size_all / globals.size))
                        table.Table.this_page = 0
                        delta -= 1

            except(IndexError):
                View.remove_full_name('Фио должно содержать только английские буквы')

    @staticmethod
    def remove_group_model():
        number = 0
        delta = 0
        if len(globals.name) == 0:
            View.remove_group('В списке нет записей')
        else:
            try:
                View.remove_group('Удаленно {}'.format(number))
                if deletion.Deletion.list_widget[0].text.isnumeric():
                    for i in range(0, globals.size_all):
                        i = i + delta
                        if deletion.Deletion.list_widget[0].text == globals.group[i]:
                            number += 1
                            View.remove_group('Удаленно {}'.format(number))
                            XmlParser.remove_student(i)
                            globals.stabilization()
                            table.Table.all_page = int((globals.size_all / globals.size))
                            table.Table.this_page = 0
                            delta -= 1
                else:
                    raise IndexError

            except(IndexError):
                View.remove_group('Ввод должен быть числовой')

    @staticmethod
    def remove_due_to_illness_model():
        number = 0
        delta = 0
        if len(globals.name) == 0:
            View.remove_due_to_illness('В списке нет записей')
        else:
            try:
                View.remove_due_to_illness('Удаленно {}'.format(number))
                if deletion.Deletion.list_widget[0].text.isnumeric():
                    for i in range(0, globals.size_all):
                        i = i + delta
                        if deletion.Deletion.list_widget[0].text == globals.diseases[i]:
                            number += 1
                            View.remove_due_to_illness('Удаленно {}'.format(number))
                            XmlParser.remove_student(i)
                            globals.stabilization()
                            table.Table.all_page = int((globals.size_all / globals.size))
                            table.Table.this_page = 0

                            delta -= 1
                else:
                    raise IndexError

            except(IndexError):
                View.remove_due_to_illness('Ввод должен быть числовой')

    @staticmethod
    def remove_for_other_reason_model():
        number = 0
        delta = 0
        if len(globals.name) == 0:
            View.remove_for_other_reason_mode('В списке нет записей')
        else:
            try:
                View.remove_for_other_reason_mode('Удаленно {}'.format(number))
                if deletion.Deletion.list_widget[2].text.isnumeric():
                    for i in range(0, globals.size_all):
                        i = i + delta
                        if deletion.Deletion.list_widget[2].text == globals.other_reasons[i]:
                            number += 1
                            View.remove_for_other_reason_mode('Удаленно {}'.format(number))
                            search.Search.i_i += 1
                            XmlParser.remove_student(i)
                            globals.stabilization()
                            table.Table.all_page = int((globals.size_all / globals.size))
                            table.Table.this_page = 0
                            delta -= 1
                else:
                    raise IndexError

            except(IndexError):
                View.remove_for_other_reason_mode('Ввод должен быть числовой')

    @staticmethod
    def remove_for_no_good_reason_model():
        number = 0
        delta = 0
        if len(globals.name) == 0:
            View.remove_for_no_good_reason_model('В списке нет записей')
        else:
            try:
                View.remove_for_no_good_reason_model('Удаленно {}'.format(number))
                if deletion.Deletion.list_widget[4].text.isnumeric():
                    pass
                else:
                    raise IndexError
                for i in range(0, globals.size_all):
                    i = i + delta
                    if deletion.Deletion.list_widget[4].text == globals.without_a_valid[i]:
                        number += 1
                        View.remove_for_no_good_reason_model('Удаленно {}'.format(number))
                        XmlParser.remove_student(i)
                        globals.stabilization()
                        table.Table.all_page = int((globals.size_all / globals.size))
                        table.Table.this_page = 0
                        delta -= 1
            except(IndexError):
                View.remove_for_no_good_reason_model('Ввод  должен быть числовой')

    @staticmethod
    def remove_due_to_illness_min_model():
        if len(globals.name) == 0:
            deletion.Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.diseases[i] = int(globals.diseases[i])

            min_number = min(globals.diseases)
            try:
                for i in range(0, globals.size_all):
                    i = i + delta
                    if int(globals.diseases[i]) == min_number:
                        number += 1
                        deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                        XmlParser.remove_student(i)
                        globals.stabilization()
                        table.Table.all_page = int((globals.size_all / globals.size))
                        table.Table.this_page = 0
                        delta -= 1
            except IndexError:
                pass

            for i in range(0, globals.size_all):
                globals.diseases[i] = str(globals.diseases[i])

    @staticmethod
    def remove_due_to_illness_max_model():
        if len(globals.name) == 0:
            deletion.Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.diseases[i] = int(globals.diseases[i])

            max_number = max(globals.diseases)

            for i in range(0, globals.size_all):
                i = i + delta
                if int(globals.diseases[i]) == max_number:
                    number += 1
                    deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    table.Table.all_page = int((globals.size_all / globals.size))
                    table.Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.diseases[i] = str(globals.diseases[i])

    @staticmethod
    def remove_for_other_reasons_min_model():
        if len(globals.name) == 0:
            deletion.Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.other_reasons[i] = int(globals.other_reasons[i])

            min_number = min(globals.other_reasons)

            for i in range(0, globals.size_all):
                i = i + delta
                if int(globals.other_reasons[i]) == min_number:
                    number += 1
                    deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    table.Table.all_page = int((globals.size_all / globals.size))
                    table.Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.other_reasons[i] = str(globals.other_reasons[i])

    @staticmethod
    def remove_for_other_reasons_max_model():
        if len(globals.name) == 0:
            deletion.Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.other_reasons[i] = int(globals.other_reasons[i])

            max_number = max(globals.other_reasons)

            for i in range(0, globals.size_all):
                i = i + delta
                if int(globals.other_reasons[i]) == max_number:
                    number += 1
                    deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    table.Table.all_page = int((globals.size_all / globals.size))
                    table.Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.other_reasons[i] = str(globals.other_reasons[i])

    @staticmethod
    def remove_for_no_good_reason_min_model():
        if len(globals.name) == 0:
            deletion.Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.without_a_valid[i] = int(globals.without_a_valid[i])

            min_number = min(globals.without_a_valid)

            for i in range(0, globals.size_all):
                i = i + delta
                if int(globals.without_a_valid[i]) == min_number:
                    number += 1
                    deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    table.Table.all_page = int((globals.size_all / globals.size))
                    table.Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.without_a_valid[i] = str(globals.without_a_valid[i])

    @staticmethod
    def remove_for_no_good_reason_max_model():
        if len(globals.name) == 0:
            deletion.Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.without_a_valid[i] = int(globals.without_a_valid[i])

            max_number = max(globals.without_a_valid)

            for i in range(0, globals.size_all):
                i = i + delta
                if int(globals.without_a_valid[i]) == max_number:
                    number += 1
                    deletion.Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    table.Table.all_page = int((globals.size_all / globals.size))
                    table.Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.without_a_valid[i] = str(globals.without_a_valid[i])

    # модель шестого экрана

    @staticmethod
    def show_file_model():
        delta = 0
        files = os.listdir(globals.directory)
        number = len(files)
        for i in range(0, number):
            i = i + delta
            if files[i].endswith(".xml"):
                pass
            else:
                del files[i]
                delta -= 1
        number = len(files)
        file_selection.FileSelection.list_file = files
        View.show_file(number, files)

    @staticmethod
    def chose_file_model():
        global root
        delta = 0
        files = os.listdir(globals.directory)
        number = len(files)
        for i in range(0, number):
            i = i + delta
            if files[i].endswith(".xml"):
                pass
            else:
                del files[i]
                delta -= 1
        file_selection.FileSelection.list_file = files
        number = len(file_selection.FileSelection.list_file)
        for i in range(0, number):
            if Controller.Search.named.text == file_selection.FileSelection.list_file[i]:
                View.show_chose_file('Выбор файла произошёл успешно')
                root = XmlParser.change_file(Controller.Search.named.text)
                globals.stabilization()
                table.Table.all_page = int((globals.size_all / globals.size))
                table.Table.this_page = 0
                break

            else:
                View.show_chose_file('Такого файла нет в дериктории')


class View:
    # представление первого окна

    @staticmethod
    def show_info_table_view():
        i_info = -1
        table.Table.stabilization()
        for i in range(0, globals.size):
            try:
                i_info += 1
                table.Table.list.append(Label(text=Model.get_name()))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            except(IndexError):
                table.Table.list.append((Label(text="")))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            try:
                i_info += 1
                table.Table.list.append(Label(text=Model.get_group()))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            except(IndexError):
                table.Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            try:
                i_info += 1
                table.Table.list.append(Label(text=Model.get_diseases()))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            except(IndexError):
                table.Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            try:
                i_info += 1
                table.Table.list.append(Label(text=Model.get_other_reasons()))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            except(IndexError):
                table.Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            try:
                i_info += 1
                table.Table.list.append(Label(text=Model.get_without_a_valid()))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            except(IndexError):
                table.Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            try:
                i_info += 1
                table.Table.list.append(Label(text=Model.get_total()))
                Controller.Search.info.add_widget(table.Table.list[i_info])
            except(IndexError):
                table.Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(table.Table.list[i_info])
        i_info += 1
        table.Table.list.append(Label(text="Текущая страница:{}".format(table.Table.this_page), font_size=11))
        Controller.Search.info.add_widget(table.Table.list[i_info])
        i_info += 1
        table.Table.list.append(Label(text="Всего страниц:{}".format(table.Table.all_page), font_size=11))
        Controller.Search.info.add_widget(table.Table.list[i_info])
        i_info += 1
        table.Table.list.append(Widget())
        Controller.Search.info.add_widget(table.Table.list[i_info])
        i_info += 1
        table.Table.list.append(Widget())
        Controller.Search.info.add_widget(table.Table.list[i_info])
        i_info += 1
        if globals.size > globals.size_all:
            table.Table.list.append(Label(text="Записей на странице:{}".format(globals.size_all), font_size=11))
        else:
            table.Table.list.append(Label(text="Записей на странице:{}".format(globals.size), font_size=11))
        Controller.Search.info.add_widget(table.Table.list[i_info])
        i_info += 1
        table.Table.list.append(Label(text="Всего записей:{}".format(globals.size_all), font_size=11))
        Controller.Search.info.add_widget(table.Table.list[i_info])

    # представление  второго окна

    @staticmethod
    def show_status_adding_an_entry_view(text):
        adding_an_entry.AddingAnEntry.text = text

    # представление  четвертого окна

    @staticmethod
    def show_by_full_name():
        search.Search.i_w += 1
        search.Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Имя'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])
        search.Search.i_w += 1
        search.Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Фамилия'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])
        search.Search.i_w += 1
        search.Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Отчество'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])
        search.Search.i_w += 1
        search.Search.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])
        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_full_name))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

    @staticmethod
    def show_search_by_full_name(number):
        for i in range(0, globals.size_all):
            if search.Search.list_widget[0].text == globals.name[i] and search.Search.list_widget[1].text == \
                    globals.surname[i] and \
                    search.Search.list_widget[2].text == \
                    globals.middle_name[i]:
                number += 1
                search.Search.list_widget[3].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_by_group():
        search.Search.i_w += 1
        search.Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Группа'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])
        search.Search.i_w += 1
        search.Search.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])
        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_by_group))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

    @staticmethod
    def show_search_by_group(number):
        for i in range(0, globals.size_all):
            if search.Search.list_widget[0].text == globals.group[i]:
                number += 1
                search.Search.list_widget[1].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_by_view():
        search.Search.i_w += 1
        search.Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='По болезни'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])
        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_due_to_illness))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='По другим пичинам'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_other_reasons))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Без уважительной причины'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_no_good_reason))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

    @staticmethod
    def show_search_due_to_illness(number):
        for i in range(0, globals.size_all):
            if search.Search.list_widget[0].text == globals.diseases[i]:
                number += 1
                search.Search.list_widget[6].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_search_for_other_reasons(number):
        for i in range(0, globals.size_all):
            if search.Search.list_widget[2].text == globals.other_reasons[i]:
                number += 1
                search.Search.list_widget[6].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_search_for_no_good_reason(number):
        for i in range(0, globals.size_all):
            if search.Search.list_widget[4].text == globals.without_a_valid[i]:
                number += 1
                search.Search.list_widget[6].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_by_view_min_max():
        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск пропуски по болезни(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_due_to_illness_min))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])
        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск пропуски по болезни(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_due_to_illness_max))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск пропуски по другим причинам(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_other_reasons_min))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск пропуски по другим причинам(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_other_reasons_max))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск пропуски без уважительной причины(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_no_good_reason_min))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            Button(text='Поиск пропуски без уважительной причины(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_no_good_reason_max))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

        search.Search.i_w += 1
        search.Search.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Search.search.add_widget(search.Search.list_widget[search.Search.i_w])

    @staticmethod
    def show_search_due_to_illness_min(number, min_number):
        for i in range(0, globals.size_all):
            if globals.diseases[i] == min_number:
                number += 1
                search.Search.list_widget[6].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_search_due_to_illness_max(number, max_number):
        for i in range(0, globals.size_all):
            if globals.diseases[i] == max_number:
                number += 1
                search.Search.list_widget[6].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_search_for_other_reasons_min(number, min_number):
        for i in range(0, globals.size_all):
            if globals.other_reasons[i] == min_number:
                number += 1
                search.Search.list_widget[6].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_search_for_other_reasons_max(number, max_number):
        for i in range(0, globals.size_all):
            if globals.other_reasons[i] == max_number:
                number += 1
                search.Search.list_widget[6].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_search_for_no_good_reason_min(number, min_number):
        for i in range(0, globals.size_all):
            if globals.without_a_valid[i] == min_number:
                number += 1
                search.Search.list_widget[6].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    @staticmethod
    def show_search_for_no_good_reason_max(number, max_number):
        for i in range(0, globals.size_all):
            if globals.without_a_valid[i] == max_number:
                number += 1
                search.Search.list_widget[6].text = 'Найдено {}'.format(number)
                search.Search.i_i += 1
                search.Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

                search.Search.i_i += 1
                search.Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(search.Search.list_info[search.Search.i_i])

    # представление  пятого окна

    @staticmethod
    def show_by_del_full_name():
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Имя'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Фамилия'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Отчество'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_full_name))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

    @staticmethod
    def remove_full_name(text):
        deletion.Deletion.list_widget[3].text = text

    @staticmethod
    def show_by_del_group():
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Группа'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_group))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

    @staticmethod
    def remove_group(text):
        deletion.Deletion.list_widget[1].text = text

    @staticmethod
    def show_by_del_view():
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='По болезни'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_due_to_illness))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='По другим пичинам'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_other_reasons))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Без уважительной причины'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_no_good_reason))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

    @staticmethod
    def remove_due_to_illness(text):
        deletion.Deletion.list_widget[6].text = text

    @staticmethod
    def remove_for_other_reason_mode(text):
        deletion.Deletion.list_widget[6].text = text

    @staticmethod
    def remove_for_no_good_reason_model(text):
        deletion.Deletion.list_widget[6].text = text

    @staticmethod
    def show_by_del_view_min_max():
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление пропуски по болезни(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_due_to_illness_min))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])
        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление пропуски по болезни(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_due_to_illness_max))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление пропуски по другим причинам(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_other_reasons_min))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление пропуски по другим причинам(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_other_reasons_max))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление пропуски без уважительной причины(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_no_good_reason_min))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Button(text='Удаление пропуски без уважительной причины(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_no_good_reason_max))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

        deletion.Deletion.i_w += 1
        deletion.Deletion.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Delete.del_info.add_widget(deletion.Deletion.list_widget[deletion.Deletion.i_w])

    # представление шестого экрана

    @staticmethod
    def show_file(number, files):
        for i in range(0, number):
            file_selection.FileSelection.i_t += 1
            file_selection.FileSelection.list.append(Label(text=files[i], halign='left', valign='middle'))
            Controller.Search.file.add_widget(file_selection.FileSelection.list[file_selection.FileSelection.i_t])

    @staticmethod
    def show_chose_file(text):
        Controller.Search.status.text = text
