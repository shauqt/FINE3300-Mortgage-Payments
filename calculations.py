# Create a function that will calculate the monthly, semi-monthly, bi-weekly, rapid bi-weekly, weekly, and rapid weekly payments
def mortgage_payments(principal, interest, ammortization):

    # Calculate the rates for each period 
    # Note: rapid bi_weekly and rapid weekly do not have rates as their payment calculations are based of monthly payments
    monthly_rate = ((1 + (interest/2)) ** (2/12)) - 1
    semi_monthly_rate = ((1 + (interest/2)) ** (2/24)) - 1
    bi_weekly_rate = ((1 + (interest/2)) ** (2/26)) - 1
    weekly_rate = ((1 + (interest/2)) ** (2/52)) - 1

    # Using the rates, calculate the payments 
    monthly_payment = ((monthly_rate * (1 + monthly_rate) ** (ammortization * 12)) / ((1 + monthly_rate) ** (ammortization * 12) - 1)) * principal
    semi_monthly_payment = ((semi_monthly_rate * (1 + semi_monthly_rate) ** (ammortization * 24)) / ((1 + semi_monthly_rate) ** (ammortization * 24) - 1)) * principal
    bi_weekly_payment = ((bi_weekly_rate * (1 + bi_weekly_rate) ** (ammortization * 26)) / ((1 + bi_weekly_rate) ** (ammortization * 26) - 1)) * principal
    rapid_bi_weekly_payment = monthly_payment / 2 
    weekly_payment = ((weekly_rate * (1 + weekly_rate) ** (ammortization * 52)) / ((1 + weekly_rate) ** (ammortization * 52) - 1)) * principal
    rapid_weekly_payment = monthly_payment / 4
    
    # Return payment values, rounding to two decimal places
    return

def main():


if __name__ == '__main__':
    main()