__author__ = 'Artyom'

from Metrics import Metric
import re
import math
from operands import *

class HosltedaMetrics(Metric):

    OPERATORS = [ '===','<==>','==','+=','-=','*=','/=',
                  '>=','**=','%=','<=','!=','**','=','+','*',
                  '/','-','<<','%','<','>','.eql?','.equal?', '|', '!', '^', '~', '>>',
                  'and', '&&', '||', 'not']

    __total_operators           = 0
    __total_operands            = 0
    __unique_operators          = []
    __unique_operands           = []

    __program_dictionary            = 0
    __program_length                = 0
    __program_coding_quality        = 0.0
    __program_coding_laboriousness  = 0
    __program_volume                = 0

    def __init__(self, source_code):
            super(HosltedaMetrics, self).__init__(source_code)

    def __generate_result(self):
        result = {
            "Total operators"       : self.__total_operators                ,
            "Unique operators"      : len(self.__unique_operators)          ,
            "Total operands"        : self.__total_operands                 ,
            "Unique operands"       : len(self.__unique_operands)           ,
            "Program Dictionary"    : self.__program_dictionary             ,
            "Program Length"        : self.__program_length                 ,
            "Program Volume"        : self.__program_volume                 ,
            "Program Difficulty"    : self.__program_difficulty             ,
            "Effort"                : self.__effort
        }
        return result

    def __count_operands(self):
        results = operands_count(self._Metric__source_code._SourceCode__file_as_string)
        self.__unique_operands  = results["unique_operants"]
        self.__total_operands   = results["total_operands_count"]
        results = None

    def __count_operators_statistic(self):
        cleaned_code = self._Metric__source_code._SourceCode__file_as_string
        pattern = "(-|\*|\*\*|%|\+|<=|>=|!=|=|>|<|<=>|===|==|\sand\s|\sor\s|eql|equal|\*=|/=|%=|\*\*=|-=|\+=|&&|\|\||!|\snot\s+)"
        match = re.findall(pattern, cleaned_code)
        self.__total_operators = len(match)
        for operator in match:
            if not operator in self.__unique_operators:
                self.__unique_operators.append(operator.strip())

    def __get_final_result(self):
        self.__unique_operators = []
        self.__count_operators_statistic()
        self.__count_operands()
        self.__program_length  = self.__total_operands + self.__total_operators
        self.__program_dictionary = len(self.__unique_operands) + len(self.__unique_operators)
        self.__program_volume = self.__program_length * math.log(self.__program_dictionary, 2)

        #self.__program_coding_quality = \
            #(2 * len(self.__unique_operands)) / float((len(self.__unique_operators) * self.__total_operands)) // VOLUME'/VOLUME
        try:
            self.__program_difficulty = (len(self.__unique_operators) / 2) * (self.__total_operands / len(self.__unique_operands))
            self.__effort = self.__program_difficulty * self.__program_volume
        except ZeroDivisionError:
            print "Not enough data to process"
        #self.__program_coding_laboriousness = 1 / self.__program_coding_quality

        return self.__generate_result()

    def get_metric_result_as_string(self):
        return str(self.__get_final_result())
