def divide(dividend, divisor):
    
    less_than_zero = False
    if dividend < 0 or divisor < 0:
        less_than_zero = True

    dividend = abs(dividend)
    divisor = abs(divisor)
    res = 0
    while dividend >= divisor:
        dividend = dividend - divisor
        res += 1

    return res if not less_than_zero else res*(-1)

dividend = 10
divisor = 5
print(divide(dividend, divisor))
