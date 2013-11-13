__author__ = 'Artyom'

from Metrics import Metric
import re

class HosltedaMetrics(Metric):

    OPERATORS = [ '===','<==>','==','+=','-=','*=','/=',
                  '>=','**=','%=','<=','!=','**','=','+','*',
                  '/','-','<<','%','<','>','.eql?','.equal?' ]

    __total_operators           = 0
    __unique_operators_count    = 0
    __unique_operators          = []

    def __init__(self, source_code):
            super(HosltedaMetrics, self).__init__(source_code)

    def __generate_result(self):
        return {
            "Total operators"   : self.__total_operators        ,
            "Unique operators"  : self.__unique_operators_count
        }

    def __count_operators_statistic(self):
        cleaned_code = self._Metric__source_code._SourceCode__file_as_string
        for operator in self.OPERATORS:
            operators_count = cleaned_code.count(operator)
            if operators_count > 0:
                cleaned_code = cleaned_code.replace(operator, " ")
                self.__total_operators += operators_count
                self.__unique_operators.append(operator)
        self.__unique_operators_count += len(self.__unique_operators)

    def __get_final_result(self):
        self.__count_operators_statistic()
#self.__count_operands()
        return self.__generate_result()

    def get_metric_result_as_string(self):
        return str(self.__get_final_result())
