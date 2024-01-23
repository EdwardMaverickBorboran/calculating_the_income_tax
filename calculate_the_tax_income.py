# Create a program that will --

# Calculate the income tax for the given income by adhering to the rules below

# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

# Expected results: 
# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

# DEADLINE: JANUARY 26, 2024

# pseudocode

# Setting up variable for the given income
given_income = 45000

# Use if else statement to calculate the tax income
if given_income >= 20000:
    need_tax_20 = given_income - 20000
    twenty_tax = need_tax_20*0.2
    total_twenty_tax =  twenty_tax + 1000
    print("0 +","1000.0 +", twenty_tax,"=", total_twenty_tax)

elif given_income >= 10000:
    need_tax_10 = given_income - 10000
    ten_tax = need_tax_10*0.1
    print("0 +",ten_tax,"=", ten_tax)

else:
    given_income < 10000
    print("No need for the tax income.")