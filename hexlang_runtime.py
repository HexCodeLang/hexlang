import re
import sys

env = {}

def tokenize(code):
    return code.strip().splitlines()

def eval_line(line):
    line = line.strip()

    # conjure var to 13
    match = re.match(r"conjure (\w+) to (.+)", line)
    if match:
        var, val = match.groups()
        env[var] = eval_expr(val)
        return

    # bind var from a + b
    match = re.match(r"bind (\w+) from (.+)", line)
    if match:
        var, expr = match.groups()
        env[var] = eval_expr(expr)
        return

    # whisper "message"
    match = re.match(r'whisper "(.*)"', line)
    if match:
        print(match.group(1))
        return

    # whisper var
    match = re.match(r"whisper (.+)", line)
    if match:
        val = eval_expr(match.group(1))
        print(val)
        return

    # if x exceeds y then whisper "msg"
    match = re.match(r'if (\w+) exceeds (\d+) then whisper "(.*)"', line)
    if match:
        var, threshold, msg = match.groups()
        if env.get(var, 0) > int(threshold):
            print(msg)
        return

def eval_expr(expr):
    expr = expr.strip()
    try:
        return eval(expr, {}, env)
    except:
        return env.get(expr, expr)

def run_hex_file(path):
    with open(path) as f:
        for line in tokenize(f.read()):
            if line: eval_line(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: hex myscript.hex")
    else:
        run_hex_file(sys.argv[1])
