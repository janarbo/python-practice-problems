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
    list_1 = []
    list_2 = []

    if len(list) % 2 == 0:
        for each in list[range(len(list)//2 + 1)]:
            list_1.append(each)
        for each in list[(len(list)//2), len(list)]:
            list_1.append(each)
    if len(list) % 2 == 1:
        for each in list[range(int(len(list)//2 + 2) )]:
            list_1.append(each)
        for each in list[range(int(len(list)//2 + 1)), len(list)]:
            list_2.append(each)
    return list_1, list_2
