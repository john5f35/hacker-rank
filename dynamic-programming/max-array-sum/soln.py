#!/bin/python3

import math
import os
import random
import re
import sys

# Let $S_k$ be the maximum sum of subsets up to $a_k$, then
#  S_k = max\{ S_{k-2}, a_k, S_{k-2} + a_k, S_{k-1} \}
# Then build up the solution from $0$, to $n = len(arr)$.
def maxSubsetSum(arr: [int]):
    tbl = [None] * len(arr)
    tbl[0] = arr[0]

    def _subsum(n):
        if n < 0:
            return None
        if tbl[n]:
            return tbl[n]

        choices = [arr[n], _subsum(n - 1)]
        s_n_2 = _subsum(n - 2)
        if s_n_2:
            choices += [s_n_2, s_n_2 + arr[n]]
        choices = list(filter(lambda x: x is not None, choices))

        if len(choices) > 0:
            tbl[n] = max(choices)
            return tbl[n]

    for n in range(len(arr)):
        _subsum(n)

    return _subsum(len(arr) - 1)

def test_1():
    arr = [-2, 1, 3, -4, 5]
    assert maxSubsetSum(arr) == 8

def test_2():
    arr = [3, 7, 4, 6, 5]
    assert maxSubsetSum(arr) == 13

def test_3():
    arr = [2, 1, 5, 8, 4]
    assert maxSubsetSum(arr) == 11

def test_4():
    arr = [3, 5, -7, 8, 10]
    assert maxSubsetSum(arr) == 15

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
