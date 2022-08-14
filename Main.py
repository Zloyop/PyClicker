import keyboard, time, mouse

is_clicking  = False

def set_clicker():
    global is_clicking
    if is_clicking: is_clicking = False
    else: is_clicking = True

keyboard.add_hotkey('Alt + Z', set_clicker)

while True:
    if is_clicking:
        mouse.click(button = 'left')
        time.sleep(0.01)
