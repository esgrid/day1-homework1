name = input("What is my name? ")
my_name = "Esgrid"

while True:
    if name.lower() == my_name.lower():
        print(f"Yep, my name is, {my_name}.")
        break
    else:
        name = input("What's my name again? ")