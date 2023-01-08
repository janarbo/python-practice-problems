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


# noqa # solution
def halve_the_list(input):  # noqa # solution
    first_list = []
    second_list = []
    len_list1 = len(input) // 2 + len(input) % 2

    for i in range(len_list1):
        first_list.append(input[i])
    for i in range(len(input) // 2):
        index = i + len_list1
        second_list.append(input[index])
    return first_list, second_list
