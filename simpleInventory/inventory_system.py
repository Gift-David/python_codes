# This is a simple inventory system for a retail shop

def display_menu():
    # list to store menu items
    menu_items = ["View inventory", "Add product", "Update product", "Search product", "Remove product", "Exit"]

    # looping through the list
    i =1
    for item in menu_items:
        print(f"{i}. {item}")
        i += 1

inventory = [] # list to store all products


# Recheck that this functions breaks the calling function on true

# validate_nonempty_inventory()
def validate_nonempty_inventory():
    # returns a msg if inventory list is empty
    if not inventory:
        print("Inventory is empty")
    return None


# function to view all products
def view_products():
    # returns a msg if inventory list is empty
    if not inventory:
        print("Inventory is empty")

        return False
    print("---Current Inventory--")
    print(f"{"id":<8} | {"name":<25} | {"quantity":<10} | {"price ($)":<10}")
    print("-" * 60)

    for product in inventory:
        print(f"{product["id"]:<8} | {product["name"]:<25} | {product["quantity"]:<10} | ${product["price"]:<10.2f}")

# function to add a product
def add_product(product_id, product_name, product_quantity, product_price):
    for product in inventory:
        # checks if product_id exist
        if product.get("id").lower() == product_id.lower():
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

# Function to validate product_ID
def validate_id(product_id):
    for product in inventory:
    # checks if product id doesn't exists
        if not product.get("id").lower() == product_id.lower():
            print(f"Error: Product with ID:{product_id} does not exists. Enter an existing ID")
            return True

# Function to update a product quantity
def update_product(product_id, product_quantity):
    validate_id(product_id)
    # validates the product quantity and price is a non negative integer
    if product_quantity < 0:
        print(f"Error: The quantity can't be negative")
        return False
    
    # loops through the inventory list and update the quantity
    for product in inventory:
        if product.get("id").lower() == product_id.lower():
            product["quantity"] = product_quantity
            print(f"Product {product["name"]} quantity has been updated successfully")
            return True

# Function to search for a product
def search_product(product_id):
    validate_id(product_id)
    for product in inventory:
        if product["id"] == product_id:
            print(f"{"id":<8} | {"name":<25} | {"quantity":<10} | {"price ($)":<10}")
            print("-" * 60)
            print(f"{product["id"]:<8} | {product["name"]:<25} | {product["quantity"]:<10} | ${product["price"]:<10.2f}")
            return True

# Function to delete a product 
def remove_product(product_id):
    validate_id(product_id)
    # confirms the deleting
    for product in inventory:
        if product.get("id").lower() == product_id.lower():
            print(f"{product["id"]:<8} | {product["name"]:<25} | {product["quantity"]:<10} | {product["price"]:<10.2f}")
            confirm_msg = input("You're about to delete this product. Confirm (yes/no)").lower().strip()
            if confirm_msg == "no":
                break
            elif confirm_msg == "yes":
                inventory.remove(product)
                print(f"Product removed successfully")
            else:
                print(f"Invalid input.")
                break

    return True
            
def main():
    while True:
        print("Main Menu")
        display_menu()
        choice = int(input(("Enter your choice: ")))

        if choice == 1:
            # call function display all products
            view_products()
            pass
        elif choice == 2:
            # Promt for and call function to add a product
            print("---Add a new product")
            product_id = str(input("Enter the product ID: ")).strip()
            product_name = str(input("Enter the product's name: ")).strip()
            product_quantity = int(input("Enter the quantity in stock: "))
            product_price = float(input("Enter the unit price: "))

            add_product(product_id, product_name, product_quantity, product_price)
            pass
        elif choice == 3:
            # Prompt for and call function to update a product quantity with its id
            if not inventory:
                print("Inventory is empty")
                return True
            product_id = str(input("Enter the product ID: ")).strip()
            product_quantity = int(input("Enter the quantity in stock: "))

            update_product(product_id, product_quantity)

        elif choice == 4:
            # Prompt for id and call function to get the product
            product_id = str(input("Enter the product ID: ")).strip()
            search_product(product_id)
            
        elif choice == 5:
            product_id = str(input("Enter the product ID: ")).strip()
            remove_product(product_id)
            
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()