# 🍭 HexLang - A Programming Language for Humans

**HexLang** is a full-fledged programming language for humans who are tired of semicolons and want their code to sound like texting their smartest friend.

> You don't write code. You *talk to it.*

## ✨ Example

```hexlang
# Variables with different types
let's make a number called apples = 5
let's make a string called name = "Alice"
let's make a list called fruits = ["apple", "banana", "orange"]

# String interpolation
say "Hello, {name}! You have {apples} apples."

# Arithmetic operations
add 3 to apples
multiply apples by 2
say "After calculations: {apples}"

# Conditionals with else
if apples > 10, say "You got lots of apples!"
otherwise, say "You need more apples!"

# Multiline functions with parameters
whenever you need to greet with person:
    say "Hey there, {person}!"
    say "Welcome to HexLang!"
done

greet with name now

# List operations
for each fruit in fruits, say the fruit
```

## 🚀 Quick Start

### Installation

```bash
# Install HexLang
pip install -e .

# Run the demo
hexlang demo
```

### Run Your First Program

```bash
# Create a program
echo 'say "Hello, World!"' > hello.hexlang

# Run it
hexlang run hello.hexlang
```

### Compile Programs

```bash
# Compile to Python bytecode
hexlang compile myprogram.hexlang
```

## 🛠 Usage

HexLang is a standalone language with its own file extension (`.hexlang`) and command-line tools:

```bash
hexlang run program.hexlang     # Run a program
hexlang compile program.hexlang # Compile to bytecode
hexlang demo                     # Run the demo
hexlang --help                   # Show help
```

## 📚 Documentation

- [Quick Start Guide](docs/quickstart.md) - Get started in 5 minutes!
- [Installation Guide](docs/installation.md) - Detailed installation instructions
- [Grammar Guide](docs/grammar.md) - Language syntax reference
- [Examples](examples/) - Sample programs

## 🎯 Features

- ✅ Natural, conversational syntax
- ✅ Variables (numbers, strings, lists)
- ✅ String interpolation with {variable}
- ✅ Arithmetic operations (add, subtract, multiply, divide, power, modulo)
- ✅ Conditional statements (if/then/otherwise)
- ✅ Multiline functions with parameters
- ✅ List operations (create, add items, iterate)
- ✅ User input with auto-type detection
- ✅ `.hexlang` file extension
- ✅ Standalone compiler/interpreter
- ✅ Auto-compilation to Python bytecode
- ✅ Comprehensive demo program
- ✅ Full-featured calculator application

## 🚀 Roadmap

- [x] Variables (numbers, strings, lists)
- [x] Print, input with auto-type detection
- [x] If/else statements  
- [x] For loops
- [x] Multiline functions with parameters
- [x] Arithmetic operations (add, subtract, multiply, divide, power, modulo)
- [x] String interpolation
- [x] List operations
- [x] Standalone language with .hexlang extension
- [x] Auto-compiler to bytecode
- [x] Comprehensive demo
- [x] Full-featured calculator application
- [ ] While loops
- [ ] Try/catch error handling
- [ ] File I/O operations
- [ ] Web-based interpreter

## 📜 License

MIT or the **Do Whatever You Want** License. HexLang doesn't care.
