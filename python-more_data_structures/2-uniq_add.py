#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new_list = []
    for values in my_list:
        if values not in new_list:
            new_list.append(values)
    return (sum(new_list))
