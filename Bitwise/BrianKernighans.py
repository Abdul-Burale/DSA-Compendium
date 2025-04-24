# The bitwise AND of a number range [m, n] can be efficiently computed using bit manipulation
# techniques, specifically bit shift or Brian Kernighan's Algorithm


def shiftBits(m, n):
    count = 0
    while m < n:
        m >>= 1; n >>= 1;
        count += 1

    return m << count


# Implements Brian Kernighan's algorithm to efficiently count the number of set bits in an integer.

def countSetBitsKernighan(n):
    count = 0
    while n:
        count += n & 1
        n = n >> 1

    return count

# Computes the bitwise AND of the integer range [m, n] using Brian Kernighan's principle.
def rangeBitwiseAndKernighan(m, n):
    while m < n:
        n = n & (n - 1)
