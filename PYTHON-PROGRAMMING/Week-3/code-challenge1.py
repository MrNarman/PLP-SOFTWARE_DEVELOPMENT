def large_power(base, exponent):
    """
    This function takes a base and an exponent as input and returns the result of base raised to the power of exponent.
    If the result is greater than 5000, it returns True; otherwise, it returns False.
    """
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
    
print(large_power(2, 13))  # True
print(large_power(2, 12))  # False