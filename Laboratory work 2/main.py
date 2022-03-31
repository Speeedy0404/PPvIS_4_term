import re
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from parser import *

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 800)

from kivy.uix.textinput import TextInput

Builder.load_string('''
<ItemTextInput@TextInput>:
    multiline: False
    background_color: 'white'
    halign: 'left'
    cursor_blink: True
    cursor_color: 'black'
    foreground_color: 'black'
    font_size: '14'
<ItemButton@Button>:
    font_size: 12
    color: 'black'
    background_color: .32, .85, .94, 1
    background_normal: ''
<ItemLabel@Label>:
    color: 'white'
    halign:'center'
    valign:'middle'
    text_size:self.size

<Table>:
    info: info
    button:button
    FloatLayout:
        ItemLabel:
            text: 'Число  пропусков  занятий  за  год(количество пропущенных пар)'
            size_hint: .5, .1
            pos: 1300/2-220, 720

        GridLayout:
            id: info
            rows: 53
            cols: 6
            spacing: 3
            size_hint: 1, .85
            pos: 0, 80
            ItemButton:
                id:button
                text:'Показать информацию'
                on_press:
                    root.del_info()
                    root.add_info()
            ItemButton:
                text:'Выбор файла'
                on_press:
                    root.del_info()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_six' 
            Widget:
            Widget:
            Widget:
            Widget:
            ItemLabel:
                text: 'Фио студента'
            ItemLabel:
                text: 'Группа'
            ItemLabel:
                text: 'По болезни'
            ItemLabel:
                text: 'По другим причинам'
            ItemLabel:
                text: 'Без уважительной причины'
            ItemLabel:
                text: 'Итого'





        BoxLayout:
            orientation:'horizontal' 
            size_hint: 1, .05
            pos: 0, 0
            spacing:5
            ItemButton:
                text:'Предыдущая страница'
                on_press:
                    root.del_info()
                    root.previous_page()
                    root.add_info()
            ItemButton:
                text:'Следущая страница'
                on_press:
                    root.del_info()
                    root.next_page()
                    root.add_info()
            ItemButton:
                text:'Первая страница'
                on_press:
                    root.del_info()
                    root.first_page()
                    root.add_info()
            ItemButton:
                text:'Последняя страница'
                on_press:
                    root.del_info()
                    root.last_page()
                    root.add_info()
            ItemButton:
                text:'Изменить число записей'
                on_press:
                    root.del_info()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_three'
            ItemButton:
                text:'Поиск'
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_four' 
            ItemButton:
                text:'Удаление'
                on_press:
                    root.del_info()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_five' 
            ItemButton:
                text:'Добавить студента'
                on_press:
                    root.del_info()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_two'                   



<AddingAnEntry>:
    status:status
    named:named
    surname:surname
    middlename:middlename
    group:group
    diseases:diseases
    otherreasons:otherreasons
    withoutavalid:withoutavalid

    AnchorLayout:
        BoxLayout:
            orientation: 'vertical'
            size_hint: .5, .5 
            ItemTextInput:
                id:named
                hint_text:'Имя'
            ItemTextInput:
                id:surname
                hint_text:'Фамилия'
            ItemTextInput:
                id:middlename
                hint_text:'Отчество'
            ItemTextInput:
                id:group
                hint_text:'Группа'
                input_type:'number'
                input_filter:'int'
            ItemTextInput:
                id:diseases
                hint_text:'Пропуски по болезни'
                input_type:'number'
                input_filter:'int'
            ItemTextInput:
                id:otherreasons
                hint_text:'Пропуски по другим причинам'
                input_type:'number'
                input_filter:'int'
            ItemTextInput:
                id:withoutavalid
                hint_text:'Пропуски без причины'
                input_type:'number'
                input_filter:'int'
            ItemButton:
                text: 'Добавить студента'
                on_press:
                    root.add_student()
                    root.change_status()   
            Label:
                id:status
                text:'Статус'
                halign:'left'
                valign:'middle'
                text_size:self.size
            ItemButton:
                text: 'Выход'
                on_press:
                    root.status.text='Статус'
                    root.named.text=''
                    root.surname.text=''
                    root.middlename.text=''
                    root.group.text=''
                    root.diseases.text=''
                    root.otherreasons.text=''
                    root.withoutavalid.text=''
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_one'

<NumberOfEntries>:
    sized:sized
    status:status
    AnchorLayout:

        BoxLayout:
            orientation: 'vertical'
            size_hint: .25, .25 
            ItemTextInput:
                id:sized
                hint_text:'Число записей на странице(0-50)'
                input_type:'number'
                input_filter:'int'
            ItemButton:
                text:'Применить изменения'
                on_press:
                    root.change_the_nuber_of_entries()
            Label:
                id:status
                text:'Статус'
                halign:'left'
                valign:'middle'
                text_size:self.size
            ItemButton:
                text: 'Выход'
                on_press:
                    root.status.text='Статус'
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_one'



<Search>:
    search:search
    info:info
    FloatLayout:

        GridLayout:
            id: info
            rows: 37
            cols: 6
            spacing: 3
            size_hint: 1, .7
            pos: 0,245 
            ItemLabel:
                text: 'Фио студента'
            ItemLabel:
                text: 'Группа'
            ItemLabel:
                text: 'По болезни'
            ItemLabel:
                text: 'По другим причинам'
            ItemLabel:
                text: 'Без уважительной причины'
            ItemLabel:
                text: 'Итого'

        BoxLayout:
            id:search
            spacing:2
            orientation: 'vertical'
            size_hint: .5, .25
            pos:325,45


        BoxLayout:
            orientation:'horizontal' 
            size_hint: 1, .05
            pos: 0, 0
            spacing:5
            ItemButton:
                text:'По ФИО'
                on_press:
                    root.remove_widgets()
                    root.remove_widgets_info()
                    root.add_widget_full_name()
            ItemButton:
                text:'По номеру группы'
                on_press:
                    root.remove_widgets()
                    root.remove_widgets_info()
                    root.add_widget_group()
            ItemButton:
                text:'По виду пропуска'
                on_press:
                    root.remove_widgets()
                    root.remove_widgets_info()
                    root.add_widget_view()
            ItemButton:
                text:'По виду пропуска(макс., мин.)'
                on_press:
                    root.remove_widgets()
                    root.remove_widgets_info()
                    root.add_widget_view_min_max()
            ItemButton:
                text: 'Выход'
                on_press:
                    root.remove_widgets()
                    root.remove_widgets_info()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_one'



<Deletion>:
    del_info:del_info
    FloatLayout:

        BoxLayout:
            id:del_info
            orientation: 'vertical'
            size_hint: .5, .5 
            spacing:5
            pos:325,200

        BoxLayout:
            orientation:'horizontal' 
            size_hint: 1, .05
            pos: 0, 0
            spacing:5
            ItemButton:
                text:'По ФИО'
                on_press:
                    root.remove_widgets()
                    root.add_widget_full_name()
            ItemButton:
                text:'По номеру группы'
                on_press:
                    root.remove_widgets()
                    root.add_widget_group()
            ItemButton:
                text:'По виду пропуска'
                on_press:
                    root.remove_widgets()
                    root.add_widget_view()
            ItemButton:
                text:'По виду пропуска(макс., мин.)'
                on_press:
                    root.remove_widgets()
                    root.add_widget_view_min_max()
            ItemButton:
                text: 'Выход'
                on_press:
                    root.remove_widgets()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_one'

<FileSelection>:
    file:file
    status:status
    named:named
    AnchorLayout:
        BoxLayout:
            id:file
            orientation: 'vertical'
            size_hint: .5, .5 
            spacing:5
            ItemTextInput:
                id:named
                hint_text:'Введите нужный файл'
            Label:
                id:status
                text:'Статус'
                halign:'left'
                valign:'middle'
                text_size:self.size
            ItemButton:
                text: 'Показать доступные файлы' 
                on_press:
                    root.remove_widgets()
                    root.show_file()
            ItemButton:
                text: 'Выбрать'   
                on_press:
                    root.choice()
            ItemButton:
                text: 'Выход'
                on_press:
                    root.named.text=''
                    root.remove_widgets()
                    root.status.text='Статус'
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 0.5
                    root.manager.current = 'screen_one'

''')


# Создайте класс для всех экранов, в которые вы можете включить
# полезные методы, специфичные для этого экрана

class Table(Screen):
    i_n = -1
    i_s = -1
    i_m = -1
    i_g = -1
    i_d = -1
    i_o = -1
    i_w = -1
    i_t = -1
    list = []
    all_page = int((globals.size_all / globals.size))
    this_page = 0

    def add_info(self):
        Controller.on_press_show_info(self)

    def del_info(self):
        try:
            for i in range(0, (globals.size * 6) + 6):
                self.info.remove_widget(Table.list[i])
            Table.list.clear()
        except(IndexError):
            pass

    @staticmethod
    def stabilization():
        Table.i_n = (Table.this_page * globals.size) - 1
        Table.i_s = (Table.this_page * globals.size) - 1
        Table.i_m = (Table.this_page * globals.size) - 1
        Table.i_g = (Table.this_page * globals.size) - 1
        Table.i_d = (Table.this_page * globals.size) - 1
        Table.i_o = (Table.this_page * globals.size) - 1
        Table.i_w = (Table.this_page * globals.size) - 1
        Table.i_t = (Table.this_page * globals.size) - 1

    def next_page(self):
        Controller.on_press_next_page()

    def previous_page(self):
        Controller.on_press_previous_page()

    def first_page(self):
        Controller.on_press_first_page()

    def last_page(self):
        Controller.on_press_last_page()


class AddingAnEntry(Screen):
    text = "Добавление произошло успешно"

    def change_status(self):
        self.status.text = AddingAnEntry.text
        AddingAnEntry.text = "Добавление произошло успешно"

    def add_student(self):
        Controller.on_press_add_student(self)


class NumberOfEntries(Screen):

    def change_the_nuber_of_entries(self):
        Controller.on_press_change_the_nuber_of_entries(self)


class Search(Screen):
    list_info = []
    i_i = -1
    list_widget = []
    i_w = -1

    def remove_widgets(self):
        try:
            for i in range(0, Search.i_w + 1):
                self.search.remove_widget(Search.list_widget[i])
            Search.list_widget.clear()
            Search.i_w = -1
        except(IndexError):
            pass

    def remove_widgets_info(self):
        try:
            for i in range(0, Search.i_i + 1):
                self.info.remove_widget(Search.list_info[i])
            Search.list_info.clear()
            Search.i_i = -1
        except(IndexError):
            pass

    def add_widget_full_name(self):
        Controller.on_press_by_full_name(self)

    def add_widget_group(self):
        Controller.on_press_by_group(self)

    def add_widget_view(self):
        Controller.on_press_by_view(self)

    def add_widget_view_min_max(self):
        Controller.on_press_by_view_min_max(self)


class Deletion(Screen):
    list_widget = []
    i_w = -1

    def remove_widgets(self):
        try:
            for i in range(0, Deletion.i_w + 1):
                self.del_info.remove_widget(Deletion.list_widget[i])
            Deletion.list_widget.clear()
            Deletion.i_w = -1
        except(IndexError):
            pass

    def add_widget_full_name(self):
        Controller.on_press_del_full_name(self)

    def add_widget_group(self):
        Controller.on_press_del_group(self)

    def add_widget_view(self):
        Controller.on_press_del_view(self)

    def add_widget_view_min_max(self):
        Controller.on_press_del_view_min_max(self)


class FileSelection(Screen):
    list = []
    i_t = -1
    list_file = []

    def remove_widgets(self):
        try:
            for i in range(0, FileSelection.i_t + 1):
                self.file.remove_widget(FileSelection.list[i])
            FileSelection.list.clear()
            FileSelection.i_t = -1
        except(IndexError):
            pass

    def choice(self):
        Controller.on_press_chose_file(self)

    def show_file(self):
        Controller.on_press_show_file(self)


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
        Table.i_n += 1
        Table.i_s += 1
        Table.i_m += 1
        return globals.name[Table.i_n] + " " + globals.surname[Table.i_s] + " " + globals.middle_name[
            Table.i_m]

    @staticmethod
    def get_group():
        Table.i_g += 1
        return globals.group[Table.i_g]

    @staticmethod
    def get_diseases():
        Table.i_d += 1
        return globals.diseases[Table.i_d]

    @staticmethod
    def get_other_reasons():
        Table.i_o += 1
        return globals.other_reasons[Table.i_o]

    @staticmethod
    def get_without_a_valid():
        Table.i_w += 1
        return globals.without_a_valid[Table.i_w]

    @staticmethod
    def get_total():
        Table.i_t += 1
        return globals.total[Table.i_t]

    @staticmethod
    def stabilization_of_iterators():
        Table.i_n = -1
        Table.i_s = -1
        Table.i_m = -1
        Table.i_g = -1
        Table.i_d = -1
        Table.i_o = -1
        Table.i_w = -1
        Table.i_t = -1

    @staticmethod
    def add_info_model():
        View.show_info_table_view()
        Model.stabilization_of_iterators()

    @staticmethod
    def next_page_model():
        if Table.this_page == Table.all_page:
            Table.this_page = Table.all_page
            Table.stabilization()
        else:
            Table.this_page += 1
            Table.stabilization()

    @staticmethod
    def previous_page_model():
        if Table.this_page == 0:
            Table.this_page = 0
            Table.stabilization()
        else:
            Table.this_page -= 1
            Table.stabilization()

    @staticmethod
    def first_page_model():
        Table.this_page = 0
        Table.stabilization()

    @staticmethod
    def last_page_model():
        Table.this_page = Table.all_page
        Table.stabilization()

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
            Table.all_page = int((globals.size_all / globals.size))
            Table.this_page = 0

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
            Table.all_page = int((globals.size_all / globals.size))
            Table.this_page = 0
            Controller.Search.status.text = "Изменения применены"
        except(ValueError):
            del_size = 10
            globals.size = del_size
            Table.all_page = int((globals.size_all / globals.size))
            Table.this_page = 0
            Controller.Search.status.text = "Изменения применены"

    # модель четвёртого окна

    @staticmethod
    def search_full_name_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            Search.list_widget[3].text = 'Найдено {}'.format(number)
            if re.search(r'[^a-zA-Z]', Search.list_widget[0].text):
                raise IndexError
            elif re.search(r'[^a-zA-Z]', Search.list_widget[1].text):
                raise IndexError
            elif re.search(r'[^a-zA-Z]', Search.list_widget[2].text):
                raise IndexError
            View.show_search_by_full_name(number)

        except(IndexError):
            Search.list_widget[3].text = 'Фио должно содержать только английские буквы'

    @staticmethod
    def search_group_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            Search.list_widget[1].text = 'Найдено {}'.format(number)
            if Search.list_widget[0].text.isnumeric():
                pass
            else:
                raise IndexError
            View.show_search_by_group(number)

        except(IndexError):
            Search.list_widget[1].text = 'Ввод группы должен быть из чисел'

    @staticmethod
    def search_due_to_illness_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            Search.list_widget[6].text = 'Найдено {}'.format(number)
            if Search.list_widget[0].text.isnumeric():
                pass
            else:
                raise IndexError
            View.show_search_due_to_illness(number)

        except(IndexError):
            Search.list_widget[6].text = 'Ввод  должен быть числовой'

    @staticmethod
    def search_for_other_reasons_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            Search.list_widget[6].text = 'Найдено {}'.format(number)
            if Search.list_widget[2].text.isnumeric():
                pass
            else:
                raise IndexError
            View.show_search_for_other_reasons(number)

        except(IndexError):
            Search.list_widget[6].text = 'Ввод  должен быть числовой'

    @staticmethod
    def search_for_no_good_reason_model():
        number = 0
        Controller.Search.remove_widgets_info()
        try:
            Search.list_widget[6].text = 'Найдено {}'.format(number)
            if Search.list_widget[4].text.isnumeric():
                pass
            else:
                raise IndexError
            View.show_search_for_no_good_reason(number)

        except(IndexError):
            Search.list_widget[6].text = 'Ввод  должен быть числовой'

    @staticmethod
    def search_due_to_illness_min_model():
        number = 0
        Controller.Search.remove_widgets_info()
        Search.list_widget[6].text = 'Найдено {}'.format(number)

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
        Search.list_widget[6].text = 'Найдено {}'.format(number)

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
        Search.list_widget[6].text = 'Найдено {}'.format(number)

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
        Search.list_widget[6].text = 'Найдено {}'.format(number)

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
        Search.list_widget[6].text = 'Найдено {}'.format(number)

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
        Search.list_widget[6].text = 'Найдено {}'.format(number)

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
                if re.search(r'[^a-zA-Z]', Deletion.list_widget[0].text):
                    raise IndexError
                elif re.search(r'[^a-zA-Z]', Deletion.list_widget[1].text):
                    raise IndexError
                elif re.search(r'[^a-zA-Z]', Deletion.list_widget[2].text):
                    raise IndexError
                for i in range(0, globals.size_all):
                    i = i + delta
                    if Deletion.list_widget[0].text == globals.name[i] and Deletion.list_widget[1].text == \
                            globals.surname[i] and \
                            Deletion.list_widget[2].text == \
                            globals.middle_name[i]:
                        number += 1
                        View.remove_full_name('Удаленно {}'.format(number))
                        XmlParser.remove_student(i)
                        globals.stabilization()
                        Table.all_page = int((globals.size_all / globals.size))
                        Table.this_page = 0
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
                if Deletion.list_widget[0].text.isnumeric():
                    for i in range(0, globals.size_all):
                        i = i + delta
                        if Deletion.list_widget[0].text == globals.group[i]:
                            number += 1
                            View.remove_group('Удаленно {}'.format(number))
                            XmlParser.remove_student(i)
                            globals.stabilization()
                            Table.all_page = int((globals.size_all / globals.size))
                            Table.this_page = 0
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
                if Deletion.list_widget[0].text.isnumeric():
                    for i in range(0, globals.size_all):
                        i = i + delta
                        if Deletion.list_widget[0].text == globals.diseases[i]:
                            number += 1
                            View.remove_due_to_illness('Удаленно {}'.format(number))
                            XmlParser.remove_student(i)
                            globals.stabilization()
                            Table.all_page = int((globals.size_all / globals.size))
                            Table.this_page = 0

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
                if Deletion.list_widget[2].text.isnumeric():
                    for i in range(0, globals.size_all):
                        i = i + delta
                        if Deletion.list_widget[2].text == globals.other_reasons[i]:
                            number += 1
                            View.remove_for_other_reason_mode('Удаленно {}'.format(number))
                            Search.i_i += 1
                            XmlParser.remove_student(i)
                            globals.stabilization()
                            Table.all_page = int((globals.size_all / globals.size))
                            Table.this_page = 0
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
                if Deletion.list_widget[4].text.isnumeric():
                    pass
                else:
                    raise IndexError
                for i in range(0, globals.size_all):
                    i = i + delta
                    if Deletion.list_widget[4].text == globals.without_a_valid[i]:
                        number += 1
                        View.remove_for_no_good_reason_model('Удаленно {}'.format(number))
                        XmlParser.remove_student(i)
                        globals.stabilization()
                        Table.all_page = int((globals.size_all / globals.size))
                        Table.this_page = 0
                        delta -= 1
            except(IndexError):
                View.remove_for_no_good_reason_model('Ввод  должен быть числовой')

    @staticmethod
    def remove_due_to_illness_min_model():
        if len(globals.name) == 0:
            Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.diseases[i] = int(globals.diseases[i])

            min_number = min(globals.diseases)

            for i in range(0, globals.size_all):
                i = i + delta
                if globals.diseases[i] == min_number:
                    number += 1
                    Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    Table.all_page = int((globals.size_all / globals.size))
                    Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.diseases[i] = str(globals.diseases[i])

    @staticmethod
    def remove_due_to_illness_max_model():
        if len(globals.name) == 0:
            Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.diseases[i] = int(globals.diseases[i])

            max_number = max(globals.diseases)

            for i in range(0, globals.size_all):
                i = i + delta
                if globals.diseases[i] == max_number:
                    number += 1
                    Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    Table.all_page = int((globals.size_all / globals.size))
                    Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.diseases[i] = str(globals.diseases[i])

    @staticmethod
    def remove_for_other_reasons_min_model():
        if len(globals.name) == 0:
            Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.other_reasons[i] = int(globals.other_reasons[i])

            min_number = min(globals.other_reasons)

            for i in range(0, globals.size_all):
                i = i + delta
                if globals.other_reasons[i] == min_number:
                    number += 1
                    Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    Table.all_page = int((globals.size_all / globals.size))
                    Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.other_reasons[i] = str(globals.other_reasons[i])

    @staticmethod
    def remove_for_other_reasons_max_model():
        if len(globals.name) == 0:
            Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.other_reasons[i] = int(globals.other_reasons[i])

            max_number = max(globals.other_reasons)

            for i in range(0, globals.size_all):
                i = i + delta
                if globals.other_reasons[i] == max_number:
                    number += 1
                    Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    Table.all_page = int((globals.size_all / globals.size))
                    Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.other_reasons[i] = str(globals.other_reasons[i])

    @staticmethod
    def remove_for_no_good_reason_min_model():
        if len(globals.name) == 0:
            Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.without_a_valid[i] = int(globals.without_a_valid[i])

            min_number = min(globals.without_a_valid)

            for i in range(0, globals.size_all):
                i = i + delta
                if globals.without_a_valid[i] == min_number:
                    number += 1
                    Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    Table.all_page = int((globals.size_all / globals.size))
                    Table.this_page = 0
                    delta -= 1

            for i in range(0, globals.size_all):
                globals.without_a_valid[i] = str(globals.without_a_valid[i])

    @staticmethod
    def remove_for_no_good_reason_max_model():
        if len(globals.name) == 0:
            Deletion.list_widget[6].text = 'В списке нет записей'
        else:
            number = 0
            delta = 0
            Deletion.list_widget[6].text = 'Удаленно {}'.format(number)

            for i in range(0, globals.size_all):
                globals.without_a_valid[i] = int(globals.without_a_valid[i])

            max_number = max(globals.without_a_valid)

            for i in range(0, globals.size_all):
                i = i + delta
                if globals.without_a_valid[i] == max_number:
                    number += 1
                    Deletion.list_widget[6].text = 'Удаленно {}'.format(number)
                    XmlParser.remove_student(i)
                    globals.stabilization()
                    Table.all_page = int((globals.size_all / globals.size))
                    Table.this_page = 0
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
        FileSelection.list_file = files
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
        FileSelection.list_file = files
        number = len(FileSelection.list_file)
        for i in range(0, number):
            if Controller.Search.named.text == FileSelection.list_file[i]:
                View.show_chose_file('Выбор файла произошёл успешно')
                root = XmlParser.change_file(Controller.Search.named.text)
                globals.stabilization()
                Table.all_page = int((globals.size_all / globals.size))
                Table.this_page = 0
                break

            else:
                View.show_chose_file('Такого файла нет в дериктории')


class View:
    # представление первого окна

    @staticmethod
    def show_info_table_view():
        i_info = -1
        Table.stabilization()
        for i in range(0, globals.size):
            try:
                i_info += 1
                Table.list.append(Label(text=Model.get_name()))
                Controller.Search.info.add_widget(Table.list[i_info])
            except(IndexError):
                Table.list.append((Label(text="")))
                Controller.Search.info.add_widget(Table.list[i_info])
            try:
                i_info += 1
                Table.list.append(Label(text=Model.get_group()))
                Controller.Search.info.add_widget(Table.list[i_info])
            except(IndexError):
                Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(Table.list[i_info])
            try:
                i_info += 1
                Table.list.append(Label(text=Model.get_diseases()))
                Controller.Search.info.add_widget(Table.list[i_info])
            except(IndexError):
                Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(Table.list[i_info])
            try:
                i_info += 1
                Table.list.append(Label(text=Model.get_other_reasons()))
                Controller.Search.info.add_widget(Table.list[i_info])
            except(IndexError):
                Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(Table.list[i_info])
            try:
                i_info += 1
                Table.list.append(Label(text=Model.get_without_a_valid()))
                Controller.Search.info.add_widget(Table.list[i_info])
            except(IndexError):
                Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(Table.list[i_info])
            try:
                i_info += 1
                Table.list.append(Label(text=Model.get_total()))
                Controller.Search.info.add_widget(Table.list[i_info])
            except(IndexError):
                Table.list.append(Label(text=""))
                Controller.Search.info.add_widget(Table.list[i_info])
        i_info += 1
        Table.list.append(Label(text="Текущая страница:{}".format(Table.this_page), font_size=11))
        Controller.Search.info.add_widget(Table.list[i_info])
        i_info += 1
        Table.list.append(Label(text="Всего страниц:{}".format(Table.all_page), font_size=11))
        Controller.Search.info.add_widget(Table.list[i_info])
        i_info += 1
        Table.list.append(Widget())
        Controller.Search.info.add_widget(Table.list[i_info])
        i_info += 1
        Table.list.append(Widget())
        Controller.Search.info.add_widget(Table.list[i_info])
        i_info += 1
        if globals.size > globals.size_all:
            Table.list.append(Label(text="Записей на странице:{}".format(globals.size_all), font_size=11))
        else:
            Table.list.append(Label(text="Записей на странице:{}".format(globals.size), font_size=11))
        Controller.Search.info.add_widget(Table.list[i_info])
        i_info += 1
        Table.list.append(Label(text="Всего записей:{}".format(globals.size_all), font_size=11))
        Controller.Search.info.add_widget(Table.list[i_info])

    # представление  второго окна

    @staticmethod
    def show_status_adding_an_entry_view(text):
        AddingAnEntry.text = text

    # представление  четвертого окна

    @staticmethod
    def show_by_full_name():
        Search.i_w += 1
        Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Имя'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])
        Search.i_w += 1
        Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Фамилия'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])
        Search.i_w += 1
        Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Отчество'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])
        Search.i_w += 1
        Search.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])
        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_full_name))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

    @staticmethod
    def show_search_by_full_name(number):
        for i in range(0, globals.size_all):
            if Search.list_widget[0].text == globals.name[i] and Search.list_widget[1].text == \
                    globals.surname[i] and \
                    Search.list_widget[2].text == \
                    globals.middle_name[i]:
                number += 1
                Search.list_widget[3].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_by_group():
        Search.i_w += 1
        Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Группа'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])
        Search.i_w += 1
        Search.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])
        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_by_group))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

    @staticmethod
    def show_search_by_group(number):
        for i in range(0, globals.size_all):
            if Search.list_widget[0].text == globals.group[i]:
                number += 1
                Search.list_widget[1].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_by_view():
        Search.i_w += 1
        Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='По болезни'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])
        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_due_to_illness))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='По другим пичинам'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_other_reasons))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Без уважительной причины'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_no_good_reason))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

    @staticmethod
    def show_search_due_to_illness(number):
        for i in range(0, globals.size_all):
            if Search.list_widget[0].text == globals.diseases[i]:
                number += 1
                Search.list_widget[6].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_search_for_other_reasons(number):
        for i in range(0, globals.size_all):
            if Search.list_widget[2].text == globals.other_reasons[i]:
                number += 1
                Search.list_widget[6].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_search_for_no_good_reason(number):
        for i in range(0, globals.size_all):
            if Search.list_widget[4].text == globals.without_a_valid[i]:
                number += 1
                Search.list_widget[6].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_by_view_min_max():
        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск пропуски по болезни(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_due_to_illness_min))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])
        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск пропуски по болезни(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_due_to_illness_max))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск пропуски по другим причинам(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_other_reasons_min))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск пропуски по другим причинам(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_other_reasons_max))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск пропуски без уважительной причины(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_no_good_reason_min))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            Button(text='Поиск пропуски без уважительной причины(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_search_for_no_good_reason_max))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

        Search.i_w += 1
        Search.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Search.search.add_widget(Search.list_widget[Search.i_w])

    @staticmethod
    def show_search_due_to_illness_min(number, min_number):
        for i in range(0, globals.size_all):
            if globals.diseases[i] == min_number:
                number += 1
                Search.list_widget[6].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_search_due_to_illness_max(number, max_number):
        for i in range(0, globals.size_all):
            if globals.diseases[i] == max_number:
                number += 1
                Search.list_widget[6].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_search_for_other_reasons_min(number, min_number):
        for i in range(0, globals.size_all):
            if globals.other_reasons[i] == min_number:
                number += 1
                Search.list_widget[6].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_search_for_other_reasons_max(number, max_number):
        for i in range(0, globals.size_all):
            if globals.other_reasons[i] == max_number:
                number += 1
                Search.list_widget[6].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_search_for_no_good_reason_min(number, min_number):
        for i in range(0, globals.size_all):
            if globals.without_a_valid[i] == min_number:
                number += 1
                Search.list_widget[6].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    @staticmethod
    def show_search_for_no_good_reason_max(number, max_number):
        for i in range(0, globals.size_all):
            if globals.without_a_valid[i] == max_number:
                number += 1
                Search.list_widget[6].text = 'Найдено {}'.format(number)
                Search.i_i += 1
                Search.list_info.append(
                    Label(text=globals.name[i] + ' ' + globals.surname[i] + ' ' + globals.middle_name[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.group[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.diseases[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.other_reasons[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.without_a_valid[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

                Search.i_i += 1
                Search.list_info.append(Label(text=globals.total[i]))
                Controller.Search.info.add_widget(Search.list_info[Search.i_i])

    # представление  пятого окна

    @staticmethod
    def show_by_del_full_name():
        Deletion.i_w += 1
        Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Имя'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])
        Deletion.i_w += 1
        Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Фамилия'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])
        Deletion.i_w += 1
        Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Отчество'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])
        Deletion.i_w += 1
        Deletion.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])
        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_full_name))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

    @staticmethod
    def remove_full_name(text):
        Deletion.list_widget[3].text = text

    @staticmethod
    def show_by_del_group():
        Deletion.i_w += 1
        Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Группа'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])
        Deletion.i_w += 1
        Deletion.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])
        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_group))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

    @staticmethod
    def remove_group(text):
        Deletion.list_widget[1].text = text

    @staticmethod
    def show_by_del_view():
        Deletion.i_w += 1
        Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='По болезни'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])
        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_due_to_illness))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='По другим пичинам'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_other_reasons))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            TextInput(multiline=False, background_color='white', halign='left', cursor_blink=True, cursor_color='black',
                      foreground_color='black', font_size='14', hint_text='Без уважительной причины'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление', font_size='12', color='black', background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_no_good_reason))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

    @staticmethod
    def remove_due_to_illness(text):
        Deletion.list_widget[6].text = text

    @staticmethod
    def remove_for_other_reason_mode(text):
        Deletion.list_widget[6].text = text

    @staticmethod
    def remove_for_no_good_reason_model(text):
        Deletion.list_widget[6].text = text

    @staticmethod
    def show_by_del_view_min_max():
        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление пропуски по болезни(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_due_to_illness_min))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])
        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление пропуски по болезни(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_due_to_illness_max))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление пропуски по другим причинам(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_other_reasons_min))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление пропуски по другим причинам(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_other_reasons_max))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление пропуски без уважительной причины(мин)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_no_good_reason_min))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            Button(text='Удаление пропуски без уважительной причины(макс)', font_size='12', color='black',
                   background_color=[.32, .85, .94, 1],
                   background_normal='', on_press=Controller.on_press_remove_for_no_good_reason_max))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

        Deletion.i_w += 1
        Deletion.list_widget.append(
            Label(text='Статус', halign='left', valign='middle'))
        Controller.Delete.del_info.add_widget(Deletion.list_widget[Deletion.i_w])

    # представление шестого экрана

    @staticmethod
    def show_file(number, files):
        for i in range(0, number):
            FileSelection.i_t += 1
            FileSelection.list.append(Label(text=files[i], halign='left', valign='middle'))
            Controller.Search.file.add_widget(FileSelection.list[FileSelection.i_t])

    @staticmethod
    def show_chose_file(text):
        Controller.Search.status.text = text


# ScreenManager управляет перемещением между экранами
class ScreenManagerMy(ScreenManager):
    pass


screen_manager = ScreenManager()

# Добавьте экраны к менеджеру, а затем укажите имя
# используется для переключения экранов

screen_manager.add_widget(Table(name="screen_one"))

screen_manager.add_widget(AddingAnEntry(name="screen_two"))

screen_manager.add_widget(NumberOfEntries(name="screen_three"))

screen_manager.add_widget(Search(name="screen_four"))

screen_manager.add_widget(Deletion(name="screen_five"))

screen_manager.add_widget(FileSelection(name="screen_six"))


# Создать класс приложения

class ScreenApp(App):

    def build(self):
        return screen_manager


# запустить приложение
if __name__ == "__main__":
    sample_app = ScreenApp()

    sample_app.run()
