from bbbgpio import RS485

port = RS485("/dev/ttyO1", baudrate=115200, de_pin_number=60, re_pin_number=115)

