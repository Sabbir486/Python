# Match Case Staments--->Switc-Case statement

x = int(input('Enter your value: '))
print("Your value is: ",x)

match x:
    case 0:
        print("Case is 0")
    case 4:
        print("Case is 4")

    case _ if x != 90: #For default we use underscore(_)
        print(x, " is not 90")

    case _ if x != 80:
        print(x, " is not 80")

    case _:
        print(x)

    