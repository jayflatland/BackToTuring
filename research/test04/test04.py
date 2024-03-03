#!/usr/bin/env python3

import os
import sys
import tempfile

"""
What's this one about?
 - all self contained python
 - generate the asm
 - make
 - run
 - possible (later) from tmp files
"""

def gen_hello_world_program(msg):
    #sanitize
    msg = msg.replace('"', '", 34, "')

    return f"""
    global _start
    section .rodata
        msg1: db "{msg}", 0x0a
        msg1len equ $ - msg1
    section .text
    _start:
        mov rax, 1
        mov rdi, 1
        mov rsi, msg1
        mov rdx, msg1len
        syscall
        mov rax,60
        mov rdi,0
        syscall
    """


def hello_world(msg):
    # class ScopedTempDir:
    #     def __init__(self):
    #         self.dir = "work"
    tmpdir = "work"

    # print("Generating assembly...")
    base_filename = os.path.join(tmpdir, "tmp")
    asm_file = open(base_filename + '.asm', 'w')
    asm_file.write(gen_hello_world_program(msg))
    asm_file.close()

    # print("Assembling...")
    os.system(f"nasm -f elf64 -o {base_filename}.o {base_filename}.asm")

    # print("Linking...")
    os.system(f"ld -m elf_x86_64 -o {base_filename}.x {base_filename}.o")

    # print("Running...")
    os.system(f"{base_filename}.x")

    #print("HI")
    
hello_world('"Hello from pygen!"')