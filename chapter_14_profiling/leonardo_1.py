
def leonardo(number):

    if number in (0, 1):
        return 1

    return leonardo(number - 1) + leonardo(number - 2) + 1


NUMBER = 35
for i in range(NUMBER + 1):
    print('leonardo[{}] = {}'.format(i, leonardo(i)))
