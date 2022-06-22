num = input('enter number to check prime\n')
if num.isnumeric():
    num = int(num)
    if num == 1 or num == 0:
        print('{} is not prime'.format(num))
    else:
        div_ = num // 2
        temp = 0
        for i in range(2, div_):
            if num % i == 0:
                temp += 1
                break
        if temp == 0:
            print('{} is prime'.format(num))
        else:
            print('{} is complex'.format(num))
else:
    print('Invalid input')
