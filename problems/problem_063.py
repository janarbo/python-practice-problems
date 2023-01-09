# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem
def shift_letters(inputs):
    results = ""
    new_letter = ""
    for each in inputs:
        if each == "Z":
            new_letter = "A"
        elif each ==  "z":
            new_letter = "a"
        else:
            new_letter = chr(ord(each) + 1)
        results += new_letter
    return results
print(shift_letters("Zahara"))
