

def check_if_prime(unsigned int number):
    cdef int counter = 2

    if number == 0:
        return False

    while counter < number:
        if number % counter ==  0:
            return False

        counter += 1

    return True
