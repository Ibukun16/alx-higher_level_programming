#!/usr/bin/python3
def multiple_returns(sentence):
    """A tuple with length of characters and first letter"""
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
