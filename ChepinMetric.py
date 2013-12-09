__author__ = 'Artyom'

from Metrics import Metric
import re


class ChepinMetric(Metric):
        #Vars for final matrics result
        __p = 0
        __m = 0
        __c = 0
        __t = 0

        # static coof
        A1 = 1
        A2 = 2
        A3 = 3
        A4 = 0.5

        __all_vars = [] # all vars


        def __init__(self, source_code):
            super(ChepinMetric, self).__init__(source_code)

        def __all_vars_for_input_count(self):
            match = re.findall('(^||\n)\s*[a-zA-Z][a-zA-Z\d]*\s=\sgets.chown($||\n)',
                            self._Metric__source_code._SourceCode__file_as_string)
            return match.__len__()

        def __all_vars_for_output_count(self):
            count = 0
            match = re.findall('(^|\n)?\s*(print|puts|p)\s+([a-zA-Z]*[a-zA-Z\d]+)',
                               self._Metric__source_code._SourceCode__file_as_string)
            count += match.__len__()
            match = re.findall('(^|\n)?\s*(print|puts|p)\s*\(+\s*([a-zA-Z][a-zA-Z\d]+)\s*\)',
                               self._Metric__source_code._SourceCode__file_as_string)
            count += match.__len__()
            return count

        def __all_vars_assinged_to_digit_in_source_cont(self):
            match = re.findall('(^|\n)\s*[a-zA-Z][a-zA-Z\d]*\s=\s(\d+\.?\d*)($|\n)',
                               self._Metric__source_code._SourceCode__file_as_string)
            return match.__len__()

        def __all_vars_assinged_to_string_in_source_count(self):
            count = 0
            match = re.findall('(^|\n)[a-zA-Z][a-zA-Z\d]*\s?=\s?(\'.*\')($|\n)',
                               self._Metric__source_code._SourceCode__file_as_string)
            count += match.__len__()
            match = re.findall('(^|\n)\s*[a-zA-Z][a-zA-Z\d]*\s?=\s?(\".*\")($|\n)',
                               self._Metric__source_code._SourceCode__file_as_string)
            count += match.__len__()
            return count

        def __all_vars_assinged_count(self):
            match = re.findall('(^|\n)\s*[a-zA-Z][a-zA-Z\d]*\s?=\s?.+($|\n)',
                               self._Metric__source_code._SourceCode__file_as_string)
            return match.__len__()

        def __all_vars_that_are_useless_count(self):
            usless_var_count = i = 0
            match = re.findall('(^|\n)\s*([a-zA-Z][a-zA-Z\d])*\s?=\s?(.)+($|\n)',
                                self._Metric__source_code._SourceCode__file_as_string)

            for cur in match:
                cur_var = cur[1]
                pattern = '(^|\n)?\s*'+ cur_var +'\s+'
                match_all = re.findall(pattern,
                                   self._Metric__source_code._SourceCode__file_as_string)
                all_current_var = match_all.__len__()
                pattern = '(^|\n)' + cur_var + '\s?=\s?(.)+($|\n)'
                match_unused = re.findall(pattern,
                                   self._Metric__source_code._SourceCode__file_as_string)
                all_useless_var = match_unused.__len__()
                if all_current_var - all_useless_var > 0:
                    usless_var_count += 1
            return usless_var_count

        def __find_all_assignings(self):
            match = re.findall('(^|\n)\s*((@+)?[a-zA-Z][a-zA-Z\d]*)\s*=\s*.+($|\n)',
                               self._Metric__source_code._SourceCode__file_as_string)
            return len(match)
        def __find_all_p(self):
            self.__p += self.__all_vars_for_input_count()
            self.__p += self.__all_vars_for_output_count()

        def __find_all_m(self):
            self.__m += self.__find_all_assignings()
            #self.__m += self.__all_vars_assinged_to_digit_in_source_cont()
            #self.__m += self.__all_vars_assinged_to_string_in_source_count()
            #self.__m += self.__all_vars_assinged_count()

        def __find_all_t(self):
            self.__t += self.__all_vars_that_are_useless_count()

        def __generate_result(self):
            return {
                "Chepin Result": self.A1 * self.__p + self.A2 * self.__m + self.A4 * self.__t ,
                "P": self.__p,
                "M": self.__m,
                "C": self.__c,
                "T": self.__t,
            }

        def __get_final_result(self):
            self.__find_all_p()
            self.__find_all_m()
            self.__find_all_t()
            return self.__generate_result()

        def get_metric_result_as_string(self):
            return str(self.__get_final_result())




