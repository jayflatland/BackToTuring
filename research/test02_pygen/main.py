#!/usr/bin/env python3


class Generator:
    def __init__(self):
        self.hdr = r"""
            .global _start
            .text
            _start:
        """
        self.code = ""
        self.exit = r"""
            mov     $60, %rax
            xor     %rdi, %rdi
            syscall
        """

        self.data = r"""
            .data
        """
        self.string_cnt = 1

    def output(self):
        return "".join([
            self.hdr,
            self.code,
            self.exit,
            self.data,
        ])

    def print(self, msg):
        sid = f"_{self.string_cnt}"
        self.string_cnt += 1
        self.data += fr"""
            {sid}:
            .ascii "{msg}\n"
            {sid}_len = . - {sid}
        """

        self.code += fr"""
            mov     $1, %rax
            mov     $1, %rdi
            mov     ${sid}, %rsi
            mov     ${sid}_len, %rdx
            syscall
        """


g = Generator()
g.print("Hello world from python to assembly!")
g.print("Ain't this just swell?")
print(g.output())
