import re

while True:
  password = input("Create your password with 1 number, 1 uppercase")
  pattern = r"[A-Z]"
  pattern2 = r"[0-9]"
  if re.search(pattern, password):
    pass
  else:
    print("You need to use at least 1 uppercase in your password.\n")

  if re.search(pattern2, password):
    pass
  else:
    print("You need to use at least 1 number in your password.\n\n")
  if re.search(pattern, password) and re.search(pattern2, password):
    print("Password created!")
    break
