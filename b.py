f_name=input("Your first name:-->")
s_name=input("Your second name:-->")

def full_name_generator(first_name,second_name):
    full_name = f" {first_name} + {second_name}"
    return full_name

print("Your full name is:", full_name_generator(f_name,s_name))


#string formatting
# print("My-1 name-2 is-3 abc-4 def-5")

phone_num = 9841302345
print(f"Your phone number is {phone_num}")

first =1
second =2
third =3
four =4
fifth =5

print(f"My-{first} name-{second} is-{third} abc-{four} def-{fifth}")




