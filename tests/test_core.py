import subprocess

def test_run_hello_world():
    result = subprocess.run(["python", "hex.py", "examples/hello_world.hex"], capture_output=True, text=True)
    assert "Hello, Hex World!" in result.stdout
