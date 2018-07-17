# Prime generator
import itertools as it

class Prime():
    from itertools import islice
    
    def _check(n, primes):
        for p in primes:
            if not n % p:
                return False
        return True
    
    def nth( n , default = 0):
        global it
        "Returns the nth item or a default value"
        return next(it.islice(Prime.sieve(), n, None), default)

    def sieve():
        global it
        primes = set()
        for n in it.count(2):
            if Prime._check(n, primes):
                primes.add(n)
                yield n

    def pi():
        global it
        primes = set()
        for n in it.count(2):
            if Prime._check(n, primes):
                primes.add(n)
            yield len(primes)
