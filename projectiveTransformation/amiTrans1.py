import math

# Height in meters
h = 3 

# Offest of point from the centre of the picture
i = 200
j = 350

# Image size in pixels
I = 1024
J = 768

theta = math.pi / 4
phi= math.pi / 6

# alpha is in degrees (?)
alpha = math.pi / 5


xGround = (h * 2 * i / I * math.tan(theta / 2)) / (math.sin(alpha) - 2 * j / J * math.tan(phi / 2) * math.cos(alpha))

yGround= h * (2 * j / J * math.tan(phi / 2) * math.sin(alpha) + math.cos(alpha)) / (math.sin(alpha) - 2 * j / J * math.tan(phi / 2) * math.cos(alpha))

print ('xGround is: ', xGround, 'and yGround is: ', yGround)