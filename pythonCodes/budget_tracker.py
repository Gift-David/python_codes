# A script to store and summarize budget details

budget_category = str(input("Input the budget category: " )).title()
monthly_budget = float(input("Input the monthly budget: "))
amount_spent = float(input(f"Input the amount spent on {budget_category.lower()}: "))
transaction_number = int(input("Input the number of transactions: "))

remaining_budget = (monthly_budget - amount_spent)

print(f"Category: {budget_category} \nBudget: ${monthly_budget} \nSpent: ${amount_spent} \nRemaining: ${remaining_budget} \nTransactions: {transaction_number}")