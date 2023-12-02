#!/usr/bin/python3

def multiple_returns(sentence):
    # Check if input string (sentence) is empty
    if not sentence:
        # If empty, it returns None
        return (0, None)
    else:
        # If not empty, it returns tuple with the length 
        # of a string and its first character
        return (len(sentence), sentence[0])
