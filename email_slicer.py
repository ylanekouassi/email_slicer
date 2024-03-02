#EMAIL SLICER

email = input("Enter your email: ")

username = email[ :email.index("@")] #index = email.index("@") (positionning) 

domain = email[email.index("@")+1 : -4] # +1 is excluding the "@"/ -4 is excluding ".com"

print(f"Your username is {username} and the domain is {domain}")
