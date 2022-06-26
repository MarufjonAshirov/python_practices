import math


def double(num):
    return num ** 2


def triple(num):
    return num ** 3


def sqrt_(num):
    return math.sqrt(num)


def is_prime(num, i=2):
    if num <= 2:
        return True if (i == 2) else False
    if num % i == 0:
        return False
    if i * i > num:
        return True
    return is_prime(num, i + 1)


def is_integer(num):
    if isinstance(num, int):
        return True
    else:
        return False


def is_letter(letter):
    if letter.isalpha():
        return True
    else:
        return False


def my_higher_order_function(i, func):
    return func(i)


print(my_higher_order_function(2, double))
print(my_higher_order_function(2, triple))
print(my_higher_order_function(16, sqrt_))
print(my_higher_order_function(2, is_prime))
print(my_higher_order_function(4, is_prime))
print(my_higher_order_function(2, is_integer))
print(my_higher_order_function('A', is_integer))
print(my_higher_order_function('A', is_letter))
print(my_higher_order_function('1', is_letter))
