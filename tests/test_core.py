import subprocess

def test_run_hello_world():
    result = subprocess.run(["python", "hex.py", "examples/hello_world.hexlang"], capture_output=True, text=True)
    assert "Hello, Hex World!" in result.stdout

def test_run_hello_world_with_hexlang():
    result = subprocess.run(["python", "hexlang.py", "run", "examples/hello_world.hexlang"], capture_output=True, text=True)
    assert "Hello, Hex World!" in result.stdout

def test_demo():
    result = subprocess.run(["python", "hexlang.py", "demo"], capture_output=True, text=True)
    assert "Welcome to HexLang!" in result.stdout
    assert "Demo Complete!" in result.stdout
