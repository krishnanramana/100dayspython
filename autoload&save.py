inventory = [] #change variable name and replace everywhere

def autoload():
  try:
    f = open("inventory.txt", "r") #change filename
    content = f.read()
    if content == "":
      return []
    else:
      inventory = eval(content)
      f.close()
      return inventory
  except Exception as e:
    print(f"Some error occured {e}")
    return []
  
def autosave(inventory):
  f = open("inventory.txt", "w") #change filename
  f.write(str(inventory))
  f.close()
