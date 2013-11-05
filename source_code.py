import re

# TODO change regex for better understanding


class SourceCode:
    #*** Private Var for methods ***#
    __ends_needed_to_be_closed = []
    __number_of_lines = 0
    __file_in_lines = ''

    def __init__(self, file_as_a_string):
        self.__file_in_lines = file_as_a_string.split('\n;')
        self.__number_of_lines = len(self.__file_in_lines)

    def check_if_valid(self):
        try:
            for line_index, line in enumerate(self.__file_in_lines):
                if(self.__is_class(line)):
                    self.check_the_class(line_index)
                elif(self.__is_function(line)):
                    self.check_the_function(line_index)
                else:
                    self.__check_other_options(line)
        except ValueError:
            raise ValueError('Something is not valid in your source code')

            #splited_line = line.split()
            #for elem in splited_line:

    #*** Private methods ***#
    def check_the_class(self, line_index):
        for line in self.__file_in_lines[line_index:]:
            if(self.__is_function(self.__file_in_lines[line_index])):
                self.check_the_function(self, line_index)
            else:
                self.__check_other_options(line)

    def check_the_function(self, line_index):
        for line in self.__file_in_lines[line_index:]:
            pass

    #*** Boolean functions ***#
    def __check_other_options(self, line):
        if(self.__check_if_variable(line)):
            return True
        else:
            raise ValueError('Unrecognizable line')

    def __is_function(self, line):
        return re.search("^ *def [a-z]*", line)

    def __is_class(self, line):
        return re.search("^ *class [A-Z][a-zA-Z]*", line)

    def __check_if_variable(self, line):
        # Checking for int or float var
        if self.__check_if_assining_int_or_dec(line):
            return True
        # Checking for empty array or hash
        # TODO add non empty support
        elif re.search("^\s*[a-z]+,?[a-z]*\s*=\s*[\{\[][\]\}][\s]*$",line):
            return True
        #Checking for a string empty or non empty
        elif re.search('^\s*[a-z]+,?[a-z]*\s*=\s*([\'].*[\'])|([\"].*[\
"])[\s]*$',line):
            return True
        else:
            # TODO add Error handeling
            return False

    def __check_if_assining_int_or_dec(self, line):
        splited_line = line.split("=")
        if len(splited_line) == 2:
            if self.__check_first_of_assining(splited_line[0]):
                if self.__is_dec_or_int(splited_line[1]):
                    return True
        return False

    def __is_dec_or_int(self, line):
        return re.match("^\s*[\d]+[.]*[\d]*[\s]*$", line)

    def __check_first_of_assining(self, line):
        return re.match("^\s*[a-z]+,?[a-z]*\s*", line)

    def __check_if_string(self, incoming):
        return re.match("^\s*([\'].*[\'])|([\"].*[\"])[\s]*$", incoming)

    #*** Private attributes return ***#

    #def ends_needed_to_be_closed(self): #Not sure if I will use it
    #    return self.__ends_needed_to_be_closed

    def number_of_lines(self):
        return self.__file_in_lines

    #@staticmethod
    #def check_if_valid_inside_class

