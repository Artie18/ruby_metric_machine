__author__ = 'Artyom'

from Metrics import Metric
import re

class JilbaMetric(Metric):
    __if_count = 0
    __unless_count = 0
    __while_count = 0
    __each_map_count = 0

    def __init__(self, source_code):
            super(JilbaMetric, self).__init__(source_code)

    def __find_if_count(self):
            self.__if_count += re.findall('(^|\n)\s*if(\s+|\().+(\s+|\)|\n|$)',
                                          self._Metric__source_code._SourceCode__file_as_string).__len__()
    def __find_unless_count(self):
            self.__unless_count += re.findall('(^|\n)\s*unless(\s+|\().+(\s+|\)|\n|$)',
                                          self._Metric__source_code._SourceCode__file_as_string).__len__()
    def __find_while_count(self):
            self.__while_count += re.findall('(^|\n)\s*while(\s+|\().+(\s+|\)|\n|$)',
                                          self._Metric__source_code._SourceCode__file_as_string).__len__()
    def __find_each_map_count(self):
            self.__each_map_count += re.findall('(^|\n)\s*([a-zA-Z][a-zA-Z\d]*)\.(each|map)(\s+do|\s*\{)',
                                            self._Metric__source_code._SourceCode__file_as_string).__len__()

    def __generate_result(self):
        return {
            "if's": self.__if_count,
            "unlesses": self.__unless_count,
            "whiles": self.__while_count,
            "Eaches and Maps": self.__each_map_count
        }

    def __get_final_result(self):
        self.__find_if_count()
        self.__find_each_map_count()
        self.__find_unless_count()
        self.__find_while_count()
        return self.__generate_result()

    def get_metric_result_as_string(self):
        return str(self.__get_final_result())
