import xml.etree.ElementTree as XML_module


class ConfigData:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.tree = None
        self.root = None
        self.error_message = None
        self.config_list = []
        self.error_check = self.get_root()
        self.get_config_data()

    def get_root(self):
        try:
            tree = XML_module.parse(self.config_file_path)
            root = tree.getroot()
            self.tree = tree
            self.root = root
            return True
        except XML_module.ParseError as err:
            err.msg = "Ошибка разметки файла"
            self.error_message = err.msg
            return False
        except FileNotFoundError as err:
            err.msg = '{}'.format(err)
            self.error_message = err.msg
            return False

    def get_config_data(self):
        if self.error_check:
            self.config_list = []
            for child in self.root.findall('cayman'):
                config_dict = child.attrib
                self.config_list.append(config_dict)
