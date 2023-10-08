#!/usr/bin/python3
sentence = (2, 2, 3, 4)


def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    elif len(sentence) > 0:
        x = len(sentence)
    return x, sentence[0]
