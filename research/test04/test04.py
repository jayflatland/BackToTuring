#!/usr/bin/env python3

import os
import sys
import tempfile
import shutil

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


def run_program(progtext):
    tmpdir = tempfile.mkdtemp()
    base_filename = os.path.join(tmpdir, "tmp")
    asm_file = open(base_filename + '.asm', 'w')
    asm_file.write(progtext)
    asm_file.close()

    os.system(f"nasm -f elf64 -o {base_filename}.o {base_filename}.asm")
    #TODO - check for errors here
    os.system(f"ld -m elf_x86_64 -o {base_filename}.x {base_filename}.o")
    #TODO - check for errors here
    os.system(f"{base_filename}.x")
    shutil.rmtree(tmpdir)
    
p = gen_hello_world_program('"Hello from pygen!"')
run_program(p)