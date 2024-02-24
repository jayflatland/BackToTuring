all: test03_read_a_file

test03_read_a_file: test03_read_a_file.S
	gcc -no-pie -nostdlib test03_read_a_file.S -o test03_read_a_file

clean:
	rm test03_read_a_file *.S *.o core
