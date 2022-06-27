def convert(currency, rate):
    return currency * rate


def curry(func, num):
    return lambda y: func(num, y)


dollar_to_sterling = curry(convert, 0.77)
print(dollar_to_sterling(5))
