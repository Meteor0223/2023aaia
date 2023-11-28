a = 1000000000
b = 2000000000

c =a%b
print(a,b,c)
while c!=0:#輾轉相除法
 a=b
 b=c
 c=a%b
 print(a,b,c)
print(b)