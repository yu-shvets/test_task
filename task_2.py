# Function that takes sentence as a parameter (e.g. handle_string(value)) and count number of letters and digits


def handle_string(value):

    letters = sum(i.isalpha() for i in value)
    digits = sum(i.isdigit() for i in value)

    return 'Letters' + ' - ' + str(letters) + '\n' + 'Digits' + ' - ' + str(digits)
