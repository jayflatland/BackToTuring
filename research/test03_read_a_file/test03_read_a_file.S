
.global _start
.text
_start:

mov     $1, %rax
mov     $1, %rdi
mov     $_1, %rsi
mov     $_1_len, %rdx
syscall

mov     $1, %rax
mov     $1, %rdi
mov     $_2, %rsi
mov     $_2_len, %rdx
syscall

mov     $60, %rax
xor     %rdi, %rdi
syscall

.data

_1:
.ascii "Hello world from python to assembly!\n"
_1_len = . - _1

_2:
.ascii "Ain't this just swell?\n"
_2_len = . - _2

