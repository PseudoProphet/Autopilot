import pyautogui
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def move_and_click(x, y, duration=0.5):
    try:
        pyautogui.moveTo(x, y, duration=duration)
        pyautogui.click()
        logging.info(f"Mouse moved to ({x}, {y}) and clicked.")
        return True
    except Exception as e:
        logging.error(f"Failed to move and click: {e}")
        return False
 