def sum_the_series(n):
    if n <= 1:
        return 1/2
    
    return n/(n+1) + sum_the_series((n-1))

result = round(sum_the_series(5),2)
print(f"The sum of the series is {result}")