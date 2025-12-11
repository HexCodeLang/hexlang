#!/usr/bin/env python3
# Auto-generated from examples/hello_world.hexlang
import sys
sys.path.insert(0, '/home/runner/work/hexlang/hexlang')
from hex import run_hex

hex_code = 'say "Hello, Hex World!"\nlet’s make a number called apples = 5\nif apples > 3, say "You got lots of apples!"\nwhenever you need to greet, say "Hey there!"\ngreet now\n'
run_hex(hex_code)
