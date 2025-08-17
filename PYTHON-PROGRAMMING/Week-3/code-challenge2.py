def divisible_by_ten(num):
    """
    This function checks if a given number is divisible by 10.
    """
    if num % 10 == 0:
        return True
    else:
        return False
    

print(divisible_by_ten(20))  # Expected output: True