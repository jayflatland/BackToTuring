global _start

section .bss
    buf1: db   4096 dup(?)   ; but this is definitely MASM
    buf1len equ $ - buf1

section .data
    fileDescriptor: dq 0
    readSz: dq 0

section .rodata
    msg1: db "Write this message to stdio", 0x0a
    msg1len equ $ - msg1

    msg2: db "Write this message to test.out", 0x0a
    msg2len equ $ - msg2

    filename1: db "test.out", 0
    filename1len equ $ - filename1

    ; filename2: db "test03_read_a_file.asm", 0
    ; filename2len equ $ - filename2

section .text
_start:
    ; mov rax, 1              ; sys_write
    ; mov rdi, 1              ; stdout
    ; mov rsi, msg1           ; data
    ; mov rdx, msg1len        ; sz
    ; syscall

    ; mov rax, 2              ; sys_open
    ; mov rdi, filename1      ; const char *filename
    ; mov rsi, 0102o          ; int flags
    ; mov rdx, 00600o         ; int mode
    ; syscall
    ; mov [fileDescriptor], rax

    ; mov rax, 1              ; sys_write
    ; mov rdi, [fileDescriptor] ; our file
    ; mov rsi, msg2           ; data
    ; mov rdx, msg2len        ; sz
    ; syscall

    ; mov rax,3                 ; sys_close
    ; mov rdi,[fileDescriptor]
    ; syscall

    mov rax, 2              ; sys_open
    mov rdi, filename1      ; const char *filename
    mov rsi, 0102o          ; int flags
    mov rdx, 00600o         ; int mode
    syscall
    mov [fileDescriptor], rax

    mov rax, 0              ; sys_read
    mov rdi, [fileDescriptor] ; our file
    mov rsi, buf1           ; data
    mov rdx, buf1len        ; sz
    syscall
    mov [readSz], rax

    mov rax, 1              ; sys_write
    mov rdi, 1              ; stdout
    mov rsi, buf1           ; data
    mov rdx, readSz         ; sz
    syscall

    mov rax,60
    mov rdi,0
    syscall