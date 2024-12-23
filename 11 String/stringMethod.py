a="Harry"
print(len(a))
#upper() 
print(a.upper())

#lower()
print(a.lower())

#rstrip(): remove any post training character. E-
str="Hello !!!"
print(str.rstrip("!"))

#replace():
str2="Silver Spoon"
print(str2.replace("Sp","M"))

#split() it will convert your string into LIST if there space exists in your string.
print(str2.split(" "))

#capitalize() : it will convert your first character of ur string into Capital Letter.
str3="heLLo"
#it will convert uppercase to lowercase 
print(str3.capitalize())

# center() : align the string to the center as per parameter given by the user 
print(str2.center(50))

#count : it will tell us that how many any value is used in our string
str4="Akash Vikash Vishal "
print(str4.count("a"))

#endswith(): it will tell us that the string is end or not as per parameter given by user
print(str4.endswith("al "))

#we can even search any value is present in our string or not .
str5="Welcome to the Console"
print(str5.endswith("to",4,10))

#find: search fo the first occurance of the given value and return the index where it present. 
print(str5.find("come"))

# index method : similar to find( ) method but it raise error if it not find the value the user given.
print(str5.index("to"))

# isalnum(): this method return TRUE only when the entire string consist only 0-9 or A-Z , a-z.
str6="WelcomeToTheConsole"
print(str6.isalnum())

# isalpha(): TRUE only when entire string consists only A-Z or a-z.
print(str6.isalpha())

# islower():
print(str6.islower())

# isprintable(): 
print(str6.isprintable())

#isspace():
print(str6.isspace())

#istitle(): return TRUE only if first letter of each word of the string Caputalized.
print(str6.istitle())

# startwith():
# isupper():

# swapcase(): Uppercase->Lower case . Lower case-> Upper case .
print(str6.swapcase())

# title(): convert string values into TITLE
print(str6.title())


