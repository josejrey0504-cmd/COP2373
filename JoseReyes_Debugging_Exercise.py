def calculate_discount(price, discount_rate):

    # No changes were needed here because the formula for calculating
    # the discount amount was already working correctly.
    discount_amount = price * discount_rate
    return discount_amount


def apply_discount(price, discount_amount):

    # No changes were needed here because the final price calculation
    # was already producing the correct result.
    new_price = price - discount_amount
    return new_price


def main():

    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    # The original program crashed while processing the Tablet product.
    # This loop was not the problem, but it is where the bad value was found
    # during debugging.
    for product in products:

        price = product["price"]
        discount_rate = product["discount_rate"]

        # The error occurred because the Tablet price was stored as a string.
        # This fix converts a numeric string into a number before the
        # discount calculation is performed.
        if isinstance(price, str):
            try:
                price = float(price)

            # This error message was added so the program explains the issue
            # instead of crashing if the conversion fails.
            except ValueError:
                print(f"Error: {product['name']} has an invalid price.")
                print()
                continue

        # This validation was added after debugging to prevent future crashes
        # caused by non-numeric price values.
        if not isinstance(price, (int, float)):
            print(f"Error: {product['name']} has an invalid price.")
            print()
            continue

        # This validation was added because the discount calculation requires
        # a numeric discount rate and would fail with invalid data.
        if not isinstance(discount_rate, (int, float)):
            print(f"Error: {product['name']} has an invalid discount rate.")
            print()
            continue

        # After fixing the data issue, the original discount calculation can
        # safely run without causing the TypeError.
        discount_amount = calculate_discount(price, discount_rate)

        # This line was not causing the error, but it depends on the
        # discount calculation being successful.
        final_price = apply_discount(price, discount_amount)

        print(f"Product: {product['name']}")
        print(f"Original Price: ${price}")
        print(f"Discount Amount: ${discount_amount}")
        print(f"Final Price: ${final_price}")
        print()


if __name__ == "__main__":
    main()