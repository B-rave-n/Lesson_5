import string
import keyword
def test_variable(variable):
    strings = [i for i in string.punctuation if i != '_']
    strings.extend([' ', '__'])
    count_of_strings = 0
    for i in strings:
        if i in variable:
            count_of_strings = 1
    if variable in keyword.kwlist or count_of_strings or variable[0].isdigit() or variable.lower() != variable:
        return False
    else:
        return True

assert test_variable('_') == True, 'Test1'
assert test_variable('__') == False, 'Test2'
assert test_variable('___') == False, 'Test3'
assert test_variable('x') == True, 'Test4'
assert test_variable('get_value') == True, 'Test5'
assert test_variable('get value') == False, 'Test6'
assert test_variable('get!value') == False, 'Test7'
assert test_variable('some_super_puper_value') == True, 'Test8'
assert test_variable('Get_value') == False, 'Test9'
assert test_variable('get_Value') == False, 'Test10'
assert test_variable('getValue') == False, 'Test11'
assert test_variable('3m') == False, 'Test12'
assert test_variable('m3') == True, 'Test13'
print("ОК")