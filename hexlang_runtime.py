import sys

variables = {}

def evaluate(expr):
    try:
        return eval(expr, {}, variables)
    except:
        return expr

def run(lines):
    for line in lines:
        line = line.strip()
        if line.startswith("conjure "):
            _, var, _, value = line.split()
            variables[var] = evaluate(value)
        elif line.startswith("bind "):
            parts = line.split()
            var = parts[1]
            expr = ' '.join(parts[3:])
            variables[var] = evaluate(expr)
        elif line.startswith("whisper "):
            msg = line[8:]
            val = evaluate(msg)
            print(val)
        elif line.startswith("if "):
            parts = line.split()
            var = parts[1]
            comp = parts[2]
            val = int(parts[3])
            if comp == "exceeds" and variables.get(var, 0) > val:
                if "whisper" in line:
                    message = line.split("whisper", 1)[1].strip().strip('"')
                    print(message)

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as f:
        run(f.readlines())
