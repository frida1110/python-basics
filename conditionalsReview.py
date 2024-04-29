# # Ask the user to input the current weather. This can be simplified to three categories for ease: "sunny", "rainy", or "cold".
# weather = input("What is the current weather? (sunny, rainy, cold): ")
# print(weather)

# # Implement the decision structure to advise on what to wear:
# # If the weather is "sunny", recommend "wear sunglasses and a hat".
# if weather == "sunny":
#     print("Wear sunglasses and a hat")
# # If the weather is "rainy", recommend "carry an umbrella and wear waterproof boots".
# elif weather == "rainy":
#     print("carry an umbrella and wear waterproof boots")
# # If the weather is "cold", recommend "wear a warm coat and gloves".
# elif weather == "cold":
#     print("wear a warm coat and gloves")
# # If the input doesn't match any category, inform the user with a message saying the input was not recognized.
# else:
#     print("Input not recognized")

    #Create a Python script that assigns a grade to a student based on their exam score.
# Ask the user to input a score. Assume the score is out of 100.
# Implement the logic to determine the grade based on the score:
# A score of 90 and above is an "A".
# A score of 80 to 89 is a "B".
# A score of 70 to 79 is a "C".
# A score of 60 to 69 is a "D".
# A score below 60 is an "F".
# Ensure the score entered is within the valid range (0-100). If not, print an error message.

score = int(input("Enter your score: "))
if score >=90:
    print("A")

elif score >=80 and score < 90:
    print("B")

elif score >=70 and score < 80:
    print("C")

elif score >=60 and score < 70:
    print("D")

elif score >=50 and score < 60:
    print("F")