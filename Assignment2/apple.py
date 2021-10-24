#This the start of the program 

money_str= int(input("How much money you have here:")) #please enter the amount of money you have
money= money_str
nyapol_str= int(input("What is the price of the apple: ")) #The price of the apple you will buy
nyapol= nyapol_str
maxNumber_str= money//nyapol
maxNumber= maxNumber_str
amount_str= nyapol*maxNumber #this will identify how much will you pay depending on the indicated money you have
amount=amount_str
change_str= money-amount
change=change_str
print(f'You can buy {maxNumber} apples and your change is {change} pesos.')



