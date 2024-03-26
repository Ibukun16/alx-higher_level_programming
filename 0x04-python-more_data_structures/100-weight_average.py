#!/usr/bin/python3
def weight_average(my_list=[]):
    """A function that returns the weighted average 
     of all integers in a tuple."""
    if not my_list:
        return 0
    tot_score = 0
    tot_freq = 0
    for col in my_list:
        tot_score += (col[0] * col[1])
        tot_freq += col[1]
    return tot_score / tot_freq
