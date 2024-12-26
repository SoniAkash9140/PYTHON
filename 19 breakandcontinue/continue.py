# Take input from user for the range limit
a = int(input("Enter the number for the table: "))

# Iterate from 2 to the number a
for num in range(2, a + 1):
    print(f"Multiplication table for {num}:")
    
    # Generate the table for the current number
    for i in range(10):  # 10 times multiplication (1 to 10)
        # if i == 3:  # Skip when multiplier is 4 (i.e., i == 3)
        #     continue
        print(f"{num} X {i + 1} = {num * (i + 1)}")
    print()  # To add a blank line between tables
