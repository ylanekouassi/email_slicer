#EMAIL SLICER

email = input("Enter your email: ")

#index = email.index("@") (positionning) 

username = email[:email.index("@")]
print(username)

domain = email[email.index("@")+1:]
print(domain)
