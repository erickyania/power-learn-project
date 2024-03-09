# def calculate_discount(price, discount_percent):
#   """
#   This function calculates the final price after applying a discount.

#   Args:
#       price: The original price of the item.
#       discount_percent: The discount percentage (0 to 100).

#   Returns:
#       The final price after applying the discount (if applicable).
#   """

#   if discount_percent >= 20:
#     discount = price * discount_percent / 100
#     final_price = price - discount
#   else:
#     final_price = price

#   return final_price

def calculate_discount(price, discount_percent):
  """
  This function calculates the final price after applying a discount.

  Args:
      price: The original price of the item.
      discount_percent: The discount percentage (0 to 100).

  Returns:
      The final price after applying the discount (if applicable).
  """

  if discount_percent >= 20:
    discount = price * discount_percent / 100
    final_price = price - discount
  else:
    final_price = price

  return final_price

# Get user input for price and discount
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Print the result with appropriate message
if discount_percent >= 20:
  print(f"Final price after applying {discount_percent}% discount: ${final_price:.2f}")
else:
  print(f"No discount applied. Original price: ${original_price:.2f}")
