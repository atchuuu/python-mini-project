a=int(input("Date: "))
b=int(input("Month: "))
c=int(input("Year: "))
x=str(c)
d="The starting date {}/{}/{}".format(a,b,c)
print(d)
p=int(input("Date: "))
q=int(input("Month: "))
r=int(input("Year: "))
y=str(r)
s="The end date {}/{}/{}".format(p,q,r)
print(s)
if a<=31 and b<13 and len(x)<=4 and p<=31 and q<=12 and len(y)<=4:
    if c<r:
        print("Here is a list of leap years between " + str(c) + " and " + str(r)  + ":")
        for i in range(c,r):
            if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                print(i,end=" \t")
    print("Here is a list of non-leap years between " + str(c) + " and " + str(r) + ":")
    for i in range(c,r):
        if (i%4!=0):
            print(i,end=" \t")
else:
    print("The entered number is invalid")
