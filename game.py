first_name=input("Enter your first name ")
last_name=input("Enter your last name ")
print(f"hi {first_name} Your full name is {first_name} {last_name}")
print(f"sometimes your full name is also {last_name} {first_name}")
lfirstname = len(first_name)
llastname = len(last_name)
fchar = first_name[0]
lchar = first_name[-1]
fchar1 = last_name[0]
lchar1 = last_name[-1]
print(f"Your first name has {lfirstname} characters")
print(f"Your last name has {llastname} characters")
print(f"The first character in your first name is {fchar}")
print(f"The last character in your first name is {lchar}")
print(f"The first character in your last name is {fchar1}")
print(f"The last character in your last name is {lchar1}")