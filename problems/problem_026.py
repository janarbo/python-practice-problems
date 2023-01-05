# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average


def calculate_grade(values):

    if len(values) == 0:
        return None
    sum = 0
    for score in values:
        0 < score < 100
        sum += score
    average_score = sum / len(values)

    if average_score >= 90:
        return "A"
    if average_score >= 80:
        return "B"
    if average_score >= 70:
        return "C"
    if average_score >= 60 and average_score <= 70:
        return "D"
    else:
        return "F"
