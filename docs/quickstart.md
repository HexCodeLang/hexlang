# 🚀 HexLang Quick Start Guide

## What is HexLang?

HexLang is a programming language where you write code the way you talk. No semicolons, no complex syntax—just natural, conversational programming.

## Installation

```bash
git clone https://github.com/HexCodeLang/hexlang.git
cd hexlang
pip install -e .
```

## Your First Program

Create a file called `hello.hexlang`:

```hexlang
say "Hello, World!"
let's make a number called count = 10
if count > 5, say "That's a lot!"
```

Run it:

```bash
hexlang run hello.hexlang
```

## Try the Demo

See all language features in action:

```bash
hexlang demo
```

## Language Features

### Variables
```hexlang
let's make a number called apples = 5
```

### Printing
```hexlang
say "Hello!"
```

### Conditionals
```hexlang
if apples > 3, say "You have lots of apples!"
```

### Functions
```hexlang
whenever you need to greet, say "Hey there!"
greet now
```

## Compiling Programs

Compile your HexLang code to Python bytecode:

```bash
hexlang compile myprogram.hexlang
```

This creates:
- `myprogram_compiled.py` - Intermediate Python code
- `myprogram.pyc` - Compiled bytecode

## Examples

Check out the `examples/` directory for more:
- `hello_world.hexlang` - Basic example
- `calculator.hexlang` - Math operations
- `functions.hexlang` - Function definitions
- `conditionals.hexlang` - If statements
- `demo.hexlang` - Comprehensive demo

## Next Steps

- Read the [Installation Guide](installation.md)
- Study the [Grammar Guide](grammar.md)
- Explore the example programs
- Start writing your own HexLang code!

## Getting Help

```bash
hexlang --help
```

## Philosophy

HexLang believes that code should be readable by humans first, computers second. If you can say it, you can code it.

Happy coding! 🍭
