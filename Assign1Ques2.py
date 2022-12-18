'''Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.
Hint:
Taxable income = GrossIncome - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate'''

g = float (input("Please Enter Your Gross Income To nearest Decimal :"))

d= int(input("Number Of Dependents:" )) #checking for right no of dependent 
if (d>=0):
 y = g - 10000 - (3000 
 * d)
 z=float (y)
 if (z>0):#checking for income tax to be positive 
     print(z)

 else:
     print (" Not liable for income tax ")
   
else:
    print("not possible")
