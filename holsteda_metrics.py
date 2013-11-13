__author__ = 'Artyom'

from Metrics import Metric
import re

class HosltedaMetrics(Metric):

    OPERATORS = [ '=','==','+','+=','-=','*=','/=','*',
                  '/','-','<<','%','**','!=','<','>','>=',
                  '**=','%=','<=','<==>','===','.eql?','.equal?' ]

    __total_operators = 0
    __unique_operators = 0

    def __init__(self, source_code):
            super(HosltedaMetrics, self).__init__(source_code)

    def __get_final_result(self):
        for operator in self.OPERATORS:
            operators_count = self.self._Metric__source_code._SourceCode__file_as_string.count(operator)
            if operators_count > 0:
                self.cleaned_code = self.cleaned_code.replace(operator, " ")
                self.__total_operators += operators_count
                self.__unique_operators.add(operator)
        self.total_operators_count += self.__total_operators
        self.unique_operators_count += len(self.__unique_operators)

    def get_metric_result_as_string(self):
        return str(self.__get_final_result())