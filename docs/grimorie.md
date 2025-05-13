# 📖 THE GRIMOIRE
### A living spellbook for the HexLang programming language

> “When logic fails, summon chaos.”

Welcome, initiate. If you're reading this, it means you've heard the whispers from your terminal. It means you want more than just variables and functions. You want spells. Runes. Control over the machine. You're home.

---

## 🔮 CORE SPELLS

These are the base runes of HexLang—use them wisely. Abuse them frequently.

---

### `conjure <var> to <value>`

**Purpose:** Declare and initialize a variable.

**Example:**
```hex
conjure mana to 40
```
---

### `bind <var> from <expression>`

**Purpose:** Assign a value based on a computation.

**Example:**
```hex
bind chaos from mana + 13
```

---

### `whisper <value>`

**Purpose:** Speak directly to the user or the void.

**Example:**
```hex
whisper "Spell complete."
whisper chaos
```
---

### `if <var> exceeds <value> then whisper "<message>"`

**Purpose:** Basic conditional casting.

**Example:**
```
if chaos exceeds 50 then whisper "The gate opens."
```
---

## 🧠 Math and Types

- Supports integers and floats` (`3`, `4.5`)`
- Math: `+`, `-`, `*`, `/`
- ``x + y`` will auto-coerce types
- ``"5"`` stays a string — but `5` is treated as numeric

---

## 🪄 Ritual Returns

Use `return` to return a value from a ritual:
```
ritual power with x
return x * x
end
```
---

## ❌ Errors

- Bad math or variables won't crash the ritual.
- Errors are printed as `[error: something]`
## 🧪 SOON TO BE SUMMONED

Planned future spells and syntax:

- `loop <n> times:` — repeat a ritual
- `ritual <name>:` — define a custom function
- `summon "<file.hex>"` — import other spell files
- `curse <var>` — delete a variable
- `hex <code>` — raw interpreter commands

---

## ☠️ RESERVED WORDS

Avoid naming your variables with these sacred symbols:

- conjure
- bind
- whisper
- if
- exceeds
- then
- ritual
- loop
- summon
- curse
- hex

---

## 💡 NOTES FROM THE ARCANE COUNCIL

- All variables are global (magic doesn't care about scope).
- Math is plain-text (`+`, `-`, `*`, `/`) using Python rules for now.
- You can't whisper your way out of broken spells.

---

## 📜 EXAMPLE RITUAL
```
conjure mana to 90
bind fury from mana + 10
whisper "Charging..."
if fury exceeds 95 then whisper "Spell cast!"
```
**Expected Output:**
```
Charging...
Spell cast!
```

---

## 🐍 RUNNING THE INTERPRETER

Use the sacred interpreter artifact:

`python hexlang_runtime.py path/to/spell.hex`

---

## 🕷️ FINAL WARNING

HexLang is unstable, unholy, and unnecessary. It exists only to empower chaos. Use at your own risk. Side effects may include runtime hauntings and mild existential dread.

> “Code is just magic we understand.” -CJ Hauser, founder of HexLang
