amount=int(input())
f_n=amount//500
rem=amount%500
print("Five hundred notes:(500)",+f_n)
h_n=rem//100
rem=rem%100
print("hundred note:(100)",+h_n)
fy_n=rem//50
rem=rem%50
print("fifty note:(50)",+fy_n)
t_n=rem//10
rem=rem%10
print("ten notes:(10)",+t_n)
