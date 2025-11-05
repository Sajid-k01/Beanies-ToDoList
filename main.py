def main_menu():
    
    """ displays main menu"""

    print("\n*/// Menu ///*\n")
    print("1) View To-do's")
    print("2) Add To-do's")
    print("3) Remove To-do's")
    print("4) Edit To-do's") 
    print("\n")
    

    user_input = input("Select an Option: ")
    if user_input == "1":
        view_menu()
    elif user_input == "2":
        add_menu()
    elif user_input == "3":
        remove_menu()
    elif user_input == "4":
        edit_menu()
    else:
        print("Choose from the Option List!!!")

def view_menu():

    print("\n")
    print("1) View Monday")
    print("2) View Tuesday")
    print("3) View Wednesday")
    print("4) View Thursday")
    print("5) View Friday")
    print("6) View Saturday")
    print("7) View Sunday")
    print("8) Go Back")
    print("\n")

    user_view = input("Select a day: ")
    if user_view == "1":
        """idk"""
    elif user_view == "2":
        """idk"""
    elif user_view == "3":
        """idk"""
    elif user_view == "4":
        """idk"""
    elif user_view == "5":
        """idk"""
    elif user_view == "6":
        """idk"""
    elif user_view == "7":
        """idk"""
    elif user_view == "8":
         main_menu()
    else:
        print("Choose from the option list!!!")

def add_menu():
    print("\n")
    print("1) Add To Monday")
    print("2) Add To Tuesday")
    print("3) Add To Wednesday")
    print("4) Add To Thursday")
    print("5) Add To Friday")
    print("6) Add To Saturday")
    print("7) Add To Sunday")
    print("8) Go Back")
    print("\n")
    
    user_add = input("Select a day: ")
    if user_add == "1":
        """idk"""
    elif user_add == "2":
        """idk"""

    elif user_add == "3":
        """idk"""
    elif user_add == "4":
        """idk"""
    
    elif user_add == "5":
        """idk"""

    elif user_add == "6":
        """idk"""

    elif user_add == "7":
        """idk"""

    elif user_add == "8":
         main_menu()
    else:
        print("Choose from the option list!!!")
        


def remove_menu():
    print("\n")
    print("1) Remove from Monday")
    print("2) Remove from Tuesday")
    print("3) Remove from Wednesday")
    print("4) Remove from Thursday")
    print("5) Remove from Friday")
    print("6) Remove from Saturday")
    print("7) Remove from Sunday")
    print("8) Go Back")
    print("\n")

    user_remove = input("Select a day: ")
    if user_remove == "1":
        """idk"""
    elif user_remove == "2":
        """idk"""
    elif user_remove == "3":
        """idk"""
    elif user_remove == "4":
        """idk"""
    elif user_remove == "5":
        """idk"""
    elif user_remove == "6":
        """idk"""
    elif user_remove == "7":
        """idk"""
    elif user_remove == "8":
        main_menu()
    else:
        print("Choose from the option list!!!")

def edit_menu():
    print("\n")
    print("1) Edit Monday")
    print("2) Edit Tuesday")
    print("3) Edit Wednesday")
    print("4) Edit Thursday")
    print("5) Edit Friday")
    print("6) Edit Saturday")
    print("7) Edit Sunday")
    print("8) Go Back")
    print("\n")
    edit_menu = input("Select a day: ")
    if edit_menu == "1":
        """idk"""
    elif edit_menu == "2":
        """idk"""
    elif edit_menu == "3":
        """idk"""
    elif edit_menu == "4":
        """idk"""
    elif edit_menu == "5":
        """idk"""
    elif edit_menu == "6":
        """idk"""
    elif edit_menu == "7":
        """idk"""
    elif edit_menu == "8":
         main_menu()
    else:
        print("Choose from the option list!!!")


    
    
    
print("Choose from the option list!!!")




    
"""
def add_task():
   while True:
        user_input = input().lower() 
        if user_input == "add tasks":
            print("What task would you like to add?")
            
        

        
        else:
            print("\n!! Choose from the option list !!\n")
"""

main_menu()

"""
Sajid's notes:
the first main menu is pretty good as is in my opinion.
Now for each option like view and todo. Just give a few lines you might think would be needed. E.G

def view menu():
    print("would you like to see all your todos or filter")
    y or n
    if they want to filter let the user input some filters like what category they want to see for example
    category = input("please enter a category or press n to skip this filter")

    day = input("please enter a day or press n to skip this filter")


^^ we can alter and change things about if needs be

One of your other tasks are to remove todos:

def DeleteTodo():
id = input("please enter the id of the selected todo")

See if you can retrieve that todo from the json file (use google/chatgpt) and print out the specific todo 

then ask the user to confirm the choice and have a go at deleting it (again use google and chatgpt). I also sent a picture of my json file of tasks so copy that to see how it would look like
"""







