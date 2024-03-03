global _start

section .bss
    buf1: db   4096 dup(?)
    buf1len equ $ - buf1

section .data
    fileDescriptor: dq 0
    readSz: dq 0

section .rodata
    msg1: db "Write this message to stdio", 0x0a
    msg1len equ $ - msg1

    no_file_msg: db "Must provide a file argument", 0x0a
    no_file_msglen equ $ - no_file_msg

    yes_file_msg: db "Yay a file!", 0x0a
    yes_file_msglen equ $ - yes_file_msg

    msg2: db "Write this message to test.out", 0x0a
    msg2len equ $ - msg2

    filename1: db "test05.asm", 0
    filename1len equ $ - filename1

section .text
_start:
    mov rdi, [rsp + 8 * 0]
    cmp rdi, 2
    jne no_file

    ; mov rax, [rsp + 8 * 1]
    ; mov rax, [rsp + 8 * 2]

    mov rax, 1 ; sys_write
    mov rdi, 1 ; stdout
    mov rsi, yes_file_msg
    mov rdx, yes_file_msglen
    syscall

    mov rax, 2              ; sys_open
    mov rdi, [rsp + 8 * 2]  ; const char *filename, is our argv[1], still there
    mov rsi, 0102o          ; int flags
    mov rdx, 00600o         ; int mode
    syscall
    mov [fileDescriptor], rax

    mov rax, 0              ; sys_read
    mov rdi, [fileDescriptor] ; our file
    mov rsi, buf1           ; data
    mov rdx, buf1len        ; sz
    syscall
    ; mov [readSz], rax

    ; mov rax, 1              ; sys_write
    ; mov rdi, 1              ; stdout
    ; mov rsi, buf1           ; data
    ; mov rdx, readSz         ; sz
    ; syscall

    jmp exit

no_file:
    mov rax, 1 ; sys_write
    mov rdi, 1 ; stdout
    mov rsi, no_file_msg
    mov rdx, no_file_msglen
    syscall
        

exit:
    mov rax,60
    mov rdi,0
    syscall