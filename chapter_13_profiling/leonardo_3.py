
CACHE = {}


@profile
def leonardo(number):

    if number in (0, 1):
        return 1

    if number not in CACHE:
        result = leonardo(number - 1) + leonardo(number - 2) + 1
        CACHE[number] = result

    ret_value = CACHE[number]

    MAX_SIZE = 5
    while len(CACHE) > MAX_SIZE:
        # Maximum size allowed,
        # delete the first value, which will be the oldest
        key = list(CACHE.keys())[0]
        del CACHE[key]

    return ret_value


NUMBER = 35000
for i in range(NUMBER + 1):
    print(f'leonardo[{i}] = {leonardo(i)}')
