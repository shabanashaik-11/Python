password=input()
i=len(password)
a=['@','#','&','_','-','+','*','/',')','(','!','?',';','.',',']
if i<8:
     print("invalid password...")
else :
  digit=False
  upper=False
  lower=False
  sp=False
  for i in password:
     if i.isdigit():
          digit=True
     elif i.isupper():
          upper=True
     elif i.islower():
          lower=True
     elif i in a:
          sp=True
  if digit and upper and lower and sp:
    print("valid password")
  else :
    print("invalid password")
