all: test05

test05: test05.asm
	nasm -f elf64 -o test05.o test05.asm
	ld -m elf_x86_64 -o test05 test05.o

clean:
	rm test05 *.o core
