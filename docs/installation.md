# 🚀 HexLang Installation Guide

## Quick Install

### Method 1: Install from source (Recommended)

```bash
# Clone the repository
git clone https://github.com/HexCodeLang/hexlang.git
cd hexlang

# Install HexLang
pip install -e .

# Verify installation
hexlang --version
```

### Method 2: Direct Python usage

```bash
# Clone the repository
git clone https://github.com/HexCodeLang/hexlang.git
cd hexlang

# Run directly with Python
python hexlang.py run examples/demo.hexlang
```

## Usage

### Running HexLang programs

```bash
# Run a HexLang program
hexlang run program.hexlang

# Or use the legacy hex.py (backward compatible)
python hex.py examples/hello_world.hexlang
```

### Compiling HexLang programs

```bash
# Compile to Python bytecode
hexlang compile program.hexlang

# Specify output file
hexlang compile program.hexlang -o myprogram.pyc
```

### Running the demo

```bash
# Run the comprehensive demo
hexlang demo
```

## Creating Your First Program

1. Create a file with `.hexlang` extension:

```bash
echo 'say "Hello from HexLang!"' > myprogram.hexlang
```

2. Run it:

```bash
hexlang run myprogram.hexlang
```

## File Extensions

HexLang uses the `.hexlang` file extension for all source files. Both `.hex` and `.hexlang` are supported for backward compatibility.

## Requirements

- Python 3.7 or higher
- No external dependencies!

## Troubleshooting

### Command not found: hexlang

If you get a "command not found" error, make sure:
1. You've installed HexLang with `pip install -e .`
2. Your Python scripts directory is in your PATH
3. Try using `python hexlang.py` instead

### Import errors

Make sure you're running Python 3.7 or higher:
```bash
python --version
```

## Next Steps

- Check out the [examples](../examples/) directory
- Read the [grammar guide](grammar.md)
- Explore the language features with `hexlang demo`
