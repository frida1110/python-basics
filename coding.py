name = input("What is your name: ")
act = input("What act will you be performing: ")
time = int(input("What time after five pm"))

if time == 5:
    print("Your appointment is at 5:00-5:15")

elif time == 515:
    print("Your appointment is at 5:15 - 5:30")

elif time == 530:
    print("Your appoinment is at 5:30 - 5:45")

vote = int(input("Vote for the performer"))

print(name)
print(act)
print(time)
print("Your score is " + str(vote))

