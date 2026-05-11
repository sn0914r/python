# Print the first `n` numbers of the Fibonacci series.

def fibonacci_series(num):
    fn = 0
    sn = 1
    series = [0, 1]
    count = 2

    while count < num:
        tn = fn + sn
        series.append(tn)
        fn, sn = sn, tn
        count += 1
    
    return series

print(fibonacci_series(5))
print(fibonacci_series(7))