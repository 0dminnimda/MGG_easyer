import numpy as np
s1, s2 = 7.52, 5.99 #9.09, 4.55
team = [7.87, s1, s2]
enemy = [5]#[4.55] * 3
speed = np.array(team + enemy)
rem = np.zeros_like(speed)
steps = np.zeros_like(speed)
st_num = np.zeros_like(speed)
speed.sort()
ratio = np.round_(speed/speed.min(), 2)
num = 5

print(speed)
for i in range(num):
    st_num += steps
    steps = np.trunc(ratio + rem)
    rem = ratio - steps
    print(f"\n{i} step")
    arr = {}
    for m in range(speed.shape[0]):
        for n in range(int(steps[m])):
            a = n*speed[m]/(ratio[m])
            if a == 0:
                a = speed[m]
            arr[str(m)+"_"+str(n)] = a
    vals = list(arr.values())
    keys = list(arr.keys())
    sor = sorted(vals)[::-1]
    for i in sor:
        print(list(keys[vals.index(i)])[0], end=" ")