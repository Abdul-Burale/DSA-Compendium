#Binary value of whether a number is prime or not
Sieve = [1] * (int(1e6) + 1)
Sieve[0], Sieve[1] = 0
for i in range(2, int(1e6)**0.5):
    if Sieve[i]:
        # If 'i' remains marked (true), it's a prime number.
        # Consequently, all its multiples (starting from 2*i) within the range
        # are composite (not primes) and are marked accordingly.
        for j in range(i*2, int(1e6) + 1, i):
            Sieve[j] = 0
