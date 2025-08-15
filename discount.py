def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount = price * (discount_percent/100)
        final_price = int(price - discount)
        return final_price
    else:
        return price

original_price = float(input(f"Enter original price: "))
discount_percentage = float(input(f"\nEnter the discount percentage: "))

print(f"The final price is: {calculate_discount(original_price, discount_percentage)}")
