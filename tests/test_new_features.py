import subprocess
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import hex

def test_arithmetic_operations():
    """Test arithmetic operations"""
    code = '''
let's make a number called x = 10
add 5 to x
subtract 3 from x
multiply x by 2
divide x by 4
'''
    hex.run_hex(code)
    assert hex.variables['x'] == 6.0

def test_string_variables():
    """Test string variables and interpolation"""
    code = '''
let's make a string called name = "Alice"
let's make a number called age = 25
'''
    hex.run_hex(code)
    assert hex.variables['name'] == "Alice"
    assert hex.variables['age'] == 25

def test_list_operations():
    """Test list creation and operations"""
    code = '''
let's make a list called fruits = ["apple", "banana"]
add "orange" to list fruits
'''
    hex.run_hex(code)
    assert hex.variables['fruits'] == ["apple", "banana", "orange"]

def test_power_operation():
    """Test power operation"""
    code = '''
let's make a number called base = 2
raise base to the power of 8
'''
    hex.run_hex(code)
    assert hex.variables['base'] == 256

def test_modulo_operation():
    """Test modulo operation"""
    code = '''
let's make a number called num = 17
get remainder of num divided by 5
'''
    hex.run_hex(code)
    assert hex.variables['num'] == 2

def test_multiline_function():
    """Test multiline function definition and execution"""
    code = '''
let's make a number called counter = 0
whenever you need to increment:
    add 1 to counter
done
increment now
increment now
'''
    hex.run_hex(code)
    assert hex.variables['counter'] == 2

def test_function_with_parameters():
    """Test multiline function with parameters"""
    code = '''
let's make a number called result = 0
whenever you need to set_value with val:
    let's make a number called result = val
done
set_value with 42 now
'''
    hex.run_hex(code)
    assert hex.variables['result'] == 42

def test_run_arithmetic_example():
    """Test arithmetic example file"""
    result = subprocess.run(["python", "hex.py", "examples/arithmetic.hexlang"], 
                          capture_output=True, text=True)
    assert "Advanced Arithmetic Demo" in result.stdout
    assert "After adding 5: x = 15" in result.stdout
    assert "2 to the power of 8 = 256" in result.stdout

def test_run_strings_example():
    """Test strings example file"""
    result = subprocess.run(["python", "hex.py", "examples/strings.hexlang"], 
                          capture_output=True, text=True)
    assert "String Operations Demo" in result.stdout
    assert "Greeting: Hello" in result.stdout

def test_run_lists_example():
    """Test lists example file"""
    result = subprocess.run(["python", "hex.py", "examples/lists.hexlang"], 
                          capture_output=True, text=True)
    assert "List Operations Demo" in result.stdout
    assert "Learn HexLang" in result.stdout

def test_run_multiline_functions_example():
    """Test multiline functions example file"""
    result = subprocess.run(["python", "hex.py", "examples/multiline_functions.hexlang"], 
                          capture_output=True, text=True)
    assert "Multiline Functions Demo" in result.stdout
    assert "Hello, Alice!" in result.stdout
    assert "Area: 50" in result.stdout
