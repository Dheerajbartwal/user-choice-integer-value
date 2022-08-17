def user_choice():
    choice ='wrong'
    while choice.isdigit()==False:
        choice = input("choose a number  : ")
        if choice.isdigit()==False:
            print("sorry but you did not enter an integer please try again.")
    return int(choice)

user_choice()