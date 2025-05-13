variables = {}
rituals = {}

def eval_expr(expr, scope):
    expr = expr.strip()
    try:
        # Literal string
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        # Integer
        elif expr.isdigit():
            return int(expr)
        # Float
        elif expr.replace('.', '', 1).isdigit() and '.' in expr:
            return float(expr)
        # Variable
        elif expr in scope:
            return scope[expr]
        elif expr in variables:
            return variables[expr]
        # Math expressions
        elif '+' in expr or '-' in expr or '*' in expr or '/' in expr:
            return eval_math(expr, scope)
        else:
            return expr
    except Exception as e:
        return f"[error: {str(e)}]"

def eval_math(expr, scope):
    for var in scope:
        expr = expr.replace(var, str(scope[var]))
    for var in variables:
        expr = expr.replace(var, str(variables[var]))
    try:
        return eval(expr)
    except Exception as e:
        return f"[math error: {e}]"

def execute(lines, scope=None):
    if scope is None:
        scope = {}

    i = 0
    output = ""
    return_val = None
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("#"):
            i += 1
            continue
        tokens = line.split()

        try:
            if tokens[0] == "ritual":
                name = tokens[1]
                args = tokens[tokens.index("with")+1:] if "with" in tokens else []
                body = []
                i += 1
                while i < len(lines) and lines[i].strip() != "end":
                    body.append(lines[i])
                    i += 1
                rituals[name] = {"args": args, "body": body}
                i += 1
                continue

            if tokens[0] in rituals and "with" in tokens:
                name = tokens[0]
                call_args = tokens[tokens.index("with")+1:]
                ritual = rituals[name]
                local_scope = dict(zip(ritual["args"], [eval_expr(arg, scope) for arg in call_args]))
                result = execute(ritual["body"], local_scope)
                if isinstance(result, tuple):
                    output += result[0]
                    return_val = result[1]
                else:
                    output += result
                i += 1
                continue

            if tokens[0] == "conjure":
                var_name = tokens[1]
                value = eval_expr(" ".join(tokens[3:]), scope)
                scope[var_name] = value
                variables[var_name] = value
                i += 1
                continue

            if tokens[0] == "bind":
                var_name = tokens[1]
                value = eval_expr(" ".join(tokens[3:]), scope)
                if var_name in scope:
                    scope[var_name] = value
                else:
                    variables[var_name] = value
                i += 1
                continue

            if tokens[0] == "whisper":
                msg = eval_expr(line.split(" ", 1)[1], scope)
                output += str(msg) + "\n"
                i += 1
                continue

            if tokens[0] == "return":
                return_val = eval_expr(" ".join(tokens[1:]), scope)
                return (output, return_val)

        except Exception as e:
            output += f"[runtime error: {e}]\n"
        i += 1

    return (output, return_val) if return_val is not None else output
