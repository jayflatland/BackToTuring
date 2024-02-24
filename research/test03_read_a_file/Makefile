all: test03_read_a_file

test03_read_a_file: test03_read_a_file.asm
	nasm -f elf64 -o test03_read_a_file.o test03_read_a_file.asm
	ld -m elf_x86_64 -o test03_read_a_file test03_read_a_file.o

clean:
	rm test03_read_a_file *.o core
