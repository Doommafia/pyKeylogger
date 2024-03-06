from pynput.keyboard import Key, Listener

def on_press(key):
    if key == Key.enter or key == Key.space:
        print('\n', end='', flush=True)
    else:
        print(key, end=', ', flush=True)

def on_release(key):
    if key == Key.esc:  # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
