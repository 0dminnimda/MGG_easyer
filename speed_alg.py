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
print(ratio)
print(speed*ratio)
print(speed/ratio)
print(ratio/speed)
for i in range(num):
    st_num += steps
    steps = np.trunc(ratio + rem)
    rem = ratio - steps
    print(f"\n\n{i} step")
    arr = {}
    for m in range(speed.shape[0]):
        print("[", end="")

        for n in range(int(steps[m])):
            #print(n, end=" ")  # st_num[m]+
            a = n*speed[m]/(ratio[m])
            if a == 0:
                a = speed[m]
            print(a, end=" ")
            arr[str(m)+"_"+str(n)] = a

        print("] ", end="")
    print("\n", arr)

    #print()
    #print(steps)
    #print(st_num)
    #print(rem)
    #print(sp)