print("Welcome to your Personal Budget")
name = input("Whats is your name?")
print("Welcome" " " + name + "!")
print("="*45)
moneyEarned = float(input("Enter how much money you earned monthly:"))
yearlyAmount = moneyEarned * 12
tithingPercent = moneyEarned / 100 * 10
print("Annual Money Earned : ${:.2f}".format(yearlyAmount))
print ("Tithing Monthly Payment :${:.2f}" . format(tithingPercent))
fastOffering = float(input("Enter how much you would like to pay for fast offerings monthly:"))
fastAnnual = fastOffering * 12
print("Annual Fast Offering : ${:.2f}".format(fastAnnual))
print("="*45)
print("ANSWER THE QUESTIONS BELOW ABOUT YOUR PERSONAL BUDGET")
input1 = input("Enter Item 1: ")
monthly1 = float(input("Enter Item 1 Monthly Amount: "))
yearly1 = monthly1 * 12
print("Annual Amounnt Item 1: ${:.2f}".format(yearly1))
print('-'*45)
input2 = input("Enter Item 2: ")
monthly2 = float(input("Enter Item 2 Monthly Amount: "))
yearly2 = monthly2 * 12
print("Annual Amount Item 2: ${:.2f}".format(yearly2))
print('-'*45)
input3 = input("Enter Item 3: ")
monthly3 = float(input("Enter Item 3 Monthly Amount: "))
yearly3 = monthly3 * 12
print("Annual Amount Item 3: ${:.2f}".format(yearly3))
print('-'*45)
input4 = input("Enter Item 4: ")
monthly4 = float(input("Enter Item 4 Monthly Amount: "))
yearly4 = monthly4 * 12
print("Annual Amount Item 4: ${:.2f}".format(yearly4))
print('-'*45)
input5 = input("Enter Item 5: ")
monthly5 = float(input("Enter Item 5 Monthly Amount: "))
yearly5 = monthly5 * 12
print("Annual Amount Item 5: ${:.2f}".format(yearly5))
print('-'*45)
input6 = input("Enter Item 6: ")
monthly6 = float(input("Enter Item 6 Monthly Amount: "))
yearly6 = monthly6 * 12
print("Annual Amount Item 6: ${:.2f}".format(yearly6))
print('-'*45)
input7 = input("Tithings, just Write TITHINGS: ")
tithing = tithingPercent
yearTithing = tithingPercent * 12
print("Tithing Year: ${:.2f}".format(yearTithing))
print('*'*45)
print("PERSONAL BUDGET")
print('='*45)
print ("{:<15}{:<15}{:<15}".format('Income','Month','Year'))
print('-'*45)
print ("{:<15}${:<15}${:<15}".format('       ',moneyEarned,yearlyAmount))
print('='*45)
print ("{:<15}{:<15}{:<15}".format('Expenses','Month','Year'))
print('-'*45)
print ("{:<15}${:<15.2f}${:<15.2f}".format(input1,monthly1,yearly1))
print ("{:<15}${:<15.2f}${:<15.2f}".format(input2,monthly2,yearly2))
print ("{:<15}${:<15.2f}${:<15.2f}".format(input3,monthly3,yearly3))
print ("{:<15}${:<15.2f}${:<15.2f}".format(input4,monthly4,yearly4))
print ("{:<15}${:<15.2f}${:<15.2f}".format(input5,monthly5,yearly5))
print ("{:<15}${:<15.2f}${:<15.2f}".format(input6,monthly6,yearly6))
print ("{:<15}${:<15.2f}${:<15.2f}".format(input7,tithingPercent,yearTithing))
print ('='*45)
print ("{:<15}{:<15}{:<15}".format('TOTAL EXPENSES','Month','Year'))
print ("{:<15}${:<15.2f}${:<15.2f}".format('     ',monthly1+monthly2+monthly3+monthly4+monthly5+monthly6+tithingPercent,yearly1+yearly2+yearly3+yearly4+yearly5+yearly6+yearTithing))
print('='*45)
print ("{:<15}{:<15}{:<15}".format('SAVINGS','Month','Year'))
print ("{:<15}${:<15.2f}${:<15.2f}".format('     ',monthly1-monthly2-monthly3-monthly4-monthly5-monthly6-tithingPercent+moneyEarned,yearly1-yearly2-yearly3-yearly4-yearly5-yearly6-yearTithing+yearlyAmount))





