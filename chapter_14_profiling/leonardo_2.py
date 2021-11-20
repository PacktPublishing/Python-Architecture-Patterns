
CACHE = {}


def leonardo(number):

    if number in (0, 1):
        return 1

    if number not in CACHE:
        result = leonardo(number - 1) + leonardo(number - 2) + 1
        CACHE[number] = result

    return CACHE[number]


NUMBER = 35000
for i in range(NUMBER + 1):
    print(f'leonardo[{i}] = {leonardo(i)}')
