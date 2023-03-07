animals = {
    0: 'Monkey',
    1: "Rooster",
    2: "Dog",
    3: "Pig",
    4: "Rat",
    5: "Ox",
    6: "Tiger",
    7: "Rabbit",
    8: "Dragon",
    9: "Snake",
    10: "Horse",
    11: "Goat",
}

year = input("please enter valid year when you was born:")

while not year.isdigit():
    year = input("please enter valid year when you was born:")
year=int(year)
horoscope = year % 12
print("%d year is %s year" % (year, animals[horoscope]))
