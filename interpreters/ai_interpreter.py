import os
from openai import OpenAI
from config import OPENAI_API_KEY
from state.state_manager import StateManager

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


state_manager = StateManager()

def interpret_command(command):
    context = state_manager.get_state("context") or ""

    prompt = f"""
    You are an assistant that has access to the following functions:

    1. `move_and_click(x, y)` - Moves the mouse to the coordinates (x, y) and performs a click.
    2. `type_string(string)` - Types out the given string.
    3. `press_keys(keys)` - Presses the given sequence of keys.
    4. `execute_command(command)` - Executes a system command.


    Please interpret the following user commands and provide the Python code using the available functions:
    
    Examples:
    - User Command: "Open browser and go to 'wikipedia.com'"
      response: execute_command("start chrome.exe")\ntime.sleep(3)\ntype_string('wikipedia.com')\npress_keys('enter')

    - User Command: "Type 'Hello World' in notepad"
      response: execute_command("start notepad.exe")\ntype_string('Hello World')

    - User Command: "Move mouse to the top left corner and click"
      response: move_and_click(0, 0)

    User Command: {command}

    Do not respond with anything else, just the function, with appropriate code.
    
    """



    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=150,
        n=1,
        temperature=0.5
    )
    new_context = response.choices[0].message.content.strip()
    state_manager.update_state("context", context + "\n" + new_context)
    return new_context
