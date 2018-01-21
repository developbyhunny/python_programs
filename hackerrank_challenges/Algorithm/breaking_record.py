#!/bin/python3

import sys

def breakingRecords(score):
    hs = score[0]
    ls = score[0]
    cb = 0
    cw = 0
    for game in range(len(score)):
        if hs < score[game]:
            hs = score[game]
            cb += 1
        elif ls > score[game]:
            ls = score[game]
            cw += 1

    return [cb, cw]

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print(" ".join(map(str, result)))


