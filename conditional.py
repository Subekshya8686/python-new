# conditional statement in python 

name= input("What's your name please? ")
age = int(input("What's your age please? "))

if age < 0:
    print(f"Ivalid Age")
if age==10:
    print(f"Dear {name}, Your ticket price is: 100")
elif age>10:
    print(f"Dear {name}, Your ticket prive is: 150")
else:
    print(f"Dear {name}, Your ticket price is: 50")


def calc_weight(m,g=10):
    print(f"Your weight is:{m*g}N ")

mass = int(input("Please enter your mass:"))
print(calc_weight(mass))

#Today's quiestion :
#1 Ask a two integer number with user and function should return their addition
#2 Ask an information of your laptop and a fuction should return like this:
"""

Brand_Name Model_Name Available_at_price

Ex: Dell vostro @ 80000

"""

#1 
def add(num1,num2):
    sum = num1 + num2
    return(sum)

FNum = int(input("enter first number: "))
SNum = int(input("Enter second number: "))
sum = add(FNum, SNum)
print(f"Sum is {sum}")

#2
Brand_Name = input("Enter brand name: ")
Model_Name = input("Enter model name: ")
Price = int(input("Enter price: "))

def laptop_specs(Brand, Model, Price):
    print(f"The laptop is {Brand}, {Model} @ Rs.{Price}")
    
mylaptop = laptop_specs(Brand_Name, Model_Name, Price)
print(mylaptop)

#Working model of atm machine

total_price = 0
card_type = "visa"
is_same_bank = True
is_expired=False

print("Please insert your atm card: ")
required_amt = int(input("Please enter a amount: "))

def read_card():
    print("Fetching Card Details from Bank .... ")
    card_details = [1258,False,False]
    total_price = card_details[0]
    is_same_bank=card_details[1]
    is_expired= card_details[2]
    if is_expired:
        print("Sorry, this card cannot be accepted here: ")
    else:
        perform_transactions(total_price, is_same_bank)


def perform_transactions(total_amt, is_same_bank):
    charge = 0
    if not is_same_bank:
        charge = 5
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")
    else:
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")


print("Please insert your atm card:")
input()
print("Card inserted!!")
required_amt = int(input("Please enter a amount:"))
read_card()


