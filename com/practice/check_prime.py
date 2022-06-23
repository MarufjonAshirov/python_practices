def prime_check(n, i=2):
    if n <= 2:
        return True if (n == 2) else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return prime_check(n, i + 1)


num = int(input('enter number to check prime'))
print(prime_check(num))
