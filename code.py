x = int(input("enter value for x: "))
y = int(input("enter value for y: "))
z = int(input("enter value for z: "))
xvalue = (x - 0.5) * y
sqrtOfXY = (xvalue ** 0.5) + 1
f1 = sqrtOfXY / 1

xzValue = x ** z
f2 = 1 + (y * xzValue)

zValue = z + 1
zValue2 = zValue ** 0.5
zValue3 = z ** y

value4 = ((zValue2 * 4) + 1 - zValue3)
f3 = (value4 / 1)

f = f1 + (f2 * f3)

print(f)
