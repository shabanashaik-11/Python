a=int(input())
b=int(input())
c=int(input())
if a<b and a<c :
   print("a is smaller")
elif b<a and b<c:
   print(" b is smaller")
elif c<a and c<b:
   print(" c is smaller")
elif a==b and a<c:
   print("a and b are equal and a,b are smaller ")
elif a==c and a<b:
   print("a and c are equal and a,c are smaller ")
elif a==b and b==c :
   print("a,b,c are equal")
