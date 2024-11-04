# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

# def print_greeting():
#     # Your code goes here. Remember to indent!
#     python_is_fun = True
#     if python_is_fun:
#         print("Python is fun!")

# # Call the function
# print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

# def check_letter():
#     letter = input('type 1 letter: ').lower()
#     if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#         print(f'The letter {letter} is a vowel')
#     else: 
#         print(f'The letter {letter} is a consonant')

# # Call the function
# check_letter()

print('Exercise 1 is done. Commented out above.')


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

# def check_voting_eligibility():
#     age = int(input('Please enter your age: '))
#     if age < 1:
#         print('invalid age try again.')
#         check_voting_eligibility()
#     if age < 18:
#         print("You are not able to vote yet")
#     else: print('Congrats, you can vote')

# # Call the function
# check_voting_eligibility()

print('Exercise 2 is done. Commented out above.')

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

# def calculate_dog_years():
#     age = int(input("Enter your dog's age: "))
#     if age < 1:
#         print('invalid entry. Try again')
#         calculate_dog_years()
#     if age < 3 and age > 0:
#         human_age = 10 * age
#         print(f'The dog in human age is {human_age} years old.')
#     else:
#         human_age = 20 + ((age - 2) * 7)
#         print(f'The dog in human age is {human_age} years old.')

#     # Your control flow logic goes here

# # Call the function
# calculate_dog_years()

print('Exercise 3 is done. Commented out above.')