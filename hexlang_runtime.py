import sys
import os

variables = {}

def evaluate(expr):
    try:
        return eval(expr, {}, variables)
    except:
        return expr.strip('"')

def run(lines):
    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line.startswith("conjure "):
            try:
                _, var, _, value = line.split()
                variables[var] = evaluate(value)
            except:
                print(f"✖️ Failed to conjure in line: {line}")
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

def load_stdlib():
    std_path = os.path.join(os.path.dirname(__file__), "stdlib", "__init__.hex")
    if os.path.exists(std_path):
        with open(std_path) as f:
            run(f.readlines())
    else:
        print("⚠️  No stdlib found—you're flying solo, buddy.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hexlang_runtime.py path/to/script.hex")
        sys.exit(1)

    # Load standard spells first
    load_stdlib()

    # Then run the user’s spell
    spell_path = sys.argv[1]
    with open(spell_path) as f:
        run(f.readlines())
