# This is a simple inventory system for a small retail shop

def display_menu():
    # list to store menu items
    menu_items = ["View inventory", "Add product", "Update product", "Search product", "Remove product", "Exit"]

    # looping through the list
    i =1
    for item in menu_items:
        print(f"{i}. {item}")
        i += 1

inventory = [] # list to store all products

def view_products():
    # returns a msg if inventory list is empty
    if not inventory:
        print("Inventory is empty")
        return
    
    print("---Current Inventory--")
    print(f"{"id": < 8} | {"name": < 25} | {"quantity": < 10} | {"price":< 10.2}")
    print("-" * 60)

    for product in inventory:
        print(f"{product["id"]: < 8} | {product["name"]: < 25} | {product["quantity"]: < 10} | {product["price"]:< 10.2f}")


def add_product(product_id, product_name, product_quantity, product_price):
    
    for product in inventory:
        # validates product_id don't exist
        if product["id"].lower == product_id:
            print(f"Error: Product with ID:{product_id} already exists. Enter a unique ID")
            return False
    # validates the product quantity and price is a non negative integer
    if product_quantity < 0:
        print(f"Error: The quantity can't be negative")
        return False
    if product_price < 0:
        print(f"Error: The price can't be negative")
        return False
        
    # initializes a new product
    new_product = {
        "id": product_id,
        "name": product_name,
        "quantity": product_quantity,
        "price": product_price
    }

    # adds new_product to the inventory
    inventory.append(new_product)
    print(f"Product '{product_name}' with ID:{product_id} entered successfully!")
    return True

def update_product(product_id, product_quantity):
    
    for product in inventory:
        # validates product id exists
        if not product["id"].lower == product_id:
            print(f"Error: Product with ID:{product_id} does not exists. Enter an existing ID")
            return False
    # validates the product quantity and price is a non negative integer
    if product_quantity < 0:
        print(f"Error: The quantity can't be negative")
        return False
    
        




def main():
    while True:
        display_menu()
        choice = input(int("Enter your choice: "))

        if choice == 1:
            # call function display all products
            pass
        elif choice == 2:
            # Promt for and call function to add a product
            pass
        elif choice == 3:
            # Prompt for and call function to update a product quantity with its id
            pass
        elif choice == 4:
            # Prompt for id and call function to get the product
            pass
        elif choice == 5:
            # Prompt for and call function to remove a product
            pass
        elif choice == 6:
            print("Good bye!")
            break
        else:
            print("Invalid choice. Please try again.")
