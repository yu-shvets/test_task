'''Function that takes list of tuples (e.g. handle_list_of_tuples(list)) and sort it based on the next rules:
name / age / height / weight'''


def handle_list_of_tuples(a_list):

    return sorted(a_list, key=lambda x: (x[0], x[1], x[2], x[3]))
