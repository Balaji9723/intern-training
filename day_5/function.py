# a Contact Book stored in a dictionary with add_contact(), find_contact(), and list_contacts() functions.

contact_result=  {}

def add_contact():
    name = input("enter name:")
    mobile_no= input("enter mobile number:")
    contact_result[name] = mobile_no

    print("\n result successful")


def find_contact():
    name = input("search a Name")

    if name in contact_result:
        print(contact_result[name])
    else :
        print ("No contacts")

def list_contact():
     if len(contact_result) == 0:
        print("\n No contacts available")
     else:
        print("\nContact List")
    
        for name, phone in contact_result.items():
            print(name, ":", phone)

        print()


while True:

    i = input("Enter your choice: ")
    print("1. add contact")
    print("2. find contact")
    print("3. list contact")
    print("4. exit")

    if i== "1":
        add_contact()
    elif i== "2":
        find_contact()
    elif i== "3":
        list_contact()
    elif i== "4":
        print("ended ")
        break
        
    else :
        print ("\n Invalid ")






# a To-Do List stored in a list with add_task(), remove_task(), and show_tasks() functions.

# tasks = []

# def add_task():
#     task = input("Enter Task: ")
#     tasks.append(task)
#     print("\n  Added Successfully")

# def remove_task():
#     task = input("Enter Task to Remove: ")

#     if task in tasks:
#         tasks.remove(task)
#         print("\n Task Removed Successfully")
#     else:
#         print("\n Task Not Found")

# def show_task():
#     if len(tasks) == 0:
#         print("\n No Tasks Available")
#     else:
#         print("\n----- To-Do List -----")
#         for task in tasks :
#             print(task)
#         print()


# while True:

#     i = input("Enter your task: ")
#     print("1. add task")
#     print("2. show task")
#     print("3. remove task")
#     print("4. exit")

#     if i== "1":
#         add_task()
#     elif i== "2":
#         show_task()
#     elif i== "3":
#         remove_task()
#     elif i== "4":
#         print("ended ")
#         break
        
#     else :
#         print ("\n Invalid ")