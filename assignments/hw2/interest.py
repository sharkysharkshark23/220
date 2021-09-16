"""
Name:Thomas Scola
interest.py
Problem: computes the monthly interest charge
Certification of Authenticity: I certify that this is entirely my own work.

"""

def main():
    #input
    annual = eval(input("Enter the annual interest rate: "))  # user inputs annual interest rate
    number_days = eval(input("Enter the number of days in the billing cycle "))
    net_balance = eval(input("Enter the previous (net) balance "))  # enter previous balance
    pay_amount = eval(input("Enter the payment amount "))  # user enters the payment amount
    day_billing = eval(input("Enter the day of the billing cycle "))  # enter daybilling

    #calculations
    days_before_end = number_days - day_billing
    calc_1 = net_balance * number_days
    calc_2 = pay_amount * days_before_end
    calc_3 = calc_1 - calc_2
    calc_4 = calc_3 / number_days
    monthly_interest_rate = annual/12/100
    monthly_interest_charge = monthly_interest_rate * calc_4

    #output
    print(round(monthly_interest_charge, 2))

if __name__ == '__main__':

    main()
