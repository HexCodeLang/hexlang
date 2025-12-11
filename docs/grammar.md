# 📚 HexLang Language Syntax Guide

HexLang uses the `.hexlang` file extension. All programs should be saved with this extension.

## Language Constructs

### Comments
```hexlang
# This is a comment
# Comments start with # and are ignored by the interpreter
```

### Variables

#### Numbers
```hexlang
let's make a number called apples = 5
let's make a number called price = 19.99
```

#### Strings
```hexlang
let's make a string called name = "Alice"
let's make a string called greeting = "Hello World"
```

#### Lists
```hexlang
let's make a list called fruits = ["apple", "banana", "orange"]
let's make a list called numbers = [1, 2, 3, 4, 5]
let's make a list called empty = []
```

### Printing

#### Simple Print
```hexlang
say "hello!"
```

#### Print Variables
```hexlang
say apples
```

#### String Interpolation
```hexlang
say "I have {apples} apples"
say "Hello, {name}! You have {score} points."
```

### Input

#### Simple Input
```hexlang
ask the user for their name
ask the user for age
```

#### Custom Prompt
```hexlang
ask "What is your favorite color?" and store in color
ask "Enter a number:" and save it in value
```

### Arithmetic Operations

#### Addition
```hexlang
add 5 to apples
```

#### Subtraction
```hexlang
subtract 3 from apples
```

#### Multiplication
```hexlang
multiply apples by 2
```

#### Division
```hexlang
divide apples by 4
```

#### Power
```hexlang
raise base to the power of exponent
```

#### Modulo (Remainder)
```hexlang
get remainder of dividend divided by divisor
```

### Conditional Statements

#### Simple If Statement
```hexlang
if apples > 10, say "that's too many apples"
if score = 100, say "Perfect score!"
```

#### If with Action
```hexlang
if temperature > 30, add 1 to hot_days
if count < 10, multiply count by 2
```

#### If-Else Statement
```hexlang
if age >= 18, say "You are an adult"
otherwise, say "You are a minor"
```

### Loops

#### For Each Loop
```hexlang
for each thing in list, say the thing
for each number in numbers, say the number
```

### List Operations

#### Add to List
```hexlang
add "grape" to list fruits
add 42 to list numbers
```

#### Get Item from List
```hexlang
get item 0 from list fruits and save in first_fruit
```

### Functions

#### One-liner Functions
```hexlang
whenever you need to greet, say "hi there!"
greet now
```

#### Multiline Functions (No Parameters)
```hexlang
whenever you need to welcome:
    say "════════════════"
    say "  Welcome!      "
    say "════════════════"
done

welcome now
```

#### Multiline Functions (With Parameters)
```hexlang
whenever you need to greet_person with name:
    say "Hello, {name}!"
    say "Nice to meet you!"
done

greet_person with "Alice" now
```

#### Multiple Parameters
```hexlang
whenever you need to calculate_area with width and height:
    let's make a number called area = width * height
    say "Area: {area}"
done

calculate_area with 5 and 10 now
```

## Complete Example

```hexlang
# A complete HexLang program demonstrating all features

# Variables
let's make a number called score = 95
let's make a string called player = "Alice"
let's make a list called achievements = ["First Win", "Speed Run"]

say "╔══════════════════════════════════╗"
say "║      Game Statistics            ║"
say "╔══════════════════════════════════╗"
say ""

# String interpolation
say "Player: {player}"
say "Score: {score}"
say ""

# Conditionals with else
if score > 90, say "🏆 Excellent work!"
otherwise, say "Keep trying!"

# Arithmetic
add 5 to score
say "Bonus added! New score: {score}"

# Functions with parameters
whenever you need to award_badge with badge_name:
    say "✨ You earned: {badge_name}"
    add badge_name to list achievements
done

award_badge with "High Scorer" now

# Lists
say ""
say "Your achievements:"
for each achievement in achievements, say the achievement

say ""
say "✨ Game complete!"
```

## Running Programs

Save your code with a `.hexlang` extension and run:

```bash
hexlang run myprogram.hexlang
```

Or compile to bytecode:

```bash
hexlang compile myprogram.hexlang
```
