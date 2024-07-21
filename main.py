import os
todolist = []
f = open("todolist.txt","r")
todolist = eval(f.read())
f.close()

def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

def addtodo():
  task = input("What task do you want to add to your to-do list? ").strip().capitalize()
  due = input("When is it due? (dd/mm/yyyy) ").strip().capitalize()
  priority = input("What is the priority? (high, medium, low) ").strip().capitalize()
  row = [task, due, priority]
  todolist.append(row)
  print(f"Task to {task} added to your to-do list.")
  print("\n")

def prettyprint():
  for row in todolist:
    for item in row:
      if item != None:
        print(item,end = " | ")
    print("\n")

def viewtodo():
  userinput = input("Do you want to view all? Or view by priority? (a/p) ").strip().lower()
  if userinput[0] == 'a':
    prettyprint()
  elif userinput[0] == 'p':
    priority = input("What priority do you want to view? (high, medium, low) ").strip().capitalize()
    for row in todolist:
      if priority in row:
        for item in row:
          print(item,end = " | ")
        print("\n")

def edittodo():
  task = input("What task you want to edit? ").strip().capitalize()
  for row in todolist:
    if task in row:
      print(f"The task {task} has been found and has a priority of {row[2]} and due date of {row[1]}. ")
      editinput = input("What do you want to edit? (task, due date, priority) (t/d/p) ").strip().lower()
      if editinput[0] == 't':
        row[0] = input("What do you want to change the task to? ").strip().capitalize()
        print(f"Task changed to {row[0]}.")
      elif editinput[0] == 'd':
        row[1] = input("What do you want to change the due date to? (dd/mm/yyyy) ")
        print(f"Due date changed to {row[1]}.")
      elif editinput[0] == 'p':
        row[2] = input("What do you want to change the priority to? (high, medium, low) ").strip().capitalize()
        print(f"Priority changed to {row[2]}.")
      else:
        print("Invalid input!")


def removetodo():
  task = input("What task you want to remove? ").strip().capitalize()
  for row in todolist:
    if task in row:
      todolist.remove(row)
      print(f"Task {task} has been removed.")
      break
  print(f"Task {task} not found!")


os.system("clear")
print("    Life Organizer!       ")

while True:
  userinput = input("Welcome to the life organiser. Do you want to add, view, edit or remove a to do? Or exit? (a/v/e/r/x) ").strip().lower()

  if userinput[0] == 'a':
    addtodo()
  elif userinput[0] == 'v':
    viewtodo()
  elif userinput[0] == 'e':
    edittodo()
  elif userinput[0] == 'r':
    removetodo()
  elif userinput[0] == 'x':
    exit()
  else:
    print("Invalid input")

  f = open("todolist.txt", "w") 
  f.write(str(todolist)) 
  f.close()