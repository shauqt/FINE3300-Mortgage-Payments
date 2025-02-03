# Create a function that will calculate the monthly, semi-monthly, bi-weekly, rapid bi-weekly, weekly, and rapid weekly payments
def mortgage_payments(principal, rate, amortization):

    # Calculate the rates for each period 
    # Note: rapid bi_weekly and rapid weekly do not have rates as their payment calculations are based of monthly payments
    monthly_rate = ((1 + (rate/2)) ** (2/12)) - 1
    semi_monthly_rate = ((1 + (rate/2)) ** (2/24)) - 1
    bi_weekly_rate = ((1 + (rate/2)) ** (2/26)) - 1
    weekly_rate = ((1 + (rate/2)) ** (2/52)) - 1

    # Using the rates, calculate the payments 
    monthly_payment = ((monthly_rate * (1 + monthly_rate) ** (amortization * 12)) / ((1 + monthly_rate) ** (amortization * 12) - 1)) * principal
    semi_monthly_payment = ((semi_monthly_rate * (1 + semi_monthly_rate) ** (amortization * 24)) / ((1 + semi_monthly_rate) ** (amortization * 24) - 1)) * principal
    bi_weekly_payment = ((bi_weekly_rate * (1 + bi_weekly_rate) ** (amortization * 26)) / ((1 + bi_weekly_rate) ** (amortization * 26) - 1)) * principal
    rapid_bi_weekly_payment = monthly_payment / 2 
    weekly_payment = ((weekly_rate * (1 + weekly_rate) ** (amortization * 52)) / ((1 + weekly_rate) ** (amortization * 52) - 1)) * principal
    rapid_weekly_payment = monthly_payment / 4
    
    # Return payment values, rounding to two decimal places
    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2), 
        round(bi_weekly_payment, 2), 
        round(rapid_bi_weekly_payment, 2), 
        round(weekly_payment, 2), 
        round(rapid_weekly_payment, 2)
    )

# Create the main function that will run to take in user input values and output the calculated payments
def main():

    # Store user inputs for principal, interest, and ammortization as variables
    principal_input = float(input("Please provide the principal amount: "))
    interest_input = float(input("Please provide the interest rate: ")) / 100
    amortization_input = int(input("Please provide the ammorization period in years: "))

    # Call the mortgage payments function and store the values into the variables
    monthly_payment, semi_monthly_payment, bi_weekly_payment, rapid_bi_weekly_payment, weekly_payment, rapid_weekly_payment = mortgage_payments(principal_input, interest_input, amortization_input)

    # Print out the calculated values
    print(f"Your Monthly Payment Is: ${monthly_payment}")
    print(f"Your Semi-Monthly Payment Is: ${semi_monthly_payment}")
    print(f"Your Bi-Weekly Payment Is: ${bi_weekly_payment}")
    print(f"Your Rapid Bi-Weekly Payment Is: ${rapid_bi_weekly_payment}")
    print(f"Your Weekly Payment Is: ${weekly_payment}")
    print(f"Your Rapid Weekly Payment Is: ${rapid_weekly_payment}")

# Run the code if the script is executed directly and not when it is imported to another module
if __name__ == "__main__":
    main()