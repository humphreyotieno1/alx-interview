#!/usr/bin/python3
'''Prime game algorithm'''


def sieve(n):
    '''Generate prime numbers'''
    prime = [True for number in range(n + 1)]
    start_prime = 2

    while (start_prime * start_prime <= n):
        if prime[start_prime]:
            for num in range(start_prime * start_prime, n + 1, start_prime):
                prime[num] = False
        start_prime += 1

    list_prime = [i for i in range(2, n+1) if prime[i]]
    return list_prime


def isWinner(x, nums):
    '''Function to determine winner'''
    max_to_reach = max(nums)
    primes = sieve(max_to_reach)

    prime_count = [0] * (max_to_reach + 1)
    for prime in primes:
        for i in range(prime, max_to_reach + 1, prime):
            prime_count[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
