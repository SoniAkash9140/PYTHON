# slicing (name[0:n-1])

name="Akash Soni"
print(len(name))

print(name[1:4])
#it will print from index 0 to n-1

#negative slicing
fruit="mango"
print(fruit[-3:-1])
#it will print from end of string with -1 (5-3=2 , 5-1=4 so it will print from index 2 to 4)

nm="Harry"
print(len(nm))
print(nm[len(nm)-4:len(nm)-2])