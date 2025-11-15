# Palindrome Checker Program

# Step 1: Take input from the user
text = input("Enter a word or number: ")

# Step 2: Clean the input (optional)
text = text.lower()  # make it lowercase so 'Madam' also works

# Step 3: Reverse the string
reversed_text = text[::-1]

# Step 4: Compare original and reversed versions
if text == reversed_text:
    print(f" '{text}' is a palindrome.")
else:
    print(f" '{text}' is NOT a palindrome.")
