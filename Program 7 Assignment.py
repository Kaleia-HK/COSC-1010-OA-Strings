# Alphabetic Telephone Number Translator
# ...
# Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
# The application should display the telephone number, with any alphabetic characters that appeared in the original
# translated to their numeric equivalent.
# For example, if the user enters 555-GET-FOOD, the application should display 555-438-3663.


# import the re module to get characters A-Z in the string
import re

# Display the prompt
print("Please enter in a number in the format: XXX-XXX-XXXX")

# Assign the letters to the numbers / Get user input
number_assign = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5, 'M': 6,
             'N': 6, 'O': 6, 'P': 7, 'Q': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9, 'Z': 9}
get_number = (input("Please the phone number: ").upper())

# Interpret the letter to the corresponding number
charmask = re.compile(r'[A-Z]')
output = []
for letter in get_number:
    if charmask.match(letter):
        output.append(str(number_assign.get(letter)))
    else:
        output.append(str(letter))

# Display the result
print(f"The number entered is {''.join(output)}")

