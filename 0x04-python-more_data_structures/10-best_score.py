#!/usr/bin/python3
def best_score(a_dictionary):
    """A function that returns the biggest integer value
    in a dictionary."""
    if not a_dictionary:
        return None
    else:
        best_key = list(a_dictionary)[0]
        best_score = a_dictionary[best_key]

    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            best_key = key
    return best_key
