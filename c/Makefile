
APP1 = servo_read
APP2 = servo_control_modes
APP3 = servo_move_to
APP4 = ranger_read

TARGETS = $(APP1) $(APP2) $(APP3) $(APP4) 

SOURCE_COMMON = $(wildcard ./src/*.c)
SOURCE_APP1 = $(SOURCE_COMMON) $(wildcard ./examples/servo_read.c)
SOURCE_APP2 = $(SOURCE_COMMON) $(wildcard ./examples/servo_control_modes.c)
SOURCE_APP3 = $(SOURCE_COMMON) $(wildcard ./examples/servo_move_to.c)
SOURCE_APP4 = $(SOURCE_COMMON) $(wildcard ./examples/ranger_read.c)

OBJ_APP1 = $(patsubst %.c, %.o, $(SOURCE_APP1))
OBJ_APP2 = $(patsubst %.c, %.o, $(SOURCE_APP2))
OBJ_APP3 = $(patsubst %.c, %.o, $(SOURCE_APP3))
OBJ_APP4 = $(patsubst %.c, %.o, $(SOURCE_APP4))

INCLUDE_COMMON = -I./include -I/usr/local/include/modbus -L/usr/local/lib -lmodbus

CFLAGS = -Wall -c
CC = gcc

all: $(TARGETS)
$(APP1): $(OBJ_APP1)	
	@mkdir -p build/
	$(CC) $(OBJ_APP1) $(INCLUDE_COMMON) -o build/$(APP1)

$(APP2): $(OBJ_APP2)	
	@mkdir -p build/
	$(CC) $(OBJ_APP2) $(INCLUDE_COMMON) -o build/$(APP2)

$(APP3): $(OBJ_APP3)	
	@mkdir -p build/
	$(CC) $(OBJ_APP3) $(INCLUDE_COMMON) -o build/$(APP3)

$(APP4): $(OBJ_APP4)	
	@mkdir -p build/
	$(CC) $(OBJ_APP4) $(INCLUDE_COMMON)  -o build/$(APP4)		

%.o: %.c
	$(CC) $(INCLUDE_COMMON) $(CFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -rf $(OBJ_APP1) $(OBJ_APP2) $(OBJ_APP3) $(OBJ_APP4)  build/ 

