#!/usr/bin/env python3


example = r"""
        .global _start
        .text
_start:
        mov     $1, %rax
        mov     $1, %rdi
_loop:
        mov     $message, %rsi
        mov     $len, %rdx
        syscall

        mov     $60, %rax
        xor     %rdi, %rdi
        syscall

        .data
message:
        .ascii  "Hello, world\n"
        len = . - message
"""

class Generator:
    def __init__(self):
        self.data = []
        self.text = []

    def output(self):
        return example



g = Generator()
print(g.output())
