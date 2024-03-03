#!/usr/bin/env python3

from run_program import run_asm_program_text

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


    
print("Generating program assembly...")
p = gen_hello_world_program('"Hello from pygen!"')
print(p)
print("Running...")
run_asm_program_text(p)