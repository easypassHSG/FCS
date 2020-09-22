#!/usr/bin/env python3


#Please pay attention the module is from: https://github.com/jbmohler/mortgage/blob/master/ since there are several packages that are also called mortgage
#Firstly, I used a different module also called mortgage that calculated the loans in years. However, the term_unit could be changed to months too, BUT then the module misscalculated and I got a wrong result. That's why I use a different module now.
import mortgage


def calculate_payment(i,m,p):
    
    #The exercise specifies that it wants the value rounded to 2 decimal places round(value, numberOfDecimals) and the absolute value (I cannot really imagine when the value would be negative, but let's add abs() still)
    return abs(round(mortgage.Mortgage(interest=i, amount=p, months=m).monthly_payment(),2))
    




interest = 0.05
months = 12
principal = 100000


print("The monthly payment is", calculate_payment(interest, months, principal))
