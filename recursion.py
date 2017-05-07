#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Assignment 14 Fibonnaci"""

def fibonacci(n):
    """ fibonacci"""
    if isinstance(n, int) and n > 0:
        if n == 1 or n == 0:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return False


def gcd(num_a, num_b):
    """ GCD Algorithm"""

    if num_b == 0 or num_a < num_b:
        return False
    div = num_a
    rem = num_a % num_b
    if rem == 0:
        return num_b
    else:
        return gcd(div, rem)
    

def strcomp(str1, str2):
    """ Compare two strings"""

    idx1 = len(str1)
    idx2 = len(str2)

    s1 = str1[idx1 - 1] if idx1 > 0 else str1
    s2 = str2[idx2 - 1] if idx2 > 0 else str2

    if s1 > s2 or idx1 > idx2:
        return 1
    if s1 < s2 or idx1 < idx2:
        return -1
    if s1 == s2 and (idx1 > 0) == (idx2 > 0):
        s1 = str1[:len(str1) - 1]
        s2 = str2[:len(str2) - 1]
        strcomp(s1, s2)
    return 0
