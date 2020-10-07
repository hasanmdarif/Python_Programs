email = 0
check = 0

while check == 0:
    email = input("\nPlease Enter Your Email Address: ")
    if "@" in email and "." in email:
        print("\nEmail Accepted")
        check = 1
    else:
        print("\nThat Is Not A Valid Email, Please Try Again")
    while check == 1:
        email2 = input("\nPlease Enter Your Email Address For A Second Time: ")
        if email == email2:
            print("\nEmail Address Is Verified and Accepted")
        else:
            print("\nSorry Email Is Invalid")
            check = 0
