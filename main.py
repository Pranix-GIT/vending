from operations import display_laptops, purchase_laptop, sell_laptop

while True:
    print("+------------------------------------------------------+")
    print("\t=== Hamro Laptops Inventory Management System ===")
    print("+------------------------------------------------------+")
    print("1. Display Available Laptops")
    print("2. Purchase a Laptop")
    print("3. Sell a Laptop")
    print("4. Exit")

    print("+------------------------------------------------------+")
    choice = input("\nEnter your choice (1-4): ")

    if choice == '1':
        display_laptops()

    elif choice == '2':
        purchase_laptop()

    elif choice == '3':
        sell_laptop()

    elif choice == '4':
        print("Thank you for using Laptops Inventory Management System")
        break

    else:
        print("Invalid choice! Please try again.")
