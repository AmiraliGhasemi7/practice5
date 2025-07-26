x1 = float(input("enter number: "))
y1 = float(input("enter number: "))
x2 = float(input("enter number:"))
y2 = float(input("enter number:"))

# گرفتن سرعت
speed = float(input("enter speed number"))
# فاصله بین دو نقطه
distance =((x2 - x1)**2 + (y2 - y1)**2)

# محاسبه زمان (زمان = فاصله / سرعت)
if speed > 0:
    time = distance / speed
    print("زمان لازم برای رسیدن از نقطه A به نقطه B: {time} واحد زمانی")
else:
    print("سرعت باید عددی بزرگتر از صفر باشد.")