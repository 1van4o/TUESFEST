
class Admin:
  def __init__(self, username, password)                             :
    self.username = username
    self.password = password

admin= Admin("abc", "abc")


print("Admin User Login")
username_login    =str(input("Plesase Enter Username:\n"))
password_login    =str(input("Plesase Enter Password:\n"))
if admin.username    == username_login and admin.password== password_login :
  print("You are in")
  print("What do you want to do")
  option = str(input("Read file(1) Write file (2)\n"))
  if option == "1" :
    file = open('visitor_info.txt', 'r')
    New = []
    for line in file:
      visitor_info = line.strip()
      New.append(visitor_info)
    print(New)

  elif option == "2" :
   print("working on it sry")

else : print("You are not in")
