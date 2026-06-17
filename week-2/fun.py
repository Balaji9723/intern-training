# a Contact Book stored in a dictionary with add_contact(), find_contact(), and list_contacts() functions.

contact_result=  {}

def add_contact():
    
    try:
        name = input("enter name:")
        mobile_no= int(input("enter mobile number:"))
        contact_result[name] = mobile_no
    except ValueError:
        print("Value is not correct")


    print("\n result successful")


def find_contact():
    name = input("search a Name")

    try:
        print(contact_result[name])
    except KeyError as e:
        print("Contact is not founded",e)
    

def list_contact():
     if len(contact_result) == 0:
        print("\n No contacts available")
     else:
        print("\nContact List")
    
        for name, phone in contact_result.items():
            print(name, ":", phone)

        print()


