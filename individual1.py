#!/usr/bin/env python

from module_1 import func

if __name__ == "__main__":
    cnt = func()
    k = int(input("Введите значение: "))
    result = cnt(k)
    print(result)