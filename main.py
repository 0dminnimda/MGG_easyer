from pynput import mouse as mou
from pynput import keyboard
from pynput.mouse import Button, Controller
from time import sleep as sl
from detection import glob, reward

def on_move(x, y):
    #print('Pointer moved to {(x, y)}')
    pass

def on_click(x, y, button, pressed):
    if pressed == True:
        global mouse
        print(mouse.position)#((x, y))#'{0} at {1}'.format(
        #'Pressed' if pressed else 'Released',
        #(x, y)))
    if not pressed:
        # Stop listener
        return True

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

def on_press(key):
    global p
    try:
        #print(f'alphanumeric key {key.char} pressed')
        p = key.char
    except AttributeError:
        #print(f'special key {key} pressed')
        p = key

def on_release(key):
    #print(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def first_act():
    sl(0.2)
    movc("main_fig")
    sl(1)
    movc(figs[1])
    sl(1)
    movc(divs[3])
    find_place(8)
    sl(0.4)
    movc("enter")
    sl(1)
    movc(lvls[8])
    sl(3)
    movc("close")

def mp():
    global mouse
    return mouse.position

def mov(name):
    global mouse, pos_s
    mouse.position = pos_s[name]

def clc(num=1):
    global mouse
    mouse.click(Button.left, num)

def movc(name, num=1):
    global mouse, pos_s
    mouse.position = pos_s[name]
    mouse.click(Button.left, num)

def find_place(num):
    for i in range(8-num):
        movc("left")

def act():
    sl(0.1)
    #movc("close")
    #sl(0.1)
    movc("main_fig")
    sl(0.3)
    movc(figs[1])
    movc(divs[3])
    find_place(8)
    sl(0.4)
    movc("enter")
    act_after()
    for i in []:#lvls:
        movc(i, 0)
        sl(1)
    #movc("close")
    pass

def act_after():
    sl(0.4)
    movc(lvls[8])
    sl(2)
    find_need()
    movc("down")
    movc(rows[3])
    movc(rows[4])
    movc("validate")
    sl(1)
    movc("notag")
    movc("validate")
    sl(8)

def find_need():
    movc("open_sort")
    sl(0.4)
    movc(sort[3])
    sl(0.3)
    movc(gens[6])
    sl(0.3)
    movc(rows[0]) 

def atac():
    global gl_num
    if glob() is True:
        if gl_num < 2:
            movc(atack[1])
        else:
            movc(atack[0])
        gl_num += 1
    else:
        movc(atack[0])
    movc(enms[1])

#listenerk = keyboard.Listener(
#    on_press=on_press,
#    on_release=on_release)
#listenerk.start()

m_lis = 0
fir = 0

mouse = Controller()
if bool(m_lis) is True:
    print("pos mode")
    listener = mou.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
    listener.start()

    while m_lis:
        pass

for _ in range(1): 
    figs = [f"{i}-fig" for i in range(3)]
    divs = [f"{i}-div" for i in range(7)]
    rows = [f"{i}-row" for i in range(5)]
    lvls = [f"{i}-lvl" for i in range(9)]
    enms = [f"{i}-enm" for i in range(3)]
    gens = [f"{i}-gen" for i in range(7)]
    sort = [f"{i}-gen" for i in range(6)]
    atack = [f"{i}-atc" for i in range(2)]
    pos_s = {
        "intr":(515, 845),
        "close":(1170, 200),
        "up":(550, 303),
        "down":(550, 666),
        "main_fig":(715, 750),
        "enter":(600, 545),
        "back":(340, 760),
        "left":(350, 470),
        "righ":(850, 470),
        atack[0]:(570, 780),
        atack[1]:(730, 780),
        "validate":(630, 750),
        "notag":(800, 700),
        "open_sort":(410, 280),
        }
    for i in range(len(figs)): pos_s[figs[i]] = (360+255*i, 725)
    for i in range(len(divs)): pos_s[divs[i]] = (265+110.5*i, 730)
    for i in range(len(rows)): pos_s[rows[i]] = (280, 330+83*i)
    for i in range(3):
        for j in range(3):
            pos_s[lvls[i+j*3]] = (400+200*i, 355+100*j)
    for i in range(len(gens)): pos_s[gens[i]] = (275+40*i, 255)
    for i in range(len(sort)): pos_s[sort[i]] = (435, 300+20*i)
    pos_s[enms[0]] = (850, 320)
    pos_s[enms[1]] = (950, 430)
    pos_s[enms[2]] = (1020, 620)
    print(pos_s)

fig_num = 1

sl(1)
if bool(fir) is True:
    movc("intr")
    first_act()
    sl(0.5)
    first_act()
else:
    movc("intr")
    act()
    for fi in range(fig_num):
        gl_num = 0
        while 1:
            if reward() is True:
                print("end")
                movc("close")
                break
            atac()
            sl(2)
        if fi != fig_num - 1:
            act_after()