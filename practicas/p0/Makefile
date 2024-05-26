
SRC=hw
EXE=$(SRC)


do: console

all: console postscript troff clean

console: python \
	 clean


python: $(SRC).py
	@echo "Hello world en $@..."
	python $<


clean:
	@echo "Limpiando..."
	rm -f $(EXE) HelloWorld.class
