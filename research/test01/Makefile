main: main.o
	ld main.o -o main

main.o: main.S
	as main.S -o main.o

clean:
	rm main.o main