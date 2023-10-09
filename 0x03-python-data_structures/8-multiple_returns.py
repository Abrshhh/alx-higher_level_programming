#!/usr/bin/python3
sentence = (2, 2, 3, 4)


def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
