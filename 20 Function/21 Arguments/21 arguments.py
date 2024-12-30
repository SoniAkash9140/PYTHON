#keyword argument->we can change the orf=der
def avg(a=9,b=1): 
    print("The avg is",(a+b)/2)
    
avg(b=4,a=6)

#default argument
def name(fname,mname="John", lname="whatson"):
    print("Hello",fname,mname,lname)
    
name("Amy","Agarwal","Jain")

#required argument->
def name(fname,mname,lname):
    print("Hllo!",fname,mname,lname) 
#name("Peter","Quill")->it will show error bcz the lname is not given here
name("Peter","England","Quill")

#variable length argument
def average(*numbers):
    #print(type(numbers))->tuple
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average is:",sum/len(numbers))
    return sum/len(numbers)

c=average(5,4,22,54,85)
print(c)

def name(**name): #it will create as Dictionary
    print("Hello!",name["fname"],name["mname"],name["lname"])
    
name(mname="Bachan",lname="Barsne",fname="James")


