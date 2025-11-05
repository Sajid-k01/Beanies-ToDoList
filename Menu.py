import json
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
    print("Would you like to see all of your to-do's, fiter or go back")

    print("\n")

    user_view = input(" y , n or back ")

    if user_view == "y":
        for task in tasks:
            print(f'ID: {task["id"]}, description: {task["description"]}, category: {task["category"]} ')

    elif user_view == "n":
         category_input = input("Enter a category or press n to skip :").strip().lower()
         for task in tasks:
            if task["category"].strip().lower() == category_input:
                print(f'ID: {task["id"]},  description: {task["description"]}, category: {task["category"]} ')


        
    elif user_view == "back":
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
    id_remove = input("Select an id to remove: ")
    for task in tasks:
        print(f'ID: {task["id"]}, description: {task["description"]}, category: {task["category"]} ')
    print("\n")
    for task in tasks:
        print(f'ID: {task["id"]}, description: {task["description"]}, category: {task["category"]} ')
        if id_remove == task["id"]:
            remove_confirm = input(f"Are you sure u want to remove {id_remove}, y or n:  ")
            if remove_confirm == "y":
                tasks.remove(task)
                print(f"task {id_remove} has been successfully removed")
                with open("storage.json","w") as file:
                    json.dump({"tasks": tasks}, file)  
    return(main_menu())
    



            
  

def edit_menu():
    print("\n")

    
    print("\n")
   


    
    
    
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



import json
with open("storage.json","r") as file:
    to_do = json.load(file)
    tasks = to_do["tasks"]

main_menu()









