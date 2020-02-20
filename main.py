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

pos_s = {
    "up":(550, 303),
    "down":(550, 666),
    "0row":(280, 655),
    }

for i in range(4):
    pos_s[f"{i+1}row"] = (pos_s["0row"][0], pos_s["0row"][1]+83*i)
#pos_s += {"2row":(280, 655+83)}

print(pos_s)

def move(name):
    global mouse, pos_s
    mouse.position = pos_s[name]

def clc(num=1):
    global mouse
    mouse.click(Button.left, num)

def act():
    #global mouse, pos_s
    #move("up")
    #clc()
    #sl(1)
    move("down")
    clc()

sl(5)
act()