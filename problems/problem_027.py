# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#


def max_in_list(values):
    if len(values) == 0:
        return None
    max = values[0]
    for each_value in values:
        if each_value > max:
            max = each_value
    return max
