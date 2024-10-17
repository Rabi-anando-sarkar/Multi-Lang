def checkTrinagle(a,b,c):
    if a == b and b == c and c == b:
        return "Equilateral Triangle"
    elif a == b or b == c or c == a:
        return "Isosceles Triangle"
    else: 
        return "Scalene Triangle"

print(checkTrinagle(1,2,3))
print(checkTrinagle(3,2,3))
print(checkTrinagle(3,3,3))