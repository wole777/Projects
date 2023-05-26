# Investment and Home Loan Repayment Calculators

import math

# Set the calculator categories
calculator_category_1 = "investment"
calculator_category_2 = "bond"

# Get the user's name
user_name = input("Please enter your first name: ")

# Display an introduction to the user
# I got help with multi-line f-strings here: https://realpython.com/python-f-strings/
print(f"Hi {user_name.capitalize()}. Welcome to the Investment and Home Loan Repayment Calculators. \n \n"
                                f"You can choose between the following calculators: \n" 
                                f"Investment - to calculate the amount of interest you'll earn on your investment. \n"
                                f"Bond - to calculate the amount you'll have to pay on a home loan. \n")

# Get the user's choice of calculator
while True:
    calculator_category = input("Enter 'investment' or 'bond' to proceed: ")

    # Validate the user's choice of calculator
    if calculator_category.lower() == calculator_category_1 or calculator_category.lower() == calculator_category_2:
        break
    else:
        print("\nSorry. You must enter 'investment' or 'bond' to proceed (without quote marks or other characters). Please try again.")

# Calculate the amount of interest the user will earn if they select investment
if calculator_category.lower() == calculator_category_1:
    # Get the user's deposit amount
    while True:
        try:
            investment_amount = float(input("Please enter the amount you wish to invest: "))
            break
        except ValueError:
            print("\nSorry. You must enter whole or decimal numbers only. Please try again.")

    # Get the user's interest rate
    while True:
        try:
            interest_rate = float(input("Please enter the interest rate (as a percentage number): "))
            break
        except ValueError:
            print("\nSorry. You must enter whole or decimal numbers only (without the percentage symbol). Please try again.")

    # Get the user's investment period in years
    while True:
        try:
            investment_period = int(input("Please enter the number of years you plan to invest: "))
            break
        except ValueError:
            print("\nSorry. You must enter a whole number only. Please try again.")

    # Get the user's interest type
    while True:
        interest = input("Please enter the type of interest you wish to earn (simple or compound): ")

        # Validate the user's interest type
        if interest.lower() == "simple" or interest.lower() == "compound":
            break
        else:
            print("\nSorry. You must enter 'simple' or 'compound' to proceed (without quote marks or other characters). Please try again.")

    # Calculate the amount of interest the user will earn
    if interest.lower() == "simple":
        interest_amount = investment_amount * (1 + (interest_rate / 100) * investment_period)
    elif interest.lower() == "compound":
        interest_amount = investment_amount * pow((1 + (interest_rate / 100)), investment_period)
    else:
        print("Sorry. There was an error. Please try again.")

    # Display the amount of interest the user will earn
    print(f"\nHi {user_name.capitalize()}. Based on the information you provided, you will earn £{interest_amount:.2f} in interest over {investment_period} years at an interest rate of {interest_rate}%.")

# Calculate the amount the user will have to pay on a home loan if they select bond
elif calculator_category.lower() == calculator_category_2:
    # Get the user's home value
    while True:
        try:
            home_value = float(input("Please enter the value of the home you wish to purchase: "))
            break
        except ValueError:
            print("\nSorry. You must enter whole or decimal numbers only. Please try again.")

    # Get the user's interest rate
    while True:
        try:
            interest_rate = float(input("Please enter the interest rate (as a percentage number): "))
            break
        except ValueError:
            print("\nSorry. You must enter whole or decimal numbers only (without the percentage symbol). Please try again.")

    # Get the user's repayment period in months
    while True:
        try:
            repayment_period = int(input("Please enter the number of months you plan to repay the loan over: "))
            break
        except ValueError:
            print("\nSorry. You must enter a whole number only. Please try again.")

    # Calculate the amount the user will have to pay on a home loan
    repayment = (((interest_rate / 100) / 12) * home_value) / (1 - pow((1 + ((interest_rate / 100) / 12)), -repayment_period))

    # Display the amount the user will have to pay on a home loan
    print(f"\nHi {user_name.capitalize()}. Based on the information you provided, you will have to pay £{repayment:.2f} per month over {repayment_period} months at an interest rate of {interest_rate}%.")

# Display an error message if the user's choice of calculator is invalid
else:
    print("Sorry. There was an error. Please try again.")
