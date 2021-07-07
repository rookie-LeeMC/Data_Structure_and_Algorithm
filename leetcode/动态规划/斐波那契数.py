# -*- coding:UTF-8 -*-
'''

'''


def fib(n: int) -> int:
    if n < 2: return n
    first, second = 0, 1

    for i in range(n - 1):
        ans = first + second
        first = second
        second = ans

    return ans


print(fib(2))
print(fib(3))
print(fib(4))
