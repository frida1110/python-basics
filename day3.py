age = int(input("Enter your age: "))
while age <0:
    print("Age can nopt be negative: ")
    age = int(input("Enter your age: "))

print("You are {age} years old. ")


name = input("Enter your name: ")
if name =="":
    print("You did not eneter your name")
else: 
    print(f"Hello {name}")


food = input("Enter a food you like (q tp quit):" ) 
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print("bye")

num = int(input("Enter a # between 1 - 10: "))
while nin <1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10:"))
print(f"Your number is {num}")