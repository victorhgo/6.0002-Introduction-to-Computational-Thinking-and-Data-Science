def fastFib(n, memo = {}):
    """ n is an integer and n > 0, 
    memo is the dictionary that stores every fib(n) calculated, only used by recursive calls
    return Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result

        return result
    
# Test it
for n in range(121):
    print(f"fib({n}) = {fastFib(n)}")