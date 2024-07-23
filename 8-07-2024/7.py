#Write a program to check if a given string is a valid email address (assume a simple pattern like containing "@" and ".").

email = "tarun226nagwadiya@gmailcom"

# if email.count("@")==1:
#    print("this is valid email address")
# elif email.count(".")==1:
#    print("this is vallid email address")
# else:
#    print("this is not valid email address")        
 
if email.count("@") == 1 and email.count(".") == 1:
    print("this is valid email address")
else:
    print("this is not valid email address")

