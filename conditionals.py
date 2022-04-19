"""
Using comparative operators, you will write a program that makes decisions.
"""
userReply=input("Do you need to ship a package? (Enter yes or no) ")

if userReply=="yes":
     print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")



userReply=input("Quieres stamps,envelope, or make a copy?")

if userReply=="stamps":
    print("we have many stamp designs to choose from.")
elif userReply=="envelope":
    print("We have many envelope sizes to choose from.")
elif userReply=="copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
    