a=float(input("a=enter your number:"))
b=float(input("b=enter your number:"))
c=float(input("c=enter your number:"))
# محاسبه دلتا
delta=(b**2)-4*(a*c)
print("delta=(b**2)-4*(a*c)")
# محاسبه ریشه
if delta>0:
    x1=(-b-delta**0.5)/(2*a)
    x2=(-b+delta**0.5)/(2*a)
    print("x1=",x1)
    print("x2=",x2)
elif delta==0:
    x=(-b-delta**0.5)/(2*a)
    print("x=",x)