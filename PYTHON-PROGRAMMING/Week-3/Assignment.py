def calculate_discount(price, discount_percentage):
    """
    Calculate the discounted price based on the original price and discount percentage.
    Apply discount only if the disacount percentage is >= 20%
    """

    if discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * price
        discounted_price = price - discount_amount
        return discounted_price
    else:
        return price
    
user_price = float(input("Enter the original price: "))
user_discount = float(input(r"Enter the discount percentage (Do not include the % sign): "))
print(calculate_discount(user_price, user_discount))  # Outputs the discounted price or original price
