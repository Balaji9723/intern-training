l = []

def add_task(task):
    l.append(task)
    print("Task added successfully")

def remove_task(r):
    l.pop(r)
    print("Remove successfully")

def show_task():
    for task in l:
        print(task)
    print("Displayed Successfully")

while(True):
    print("\n1.Add the task\n2.Remove the task\n3.Show the task")
    n = int(input("Enter the choice: "))
    if(n == 1): 
        task = input("\nEnter the Task: ")
        add_task(task)
    elif(n == 2): 
        show_task()
        r = int(input("Enter the remove task no. "))
        remove_task(r-1)
    elif(n==3): show_task()