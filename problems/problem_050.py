# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]


def halve_the_list(list):
    list1 = []
    list2 = []
    len_list1 = len(list) // 2 + len(list) % 2

    for i in range(len_list1):
        list1.append(list[i])
    for i in range(len(list) // 2):
        index = len_list1 + i
        list2.append(list[index])
    return list1, list2
