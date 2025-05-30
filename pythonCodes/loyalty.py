# A script that uses variables to store and display a customer's loyalty details

name = str(input("Customer's name: ")).title()
id = str(input("Customer's ID: "))
visits = int(input("Number of visits: "))
total_spent = float(input("Total amount spent: "))

loyalty_points = (total_spent / 5)

print(f"Customer: {name} \nID: {id} \nVisits: {visits} \nTotal spent: ${total_spent} \nLoyalty points: {loyalty_points}pnts")

