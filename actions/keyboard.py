import pyautogui
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def type_string(text):
    try:
        pyautogui.write(text, interval=0.1)
        logging.info(f"Typed text: {text}")
        return True
    except Exception as e:
        logging.error(f"Failed to type text: {e}")
        return False

def press_keys(*keys):
    try:
        pyautogui.hotkey(*keys)
        logging.info(f"Pressed keys: {keys}")
        return True
    except Exception as e:
        logging.error(f"Failed to press keys: {e}")
        return False
