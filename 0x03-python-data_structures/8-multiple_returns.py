#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return
    else:
        return tuple(len(sentence)), tuple(sentence[0])