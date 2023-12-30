



def interest():
    print('This is a monthly interest calculator\n')
    
    # Takes the input from the User
    principal = float(input('Input the loan amount: '))
    apr = float(input('Input the annual interest rate: '))
    years = int(input('Input the number of years : ')) 
    
    # Dives the annual rate in percentages by double zeros
    monthly_interest_rate = apr / 1200
    
    # Converts the annual input to monthly input
    amount_of_months = years * 12
    
    accumulated_interest =0

    for month in range(1, 13):  # Loop through each month in the first year
        
        # Calculates the monthly payment using the present value of an annuity formula
        monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
        
        # makes an increment for each input
        accumulated_interest+=monthly_payment
        
        # Calculates the amount to pay
        to_pay = accumulated_interest + principal
       
        
        # Prints the monthly increment
        print(f'Month {month}: You are to pay: {round(accumulated_interest, 2)} accumulated debt is: {int(to_pay)}')
        
        # Gives the accumulated interest and total refund on the loan
    print(f'At the end of {years}years, your accumulated interest on {principal} is {round(accumulated_interest)} and your total payment is {round(principal+ accumulated_interest)}')
        
interest()
