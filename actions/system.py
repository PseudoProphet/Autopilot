import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Command executed successfully: {command}")
            logging.info(f"Output: {result.stdout}")
            return True, result.stdout
        else:
            logging.error(f"Command failed: {command}")
            logging.error(f"Error: {result.stderr}")
            return False, result.stderr
    except Exception as e:
        logging.error(f"Failed to execute command: {e}")
        return False, str(e)
