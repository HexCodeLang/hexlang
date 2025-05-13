import re
import sys

variables = {}
functions = {}

def say(message):
    print(message)

def run_hex(code):
    lines = code.strip().split('\n')
    for line in lines:
        line = line.strip()

        # Print
        if line.startswith("say "):
            message = re.search(r'say \"(.*)\"', line)
            if message:
                say(message.group(1))

        # Variable Declaration
        elif line.startswith("let’s make a number called "):
            match = re.match(r"let’s make a number called (\w+) = (.+)", line)
            if match:
                var, value = match.groups()
                variables[var] = eval(value, {}, variables)

        # Input
        elif line.startswith("ask the user for their "):
            match = re.match(r"ask the user for their (\w+)", line)
            if match:
                var = match.group(1)
                variables[var] = input(f"Enter your {var}: ")

        # If statement
        elif line.startswith("if "):
            match = re.match(r"if (.+), say \"(.+)\"", line)
            if match:
                condition, message = match.groups()
                condition = condition.replace("=", "==")
                if eval(condition, {}, variables):
                    say(message)

        # Loop
        elif line.startswith("for each "):
            match = re.match(r"for each (\w+) in (\w+), say the (\w+)", line)
            if match:
                item, list_name, say_item = match.groups()
                iterable = variables.get(list_name, [])
                for val in iterable:
                    say(val)

        # One-liner function definition
        elif line.startswith("whenever you need to "):
            match = re.match(r'whenever you need to (\w+), say \"(.*)\"', line)
            if match:
                name, message = match.groups()
                functions[name] = lambda msg=message: say(msg)

        # Function call
        elif line.endswith("now"):
            func_name = line.split()[0]
            if func_name in functions:
                functions[func_name]()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hex.py <file.hex>")
    else:
        with open(sys.argv[1], 'r') as f:
            hex_code = f.read()
        run_hex(hex_code)
