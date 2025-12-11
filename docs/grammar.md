# 📚 HexLang Language Syntax Guide

HexLang uses the `.hexlang` file extension. All programs should be saved with this extension.

## Language Constructs

### Comments
```hexlang
# This is a comment
# Comments start with # and are ignored by the interpreter
```

### Variables
```hexlang
let's make a number called apples = 5
```

### Printing
```hexlang
say "hello!"
```

### Input
```hexlang
ask the user for their name
```

### If Statements
```hexlang
if apples > 10, say "that's too many apples"
```

### Loops
```hexlang
for each thing in list, say the thing
```

### Functions
```hexlang
whenever you need to greet, say "hi there!"
greet now
```

## Complete Example

```hexlang
# A complete HexLang program
let's make a number called score = 95

say "Welcome to HexLang!"

if score > 90, say "Excellent work!"

whenever you need to celebrate, say "🎉 Awesome!"
celebrate now
```

## Running Programs

Save your code with a `.hexlang` extension and run:

```bash
hexlang run myprogram.hexlang
```
