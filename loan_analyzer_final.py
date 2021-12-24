from pathlib import Path


loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
total_number_of_loans = len(loan_costs)
print("The total number of loans is", total_number_of_loans)



# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
total_value_of_loans = sum(loan_costs)
print("The total value is:",  total_value_of_loans)


# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
average_loan_amount = sum(loan_costs) / len(loan_costs)
print("The average loan amount is:",  average_loan_amount)




# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
remaining_months = loan.get('remaining_months')
future_value = loan.get('future_value')
print("The remaining months are", remaining_months)
print("The future value is", future_value)

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
 
fair_value = future_value / (1 + 0.20/12) ** remaining_months
print("The fair value is", fair_value)

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
present_value = fair_value
if present_value>= 800:
    print("Buy, the loan is worth at least the cost!")
else:
    print("Do not buy! loan is too expensive!")




# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def calculate_present_value(future_value , remaining_months , annual_discount_rate):
    present_value = fair_value = future_value / (1 + 0.20/12) ** remaining_months
    return present_value


# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
annual_discount_rate = 0.20
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)
print(f"The present value of the loan is: {present_value}")


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans= []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

print(inexpensive_loans)



import csv
from pathlib import Path

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
csvpath = Path("inexpensive_loans.csv")
output_path = Path("inexpensive_loans.csv")


with open(csvpath, "w") as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=",")

    csvwriter.writerow(header)

for loan in inexpensive_loans:
    csvwriter.writerow(loan.values())

print(loan.values())
