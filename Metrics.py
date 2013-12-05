from abc import abstractmethod

__author__ = 'Artyom'

import re
from source_code import SourceCode


class Metric(object):
    __source_code = 0 # used for source_code object

    def __init__(self, source_code):
        if(source_code.is_valid):
            self.__source_code = source_code

    @abstractmethod
    def get_metric_result_as_string(self):
        pass




