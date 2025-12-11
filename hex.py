import re
import sys
import math

variables = {}
functions = {}
function_bodies = {}  # Store multiline function bodies
in_function_def = False
current_function = None
current_function_params = []
current_function_body = []

def say(message):
    print(message)

def evaluate_expression(expr):
    """Safely evaluate expressions with variable support"""
    global variables
    # Replace fancy apostrophes with regular ones
    expr = expr.replace("'", "'")
    
    # Handle string concatenation with "and"
    if " and " in expr and ("\"" in expr or "'" in expr):
        parts = re.split(r'\s+and\s+', expr)
        result = ""
        for part in parts:
            part = part.strip()
            if part.startswith("\"") and part.endswith("\""):
                result += part[1:-1]
            elif part.startswith("'") and part.endswith("'"):
                result += part[1:-1]
            elif part in variables:
                result += str(variables[part])
            else:
                try:
                    result += str(eval(part, {"__builtins__": {"abs": abs, "min": min, "max": max, "round": round, "pow": pow, "int": int, "float": float, "str": str, "len": len}}, variables))
                except:
                    result += part
        return result
    
    try:
        # Safe math operations
        safe_dict = {
            "__builtins__": {
                "abs": abs,
                "min": min, 
                "max": max,
                "round": round,
                "pow": pow,
                "int": int,
                "float": float,
                "str": str,
                "len": len
            }
        }
        return eval(expr, safe_dict, variables)
    except:
        return expr

def run_hex(code):
    global variables, functions, function_bodies
    global in_function_def, current_function, current_function_params, current_function_body
    
    variables = {}
    functions = {}
    function_bodies = {}
    in_function_def = False
    current_function = None
    current_function_params = []
    current_function_body = []
    
    lines = code.strip().split('\n')
    i = 0
    skip_next = False
    last_condition_result = False
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip comments and empty lines
        if not line or line.startswith("#"):
            i += 1
            continue
        
        # Handle multiline function definition start
        if line.startswith("whenever you need to ") and line.endswith(":"):
            match = re.match(r"whenever you need to (\w+)(?: with (.+?))?:", line)
            if match:
                in_function_def = True
                current_function = match.group(1)
                params_str = match.group(2)
                current_function_params = []
                if params_str:
                    current_function_params = [p.strip() for p in params_str.split(" and ")]
                current_function_body = []
                i += 1
                continue
        
        # Handle function body end
        if in_function_def and (line == "that's it" or line == "that's it" or line == "done"):
            function_bodies[current_function] = {
                'params': current_function_params,
                'body': current_function_body[:]
            }
            in_function_def = False
            current_function = None
            current_function_params = []
            current_function_body = []
            i += 1
            continue
        
        # Collect function body lines
        if in_function_def:
            current_function_body.append(line)
            i += 1
            continue
        
        # Handle otherwise/else
        if line.startswith("otherwise, ") or line.startswith("otherwise "):
            if skip_next:
                # Skip this otherwise because previous if was true
                skip_next = False
                i += 1
                continue
            else:
                # Execute the otherwise branch
                action = line.replace("otherwise, ", "").replace("otherwise ", "")
                execute_line(action)
                i += 1
                continue
        
        # Reset skip_next if we encounter a non-otherwise line
        if skip_next:
            skip_next = False
        
        # Execute line and check if it was an if statement
        was_if, condition_result = execute_line(line)
        if was_if:
            last_condition_result = condition_result
            # If condition was true, skip next otherwise (if there is one)
            if condition_result:
                skip_next = True
        
        i += 1

def execute_line(line):
    """Execute a single line of HexLang code
    Returns: (was_if_statement, condition_result)
    """
    global variables, functions, function_bodies
    
    # Print with variable interpolation
    if line.startswith("say "):
        # Handle string with variable or expression
        match = re.search(r'say \"(.*)\"', line)
        if match:
            message = match.group(1)
            # Replace {variable} with variable value
            for var in variables:
                message = message.replace("{" + var + "}", str(variables[var]))
            say(message)
        # Handle saying a variable directly
        else:
            match = re.match(r'say (\w+)', line)
            if match:
                var = match.group(1)
                if var in variables:
                    say(str(variables[var]))
        return (False, False)

    # Variable Declaration - number
    elif line.startswith("let's make a number called ") or line.startswith("let's make a number called "):
        match = re.match(r"let'?s make a number called (\w+) = (.+)", line)
        if match:
            var, value = match.groups()
            variables[var] = evaluate_expression(value)
        return (False, False)

    # Variable Declaration - string
    elif line.startswith("let's make a string called ") or line.startswith("let's make a string called "):
        match = re.match(r"let'?s make a string called (\w+) = \"(.*)\"", line)
        if match:
            var, value = match.groups()
            variables[var] = value
        else:
            match = re.match(r"let'?s make a string called (\w+) = (.+)", line)
            if match:
                var, expr = match.groups()
                variables[var] = str(evaluate_expression(expr))
        return (False, False)
    
    # Variable Declaration - list
    elif line.startswith("let's make a list called ") or line.startswith("let's make a list called "):
        match = re.match(r"let'?s make a list called (\w+) = \[(.*)\]", line)
        if match:
            var, items_str = match.groups()
            items = []
            if items_str.strip():
                for item in items_str.split(","):
                    item = item.strip()
                    if item.startswith("\"") and item.endswith("\""):
                        items.append(item[1:-1])
                    else:
                        items.append(evaluate_expression(item))
            variables[var] = items
        return (False, False)

    # Add to list (must come before arithmetic add)
    elif line.startswith("add ") and " to list " in line:
        match = re.match(r"add (.+) to list (\w+)", line)
        if match:
            value, var = match.groups()
            if var in variables and isinstance(variables[var], list):
                if value.startswith("\"") and value.endswith("\""):
                    variables[var].append(value[1:-1])
                else:
                    variables[var].append(evaluate_expression(value))
        return (False, False)

    # Arithmetic operations - add to
    elif line.startswith("add ") and " to " in line:
        match = re.match(r"add (.+) to (\w+)", line)
        if match:
            value, var = match.groups()
            if var in variables:
                variables[var] = variables[var] + evaluate_expression(value)
        return (False, False)
    
    # Arithmetic operations - subtract from
    elif line.startswith("subtract ") and " from " in line:
        match = re.match(r"subtract (.+) from (\w+)", line)
        if match:
            value, var = match.groups()
            if var in variables:
                variables[var] = variables[var] - evaluate_expression(value)
        return (False, False)
    
    # Arithmetic operations - multiply by
    elif line.startswith("multiply ") and " by " in line:
        match = re.match(r"multiply (\w+) by (.+)", line)
        if match:
            var, value = match.groups()
            if var in variables:
                variables[var] = variables[var] * evaluate_expression(value)
        return (False, False)
    
    # Arithmetic operations - divide by
    elif line.startswith("divide ") and " by " in line:
        match = re.match(r"divide (\w+) by (.+)", line)
        if match:
            var, value = match.groups()
            if var in variables:
                divisor = evaluate_expression(value)
                if divisor != 0:
                    variables[var] = variables[var] / divisor
                else:
                    say("Error: Cannot divide by zero!")
        return (False, False)
    
    # Power operation
    elif line.startswith("raise ") and " to the power of " in line:
        match = re.match(r"raise (\w+) to the power of (.+)", line)
        if match:
            var, value = match.groups()
            if var in variables:
                variables[var] = variables[var] ** evaluate_expression(value)
        return (False, False)
    
    # Modulo operation
    elif line.startswith("get remainder of ") and " divided by " in line:
        match = re.match(r"get remainder of (\w+) divided by (.+)", line)
        if match:
            var, value = match.groups()
            if var in variables:
                variables[var] = variables[var] % evaluate_expression(value)
        return (False, False)

    # Input
    elif line.startswith("ask the user for their ") or line.startswith("ask the user for "):
        match = re.match(r"ask the user for (?:their )?(\w+)", line)
        if match:
            var = match.group(1)
            user_input = input(f"Enter {var}: ")
            # Try to convert to number if possible
            try:
                variables[var] = float(user_input) if '.' in user_input else int(user_input)
            except:
                variables[var] = user_input
        return (False, False)

    # Input with custom prompt
    elif line.startswith("ask "):
        match = re.match(r'ask \"(.+?)\" and (?:store|save) (?:it )?in (\w+)', line)
        if match:
            prompt, var = match.groups()
            user_input = input(prompt + " ")
            # Try to convert to number if possible
            try:
                variables[var] = float(user_input) if '.' in user_input else int(user_input)
            except:
                variables[var] = user_input
        return (False, False)

    # If statement with action
    elif line.startswith("if "):
        # If with say
        match = re.match(r"if (.+), say \"(.+)\"", line)
        if match:
            condition, message = match.groups()
            result = evaluate_condition(condition)
            if result:
                # Handle variable interpolation
                for var in variables:
                    message = message.replace("{" + var + "}", str(variables[var]))
                say(message)
            return (True, result)
        else:
            # If with action on variable
            match = re.match(r"if (.+), (.+)", line)
            if match:
                condition, action = match.groups()
                result = evaluate_condition(condition)
                if result:
                    execute_line(action)
                return (True, result)
        return (False, False)

    # Loop
    elif line.startswith("for each "):
        match = re.match(r"for each (\w+) in (\w+), say (?:the )?(\w+)", line)
        if match:
            item, list_name, say_item = match.groups()
            iterable = variables.get(list_name, [])
            for val in iterable:
                say(str(val))
        return (False, False)

    # Get list item
    elif " get item " in line and " from list " in line:
        match = re.match(r"get item (.+) from list (\w+) and save in (\w+)", line)
        if match:
            index, list_name, save_var = match.groups()
            if list_name in variables and isinstance(variables[list_name], list):
                idx = evaluate_expression(index)
                if 0 <= idx < len(variables[list_name]):
                    variables[save_var] = variables[list_name][idx]
        return (False, False)

    # One-liner function definition
    elif line.startswith("whenever you need to ") and ", say \"" in line:
        match = re.match(r'whenever you need to (\w+), say \"(.*)\"', line)
        if match:
            name, message = match.groups()
            functions[name] = lambda msg=message: say(msg)
        return (False, False)

    # Function call with parameters (must come before no-parameter check)
    elif " with " in line and line.endswith(" now"):
        match = re.match(r"(\w+) with (.+) now", line)
        if match:
            func_name, args_str = match.groups()
            if func_name in function_bodies:
                func_def = function_bodies[func_name]
                args = [a.strip() for a in args_str.split(" and ")]
                
                # Save current variable state
                saved_vars = variables.copy()
                
                # Bind parameters
                for i, param in enumerate(func_def['params']):
                    if i < len(args):
                        # Evaluate argument
                        arg = args[i]
                        if arg.startswith("\"") and arg.endswith("\""):
                            variables[param] = arg[1:-1]
                        elif arg in variables:
                            variables[param] = variables[arg]
                        else:
                            variables[param] = evaluate_expression(arg)
                
                # Execute function body
                for body_line in func_def['body']:
                    execute_line(body_line)
                
                # Restore variables (remove local params)
                for param in func_def['params']:
                    if param in variables and param not in saved_vars:
                        del variables[param]
        return (False, False)

    # Function call without parameters
    elif line.endswith(" now"):
        func_name = line.replace(" now", "").strip()
        if func_name in functions:
            functions[func_name]()
        elif func_name in function_bodies:
            # Execute multiline function
            for body_line in function_bodies[func_name]['body']:
                execute_line(body_line)
        return (False, False)
    
    return (False, False)

def evaluate_condition(condition):
    """Evaluate a condition and return boolean result"""
    global variables
    # Replace fancy apostrophes
    condition = condition.replace("'", "'")
    
    # Handle "is" keyword
    condition = condition.replace(" is not ", " != ")
    condition = condition.replace(" is ", " == ")
    
    # Handle single = as comparison (but not ==, <=, >=, !=)
    if "==" not in condition and "!=" not in condition and "<=" not in condition and ">=" not in condition:
        condition = condition.replace("=", "==")
    
    try:
        safe_dict = {
            "__builtins__": {
                "abs": abs,
                "min": min,
                "max": max,
                "round": round,
                "pow": pow,
                "int": int,
                "float": float,
                "str": str,
                "len": len
            }
        }
        return bool(eval(condition, safe_dict, variables))
    except:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hex.py <file.hexlang>")
        print("Note: For full features, use 'hexlang' command instead")
    else:
        with open(sys.argv[1], 'r') as f:
            hex_code = f.read()
        run_hex(hex_code)
