all: main

main.S: main.py
	./main.py > main.S

main: main.S
	gcc -no-pie -nostdlib main.S -o main

clean:
	rm main *.S *.o core
