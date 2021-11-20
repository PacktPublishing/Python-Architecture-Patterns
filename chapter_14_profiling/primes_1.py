
PRIMES = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97]
NUM_PRIMES_UP_TO = 5000


def check_if_prime(number):
    result = True

    for i in range(2, number):
        if number % i == 0:
            result = False

    return result


if __name__ == '__main__':
    # Calculate primes from 1 to NUM_PRIMES_UP_TO
    primes = [number for number in range(1, NUM_PRIMES_UP_TO)
              if check_if_prime(number)]
    # Compare the first primers to verify the process is correct
    assert primes[:len(PRIMES)] == PRIMES

    print('Primes')
    print('------')
    for prime in primes:
        print(prime)
    print('------')
