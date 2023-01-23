# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"


def check_password(password):
    is_lower = False
    is_upper = False
    is_digit = False
    is_speacial = False
    for char in password:
        if char.isalpha():
            if char.isupper():
                is_upper = True
            else:
                is_lower = True
        elif char.isdigit():
            is_digit = True
        elif char == "$" or char == "!" or char == "@":
            is_speacial = True
    return (
        len(password) >= 6
        and len(password) <= 12
        and is_lower
        and is_upper
        and is_digit
        and is_speacial
    )
