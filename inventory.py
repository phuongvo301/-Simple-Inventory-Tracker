print("Inventory Tracker")
print("Second change for Sprint 2")
# Simple Inventory Tracker
# Developer: Phuong Vo

inventory = {}  # store items as {name: {"qty": x, "price": y}}

def add_item():
    name = input("Item name: ").strip()
    if name in inventory:
        print("Item already exists. Try updating it instead.\n")
        return
    try:
        qty = int(input("Quantity: "))
        price = float(input("Price per unit: "))
    except ValueError:
        print("Please enter numbers for quantity and price.\n")
        return
    inventory[name] = {"qty": qty, "price": price}
    print(f"Added {name} to inventory.\n")

def update_item():
    name = input("Item name to update: ").strip()
    if name not in inventory:
        print("Item not found.\n")
        return
    try:
        qty = int(input("New quantity: "))
        price = float(input("New price per unit: "))
    except ValueError:
        print("Please enter numbers for quantity and price.\n")
        return
    inventory[name]["qty"] = qty
    inventory[name]["price"] = price
    print(f"Updated {name}.\n")

def delete_item():
    name = input("Item name to delete: ").strip()
    if name in inventory:
        del inventory[name]
        print(f"Deleted {name}.\n")
    else:
        print("Item not found.\n")

def view_inventory():
    if not inventory:
        print("Inventory is empty.\n")
        return
    print("\nCurrent Inventory:")
    print("------------------")
    total_value = 0
    for name, data in inventory.items():
        line_value = data["qty"] * data["price"]
        total_value += line_value
        print(f"{name}: {data['qty']} units at ${data['price']:.2f} each "
              f"(value ${line_value:.2f})")
    print(f"Total inventory value: ${total_value:.2f}\n")

def search_item():
    name = input("Item name to search: ").strip()
    data = inventory.get(name)
    if data:
        print(f"{name}: {data['qty']} units at ${data['price']:.2f} each.\n")
    else:
        print("Item not found.\n")

def restock_alert():
    try:
        threshold = int(input("Show items with quantity less than or equal to: "))
    except ValueError:
        print("Please enter a number.\n")
        return
    low_items = {n: d for n, d in inventory.items() if d["qty"] <= threshold}
    if not low_items:
        print("No items at or below that level.\n")
        return
    print("\nLow Stock Items:")
    print("----------------")
    for name, data in low_items.items():
        print(f"{name}: {data['qty']} units left")
    print()

def show_menu():
    print("=== Simple Inventory Tracker ===")
    print("1. Add item")
    print("2. Update item")
    print("3. Delete item")
    print("4. View all items")
    print("5. Search for an item")
    print("6. Restock alert")
    print("Q. Quit")
    print("-------------------------------")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip().lower()
        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            search_item()
        elif choice == "6":
            restock_alert()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
