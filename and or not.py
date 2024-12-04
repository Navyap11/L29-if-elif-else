a=10
b=12
c=2

if a and b and c:
    print("All of them are the same")

else:
    print("some of the numbers are not the same")

d= 2
e= -2

if d or e>0:
    print("One or more of the variables are greater than 0")

else:
    print("None are greater than 0")


f= 7
g= 7
h= 8

print(f!=g)
print(g!=h)
print(h!=f)


n= int(input("Enter a number: "))
v= int(input("Enetr a second number"))


if n or v >0:
    print("One value or more is greater than 0")
else:
    print("None of the values are greater than 0")

if n!=v:
    print("Not alike")
else:
    print("Alike")
