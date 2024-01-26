def calculate_price(is_tuesday: bool, num_pizzas: int, is_delivery: bool, is_ordered_via_app: bool) -> float:
    """
    Calculate the total price for a pizza order based on various factors.

    Parameters:
    - is_tuesday (bool): True if it's Tuesday, False otherwise.
    - num_pizzas (int): The number of pizzas in the order.
    - is_delivery (bool): True if delivery is required, False otherwise.
    - is_ordered_via_app (bool): True if the customer used the app to order, False otherwise.

    Returns:
    float: The total price for the pizza order.
    """
    # Define the base price for each pizza
    pizza_price = 12
    # Calculate the delivery cost based on conditions
    delivery_cost = 2.5 if num_pizzas < 5 and is_delivery else 0
    # Calculate the total price for the pizzas without considering discounts
    total_pizza_price = num_pizzas * pizza_price
    # Apply a 50% discount on total_pizza_price if it's Tuesday
    if is_tuesday:
        total_pizza_price *= 0.5
    # Apply a 50% discount on total_pizza_price if it's Tuesday
    if is_ordered_via_app:
        total_pizza_price *= 0.75
    # Calculate the final total price by adding pizza cost and delivery cost
    total_price = total_pizza_price + delivery_cost
    return total_price
# Display welcome message
print(f"\n{'BPP Pizza Price Calculator':}\n{'='*26}\n")

# Get the number of pizzas from the user, ensuring it's a positive integer
num_pizzas = -1
while num_pizzas <= 0:
    try:
        num_pizzas = int(input("How many pizzas would you like to order? "))
        if num_pizzas < 0:
            print("Please enter a positive integer!")
    except ValueError:
            print("Please enter a number!")

# Get information about Tuesday, delivery, and app usage from the user
while True:
    is_tuesday = input("Is it Tuesday? ")
    if is_tuesday.lower() == "y":
        break
    elif is_tuesday.lower() == "n":
                break
    else:
        print('Please answer "y" or "n".')
                
                
while True:
    is_delivery = input("Is delivery required? ")
    if is_delivery.lower() == "y":
        break
    elif is_delivery.lower() == "n":
        break
    else:
        print('Please answer "y" or "n".')
                
                
while True:
    is_ordered_via_app = input("Did the customer use the app? ")
    if is_ordered_via_app.lower() == "y":
        break
    elif is_ordered_via_app.lower() == "n":
        break
    else:
        print('Please answer "y" or "n".')

# Calculate and display the total price
total_price = calculate_price(is_tuesday.lower() == "y", num_pizzas, is_delivery.lower() == "y", is_ordered_via_app.lower() == "y")
print(f"\n{f'Total Price: £{total_price:.2f}':}")
