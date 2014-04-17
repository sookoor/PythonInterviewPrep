#!/usr/bin/python
# Filename: perm.py
import sys

def _swap(a_list, i, j):
    a_list[i], a_list[j] = a_list[j], a_list[i]

def perm(a_list, k, n):
    if k == n:
        print a_list
    else:
        for i in range(k, n):
            _swap(a_list, i, k)
            perm(a_list, k + 1, n)
            _swap(a_list, i, k)

def main():
    a = [1, 2, 3, 4]
    perm(a, 0, 4)

if __name__ == "__main__":
    sys.exit(main())
