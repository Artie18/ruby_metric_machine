__author__ = 'Artyom'

import re


"""
Return:
    Info about all operands in string as hash
    { "unique_operants"         : [],
        "total_operands_count"  : y }
"""
def operands_count(source_as_string):
    operands = find_with_compare_operators(source_as_string) + find_with_assing_operators(source_as_string)
    operands += find_with_eql_operators(source_as_string)
    return {
        "unique_operants"       : set(operands),
        "total_operands_count"  : len(operands)
    }

def find_with_compare_operators(source_as_string):
    COMPARE_OPERATORS = [ '===','<==>','==','>=',
                          '<=','!=','<','>' ]
    operands = []
    for operator in COMPARE_OPERATORS:
            pattern = '\s+([a-zA-Z][a-zA-Z\d]*)\s*' + operator + '\s*([a-zA-Z][a-zA-Z\d]*)(\s+|$|\n)'
            match = re.finditer(pattern,source_as_string)
            for current in enumerate(match):
                operands.append(current[1].group(1))
                operands.append(current[1].group(2))
    return operands



def find_with_assing_operators(source_as_string):
    ASSING_OPERATORS = ['\+=','\-=','\*=','/=', '\*\*=','%=',
                          '\*\*','=','\+','\*','/','-','<<','%',]
    operands = []
    for operator in ASSING_OPERATORS:
        pattern = '(^|\n)([a-zA-Z][a-zA-Z\d]*)\s*' + operator + '\s*([a-zA-Z][a-zA-Z\d]*)($|\n)'
        match = re.finditer(pattern,source_as_string)
        for current in enumerate(match):
            operands.append(current[1].group(1))
            operands.append(current[1].group(2))
    return operands

def find_with_eql_operators(source_as_string):
    EQL_OPERATORS = ['.eql\?','.equal\?']
    operands = []
    for operator in EQL_OPERATORS:
        pattern = '(^|\n|\s+)([a-zA-Z][a-zA-Z\d]*)' + operator + '\s*([a-zA-Z][a-zA-Z\d]*)($|\n)'
        match = re.finditer(pattern,source_as_string)
        for current in enumerate(match):
            operands.append(current[1].group(1))
            operands.append(current[1].group(2))
    return operands
