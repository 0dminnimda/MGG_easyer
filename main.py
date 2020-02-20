from pynput import mouse as mou
from pynput import keyboard
from pynput.mouse import Button, Controller
from time import sleep as sl

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

#listenerk = keyboard.Listener(
#    on_press=on_press,
#    on_release=on_release)
#listenerk.start()

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

m_lis = 0
mouse = Controller()
if bool(m_lis) is True:
    listener = mou.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
    listener.start()

    while m_lis:
        pass

figs = [f"{i}_fig" for i in range(3)]
divs = [f"{i}_div" for i in range(7)]
rows = [f"{i}_row" for i in range(5)]
pos_s = {
    "intr":(515, 845),
    "close":(1170, 200),
    "up":(550, 303),
    "down":(550, 666),
    "m_fig":(715, 750),

    }
for i in range(len(figs)): pos_s[figs[i]] = (360+255*i, 725)
for i in range(len(divs)): pos_s[divs[i]] = (265+110.5*i, 730)
for i in range(len(rows)): pos_s[rows[i]] = (280, 330+83*i)

print(pos_s)

def act():
    movc("intr")
    sl(0.2)
    movc("m_fig")
    sl(0.6)
    movc(figs[1])
    for i in divs:
        movc(i, 0)
        sl(1)

    movc("close")

sl(1)
act()