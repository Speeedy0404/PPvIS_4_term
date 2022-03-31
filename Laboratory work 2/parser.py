import xml.etree.ElementTree as ET

file = 'students.xml'
tree = ET.parse(file)
root = tree.getroot()


class Globals:

    def __init__(self):
        self.name = XmlParser.find_names(root)
        self.surname = XmlParser.find_surnames(root)
        self.middle_name = XmlParser.find_midllenames(root)
        self.group = XmlParser.find_group(root)
        self.diseases = XmlParser.find_diseases(root)
        self.other_reasons = XmlParser.find_otherreasons(root)
        self.without_a_valid = XmlParser.find_withoutavalid(root)
        self.total = XmlParser.find_total(root)
        self.size_all = len(self.name)
        self.size = 5
        self.directory = '/PyCharm/ППВиС/Laboratory_work_2/'

    def stabilization(self):
        self.name = XmlParser.find_names(root)
        self.surname = XmlParser.find_surnames(root)
        self.middle_name = XmlParser.find_midllenames(root)
        self.group = XmlParser.find_group(root)
        self.diseases = XmlParser.find_diseases(root)
        self.other_reasons = XmlParser.find_otherreasons(root)
        self.without_a_valid = XmlParser.find_withoutavalid(root)
        self.total = XmlParser.find_total(root)
        self.size_all = len(self.name)


class XmlParser:

    @staticmethod
    def change_file(del_file):
        global tree
        global root
        global file
        file = del_file
        tree = ET.parse(del_file)
        root = tree.getroot()
        return root

    @staticmethod
    def find_names(root):
        names = []
        for elem in root.findall('student'):
            names.append(elem.get('name'))
        return names

    @staticmethod
    def find_surnames(root):
        names = []
        for elem in root.findall('student'):
            names.append(elem.get('surname'))
        return names

    @staticmethod
    def find_midllenames(root):
        names = []
        for elem in root.findall('student'):
            names.append(elem.get('middlename'))
        return names

    @staticmethod
    def find_group(root):
        names = []
        for elem in root.findall('student'):
            names.append(elem.get('group'))
        return names

    @staticmethod
    def find_diseases(root):
        names = []
        for elem in root.findall('student'):
            names.append(elem.get('diseases'))
        return names

    @staticmethod
    def find_otherreasons(root):
        names = []
        for elem in root.findall('student'):
            names.append(elem.get('otherreasons'))
        return names

    @staticmethod
    def find_withoutavalid(root):
        names = []
        for elem in root.findall('student'):
            names.append(elem.get('withoutavalid'))
        return names

    @staticmethod
    def find_total(root):
        names = []
        for elem in root.findall('student'):
            names.append(elem.get('total'))
        return names

    @staticmethod
    def add_student(name, surname, middlename, group, diseases, otherreasons, withoutavalid, total):
        global file
        global root
        global tree
        data = ET.Element('students')
        item = ET.SubElement(data, 'student')
        item.set('name', name)
        item.set('surname', surname)
        item.set('middlename', middlename)
        item.set('group', group)
        item.set('diseases', diseases)
        item.set('otherreasons', otherreasons)
        item.set('withoutavalid', withoutavalid)
        item.set('total', total)
        root.append(item)
        tree.write(file)  # перезапись

    @staticmethod
    def remove_student(number):
        global file
        root.remove(root[number])
        tree.write(file)


globals = Globals()
