import numpy as np
s1, s2 = 9.09, 4.55
team = [7.87, s1, s2]
enemy = [4.55] * 3
speed = np.array(team + enemy)
rem = np.zeros_like(speed)
steps = np.zeros_like(speed)
speed.sort()

sp = np.round_(speed/speed.min(), 2)
steps = np.floor(sp)
rem = sp-steps#np.trunc(sp)

#speed = list(np.rint(sp))  

print(speed)
print(steps)
print(rem)
print(sp)