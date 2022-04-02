import xml.etree.ElementTree as ET

tree = ET.parse('score.xml')
root = tree.getroot()


class XmlParser:

    @staticmethod
    def find_score(root):
        score = []
        for elem in root.findall('score'):
            score.append(elem.get('number'))
        return score

    @staticmethod
    def find_name(root):
        score = []
        for elem in root.findall('score'):
            score.append(elem.get('name'))
        return score

    @staticmethod
    def change_score(current_score, number):
        root[current_score].set('number', str(number))
        tree.write('score.xml')  # перезапись
