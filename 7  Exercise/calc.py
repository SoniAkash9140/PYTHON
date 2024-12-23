NUM1=float(input("Enter the first number here:"))
NUM2=float(input("Enter the second number here:"))

print("Enter 1 for addition \n Enter 2 for substraction / enter 3 for multiplication /n enter 4 for division")

Entered_number=int(input("choice a numbr from 1 to 4\n"))

if Entered_number==1:
    print("The sum of",NUM1,"and",NUM2,"is:",NUM1+NUM2)
elif Entered_number==2:
    print("The substraction of",NUM1,"and",NUM2,"is:",NUM1-NUM2)
elif Entered_number==3:
    print("The multiplication of",NUM1,"and",NUM2,"is:",NUM1*NUM2)
elif Entered_number==4 :
    print("The division of",NUM1,"and",NUM2,"is:",NUM1/NUM2)
else:
    print("Choose Appropriate Option")
