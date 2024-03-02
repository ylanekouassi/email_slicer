#EMAIL SLICER

email = input("Enter your email: ")

#index = email.index("@") positionning 

username = email[:email.index("@")]
print(username)

