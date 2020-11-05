class Login:
    case = None
    print("Press 0 to Login")
    print("Press 1 to Create Account")
    try:
        case = int(input("Enter Your Choice ==> "))
        if case == 0:
            print("=============LOGIN===============")
            userName = str(input("Enter Your Name : "))
            password = input("Enter Your Password : ")
            try:
                flag = None
                file = open("Credintials.txt", "r")
                read = file.read()
                read = read.splitlines()
                for i in read:
                    spl = i.split()
                    if userName == spl[0] and password == spl[1]:
                        flag = "found"
                if flag == "found":
                    print("Login Successful!")
                else:
                    print("Login Failed!")
            except IOError:
                print("Oops! Something went wrong.")
            finally:
                file.close()
        elif case == 1:
            print("============CREATE ACCOUNT================")
            name = str(input("Enter Your Name : "))
            pasw = input("Enter Password : ").lower()
            again = input("Enter Password Again : ").lower()
            if pasw != again:
                print("Sorry! You can't create account, Try Again later.")
                exit()
            else:
                try:
                    file = open("Credintials.txt", "a+")
                    file.write(name + " " + pasw + "\n")
                except IOError:
                    print("Oops! Something went wrong.")
                finally:
                    file.close()
        else:
            print("Invalid Command!")
    except ValueError:
        print("Oops! You enter invalid input, kindly correct it.")



