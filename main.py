import time
from interpreters.ai_interpreter import interpret_command
from actions import mouse, keyboard, system
from state.state_manager import StateManager

# Initialize the state manager
state_manager = StateManager()

# Define the actions dictionary
actions = {
    'move_and_click': mouse.move_and_click,
    'type_string': keyboard.type_string,
    'press_keys': keyboard.press_keys,
    'execute_command': system.execute_command,
    'time': time  # Include the time module to use sleep
}

def execute_ai_command(command):
    # Get the interpretation from the AI
    interpretation = interpret_command(command)
    print(f"AI interpretation: {interpretation}")
    try:
        # Split the interpretation into individual commands and execute them one by one
        for line in interpretation.split('\n'):
            if line.strip():  # Check if the line is not empty
                exec(line, {'__builtins__': __builtins__}, actions)
        state_manager.update_state("last_action_status", "Success")
    except Exception as e:
        print(f"Error executing command: {e}")
        state_manager.update_state("last_action_status", f"Failed: {e}")

def main():
    while True:
        user_command = input("Enter a command (or type 'exit' to quit): ")
        if user_command.lower() == "exit":
            print("Exiting...")
            break
        execute_ai_command(user_command)

if __name__ == "__main__":
    main()
