def count_alphabets_digits(input_string):
    alphabets = 0
    digits = 0
    
    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
    
    return alphabets, digits

# Get input from user
input_string = input("Enter a string: ")
alphabets, digits = count_alphabets_digits(input_string)

print("Number of alphabets:", alphabets)
print("Number of digits:", digits)
