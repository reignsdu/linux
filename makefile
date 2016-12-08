#make main
OBJS=main.o
main:$(OBJS)
	gcc -o main $(OBJS)
main.o:main.c
	gcc -c main.c
clean:
	rm -f *.o
