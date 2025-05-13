# hexlang_runtime.py

import sys

# Global state (main scope)
variables = {}
rituals = {}

def execute(lines, scope=None):
    if scope is None:
        scope = {}

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("#"):
            i += 1
            continue

        tokens = line.split()

        # --- Ritual definition ---
        if tokens[0] == "ritual":
            name = tokens[1]
            if "with" in tokens:
                args_index = tokens.index("with")
                args = tokens[args_index + 1:]
            else:
                args = []

            body = []
            i += 1
            while i < len(lines) and lines[i].strip() != "end":
                body.append(lines[i])
                i += 1
            rituals[name] = {"args": args, "body": body}
            i += 1
            continue

        # --- Ritual call ---
        if tokens[0] in rituals and "with" in tokens:
            name = tokens[0]
            args_index = tokens.index("with")
            call_args = tokens[args_index + 1:]

            ritual = rituals[name]
            if len(call_args) != len(ritual["args"]):
                raise Exception(f"Incorrect number of arguments for {name}")
            new_scope = dict(zip(ritual["args"], [eval_expr(arg, scope) for arg in call_args]))
            execute(ritual["body"], new_scope)
            i += 1
            continue

        # --- conjure ---
        if tokens[0] == "conjure":
            var_name = tokens[1]
            if tokens[2] != "to":
                raise Exception("Invalid syntax for conjure")
            value = eval_expr(" ".join(tokens[3:]), scope)
            scope[var_name] = value
            i += 1
            continue

        # --- bind ---
        if tokens[0] == "bind":
            var_name = tokens[1]
            if tokens[2] != "to":
                raise Exception("Invalid syntax for bind")
            value = eval_expr(" ".join(tokens[3:]), scope)
            scope[var_name] = value
            i += 1
            continue

        # --- whisper ---
        if tokens[0] == "whisper":
            message = line.split(" ", 1)[1]
            print(eval_expr(message, scope))
            i += 1
            continue

        else:
            raise Exception(f"Unknown incantation: {line}")

def eval_expr(expr, scope):
    expr = expr.strip()
    if expr.startswith('"') and expr.endswith('"'):
        return expr[1:-1]
    elif expr.isdigit():
        return int(expr)
    elif expr in scope:
        return scope[expr]
    elif expr in variables:
        return variables[expr]
    elif "+" in expr:
        parts = expr.split("+")
        return "".join(str(eval_expr(p.strip(), scope)) for p in parts)
    elif "-" in expr:
        parts = expr.split("-")
        return eval_expr(parts[0], scope) - eval_expr(parts[1], scope)
    else:
        raise Exception(f"Unknown expression: {expr}")

def load_stdlib():
    try:
        with open("stdlib/__init__.hex") as f:
            execute(f.readlines(), variables)
    except FileNotFoundError:
        print("Warning: No stdlib loaded.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hexlang_runtime.py your_script.hex")
        sys.exit(1)
    load_stdlib()
    with open(sys.argv[1]) as f:
        execute(f.readlines(), variables)
