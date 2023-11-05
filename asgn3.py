# Initialize the item list with names and prices
items = [["tomato", 50000], ["onion", 75000], ["cucumber", 30000], ["orange", 45000], ["banana", 60000]]
import time
# Initialize variables for the order and coupons
order = {}
total_bill = 0
coupons = 0


# Function to add an item to the order
def add_item():
    global total_bill
    item_name = input("Enter the name of the item you want to add: ").lower()
    for item in items:
        if item_name == item[0].lower():
            quantity = int(input(f"Enter the quantity of {item[0]}: "))
            order[item[0]] = order.get(item[0], 0) + quantity
            total_bill += item[1] * quantity
            print(f"{quantity} {item[0]} added to your order.")
            return
    print("Item not found!")


# Function to check the total bill
def check_total():
    print(f"The total of your bill is: {total_bill} LBP")


# Function to add a coupon
def add_coupon():
    global coupons
    coupon_value = int(input("Enter the value of the coupon: "))
    coupons += coupon_value
    print(f"{coupon_value} LBP coupon added to your account.")


# Function to checkout
def checkout():
    print("Items bought and their quantities:")
    for item, quantity in order.items():
        print(f"{item}: {quantity}")
    print(f"Total of the order (without coupons): {total_bill} LBP")
    print(f"Total of coupons: {coupons} LBP")
    total_to_pay = total_bill - coupons
    print(f"Total to pay: {total_to_pay} LBP")
    return total_to_pay


# Main program
while True:
    print("1. Start a new order")
    print("2. Close the program")

    option = input("Enter your choice: ")
    if option == "2":
        print("Bye bye!")
        time. sleep(5)
        break

    elif option == "1":
        while True:

            print("\nTOMATO 50000 LBP, ONION 75000 LBP, CUCUMBER 30000 LBP, ORANGE 45000 LBP, BANANA 60000 LBP ")
            print("1. Add a new item")
            print("2. Check the total of the bill")
            print("3. Add a coupon")
            print("4. Checkout")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_item()

            elif choice == "2":
                check_total()

            elif choice == "3":
                add_coupon()

            elif choice == "4":
                total_to_pay = checkout()
                break

            else:
                print("Invalid choice. Please select a valid option.")

    else:
        print("Invalid choice. Please select a valid option.")
