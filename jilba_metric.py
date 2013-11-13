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
            #self.__if_count += \
            #    re.findall('(^|$)if(\s+|\()([a-zA-Z][a-zA-Z\d]*)\s*={1,2}\s*([a-zA-Z][a-zA-Z\d]*)(\s+|\))(do|\{)',
            #                              self._Metric__source_code._SourceCode__file_as_string).__len__()
            self.__if_count += re.findall('(^|$)if(\s+|\().+(\s+|\))(do|\{)',
                                          self._Metric__source_code._SourceCode__file_as_string).__len__()
    def __find_unless_count(self):
            self.__unless_count += re.findall('(^|$)unless(\s+|\().+(\s+|\))(do|\{)',
                                          self._Metric__source_code._SourceCode__file_as_string).__len__()

    def __find_while_count(self):
            self.__while_count += re.findall('(^|$)while(\s+|\().+(\s+|\))(do|\{)',
                                          self._Metric__source_code._SourceCode__file_as_string).__len__()
    def __find_while_count(self):
            self.__each_map_count += re.findall('(^|$)\.(each|map)(\s+do|\s*\{)',
                                            self._Metric__source_code._SourceCode__file_as_string).__len__()

    def __get_final_result(self):
        return {
            "if's": self.__if_count,
            "unlesses": self.__unless_count,
            "whiles": self.__while_count
        }

    def get_metric_result_as_string(self):
        return str(self.__get_final_result())
