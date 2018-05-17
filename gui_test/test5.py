import math

x = 10
y = 10
width = 40
height = 50
rotate = 20

xl = math.hypot(width / 2, height / 2)
a = math.asin(width / 2 / xl) * 180 / math.pi
print(math.sqrt(a/180)*xl*math.pi)
print(math.asin(width / 2 / xl) * 180 / math.pi)
print(math.asin(height / 2 / xl) * 180 / math.pi)

