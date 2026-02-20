from pynput import keyboard
import time
from gui import GUI
import os,sys , json
import tomllib

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
json_path = os.path.join(BASE_DIR, "text_lines.json")
try:
    with open(json_path,"r",encoding="utf-8") as file:
        text_lines = json.load(file)
except Exception as e:
    print(f"Error: No text lines provided or incorrect file structure")
    os._exit(0)
config_path = os.path.join(BASE_DIR, "config.toml")

try:
    with open(config_path,"rb") as file:
        config = tomllib.load(file)
except Exception as e:
    print(f"Error: Missing config file or incorrect file structure")
    os._exit(0)

GLOBAL_CHAT = True


#create keyboard controller
controller = keyboard.Controller()
# send message to chat 
# Args: msg - (string) message
#       is_all_chat - (Boolean) is message suposed to be send to all chat   
def select_item(gui,number):
    msg = gui.select_item(number)
    if msg:
        send_message(msg, GLOBAL_CHAT)

SPECIAL_KEYS = {
    "<enter>": keyboard.Key.enter,
    "<space>": keyboard.Key.space,
    "<tab>":   keyboard.Key.tab,
    "<esc>":   keyboard.Key.esc,
    "<ins>":   keyboard.Key.insert
}

def get_key(key_string):
    return SPECIAL_KEYS.get(key_string.lower(), key_string)

def send_message(msg, is_all_chat):
    controller.press(get_key(config["chat"]["open_chat"]))
    controller.release(get_key(config["chat"]["open_chat"]))
    
    time.sleep(0.05) 
    
    if is_all_chat:
        controller.type(f"{config["chat"]["all_chat"]} ")
    else:
        controller.type(f"{config["chat"]["team_chat"]} ")

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

gui = GUI(text_lines,config)

def toggle_all_chat():
    global GLOBAL_CHAT
    GLOBAL_CHAT = not GLOBAL_CHAT



#register listeners 
hotkey = keyboard.GlobalHotKeys({
    config["hotkeys"]["toggle_gui"] : gui.trigger_toggle, 
    config["hotkeys"]["previous_page"]: gui.trigger_next,
    config["hotkeys"]["next_page"]: gui.trigger_prev,
    config["hotkeys"]["back_to_categories"]: gui.back_to_categories,
    config["hotkeys"]["pick_1"]: lambda: select_item(gui,0),
    config["hotkeys"]["pick_2"]: lambda: select_item(gui,1),
    config["hotkeys"]["pick_3"]: lambda: select_item(gui,2),
    config["hotkeys"]["pick_4"]: lambda: select_item(gui,3),
    config["hotkeys"]["pick_5"]: lambda: select_item(gui,4),
    config["hotkeys"]["toggle_chat"]: toggle_all_chat ,
    config["hotkeys"]["exit_app"]: lambda: exit_app(gui,hotkey) }) 


hotkey.start()

if __name__ == "__main__":
    try:
        gui.run()
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        exit_app(gui, hotkey)