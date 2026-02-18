from pynput import keyboard
import time
from gui import GUI
import text_lines
import os

#create keyboard controller
controller = keyboard.Controller()

# send message to chat 
# Args: msg - (string) message
#       is_all_chat - (Boolean) is message suposed to be send to all chat   
def select_item(gui,number):
    msg = gui.select_item(number)
    if msg:
        send_message(msg,True)

def send_message(msg, is_all_chat=True):
    controller.press(keyboard.Key.enter)
    controller.release(keyboard.Key.enter)
    
    time.sleep(0.05) 
    
    if is_all_chat:
        controller.type("/all ")
    else:
        controller.type("/team ")

    controller.type(msg)
    
    time.sleep(0.05)
    
    controller.press(keyboard.Key.enter)
    controller.release(keyboard.Key.enter)

# quits from app 
def exit_app(gui, hotkey):
    try:
        hotkey.stop()
        gui.trigger_exit()
    finally:

        os._exit(0)

gui = GUI()
gui.load_text_lines(text_lines.data)

#register listeners 
hotkey = keyboard.GlobalHotKeys({
    '\\': gui.trigger_toggle, 
    '.': gui.trigger_next,
    ',': gui.trigger_prev,
    '/': gui.back_to_categories,
    '6': lambda: select_item(gui,0),
    '7': lambda: select_item(gui,1),
    '8': lambda: select_item(gui,2),
    '9': lambda: select_item(gui,3),
    '0': lambda: select_item(gui,4),
    '<f10>': lambda: exit_app(gui,hotkey) }) 


hotkey.start()

if __name__ == "__main__":
    try:
        gui.run()
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        exit_app(gui, hotkey)