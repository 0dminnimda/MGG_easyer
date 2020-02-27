from pynput import mouse as mou
from pynput import keyboard
from pynput.mouse import Button, Controller
from time import sleep as sl
from detection import glob, reward, error
import cv2 as cv

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
    #movc("close")
    pass

def act_after():
    sl(0.4)
    movc(lvls[8])
    sl(2.5)
    find_need()
    after_find()
    #sl(0.5)
    #movc("down")
    #sl(0.5)
    #movc(rows[3])
    #sl(0.5)
    #movc(rows[4])
    #sl(0.5)
    #movc("validate")
    #sl(1)
    #movc("notag")
    #sl(0.5)
    #movc("validate")
    #sl(8)
    pass

def find_need():
    n = 0.5
    movc(gens[6])
    sl(n*2)
    movc("open_sort")
    sl(n*2)
    movc(sort[3])
    sl(n)
    movc(rows[0])
    sl(n)
    movc("open_sort")
    sl(n*2)
    movc(sort[1])
    sl(n)
    movc(gens[0])
    sl(n*2)

def after_find():
    n = 0.4
    sl(n)
    movc("down")
    sl(n)
    movc(rows[3])
    sl(n)
    movc(rows[4])
    sl(n*2)
    movc("validate")
    sl(n*2)
    movc("notag")
    sl(n*2)
    movc("validate")
    sl(8)

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
    movc(enms[0])
    movc(enms[2])

def buy():
    movc("shop")
    sl(0.5)
    movc("supplies")
    sl(0.5)
    movc("shop_left")
    sl(0.5)
    movc("shop_left")
    sl(0.5)
    movc("passes")
    sl(0.5)
    movc("close")

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
    sort = [f"{i}-sor" for i in range(6)]
    atack = [f"{i}-atc" for i in range(2)]
    pos_s = {
        "intr":(515, 845),
        "close":(1170, 200),
        "up":(550, 303),
        "down":(550, 685),
        "main_fig":(715, 750),
        "enter":(600, 545),
        "back":(340, 760),
        "left":(350, 470),
        "righ":(850, 470),
        atack[0]:(570, 780),
        atack[1]:(730, 780),
        "validate":(630, 750),
        "notag":(800, 700),
        "open_sort":(410, 290),
        "ok":(610, 727),
        "refresh":(85, 50),
        "shop":(830, 755),
        "supplies":(815, 290),
        "shop_left":(1025, 545),
        "passes":(875, 700),
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
    pos_s[enms[1]] = (940, 430)
    pos_s[enms[2]] = (1020, 620)
    print(pos_s)

fig_num = 2
ses_num = 5

lose = cv.imread('img7.png')
win = cv.imread('img8.png')
erimg = cv.imread('img15.png')

lim = 50000

err = 0
sl(1)
if bool(fir) is True:
    movc("intr")
    first_act()
    sl(0.5)
    first_act()
    movc("intr")
else:
    movc("intr")
    for ses in range(fig_num):
        print(f"{ses} session")
        act()
        for fi in range(ses_num):
            gl_num = 0
            err = 0
            while 1:
                last = False
                if err >= lim//2:
                    sl(0.5)
                    print("chance")
                if error(erimg) is True:
                    last = not False
                    err += 1
                if last is False:
                    err = 0
                #print(err, end=" ")
                if err >= lim:
                    print("error")
                    break
                if (reward(win) or reward(lose)) is True:
                    print("\nend",end=" ")
                    if reward(win) is True:
                        print("win")
                    elif reward(lose) is True:
                        print("lose")
                    movc("close")
                    break
                atac()
                sl(2)
            if err >= lim:
                break
            sl(0.5)
            movc("ok")
            sl(0.5)
            movc("ok")
            if fi != ses_num - 1:
                act_after()
        if err >= lim:
            break
        movc("close")
        sl(1)
        buy()
    if err >= lim:
        #movc("refresh")
        sl(0.2)
    movc("intr")