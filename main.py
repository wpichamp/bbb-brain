from dsupport.standard_uart import port

from time import sleep


class Message(object):
    def __init__(self, incoming=None):

        if incoming is None:
            self.target_id = 0
            self.checksum = None
            self.blank = 0

            self.d0 = 0
            self.d1 = 0
            self.d2 = 0
            self.d3 = 0
            self.d4 = 0
            self.d5 = 0
            self.d6 = 0
        else:
            self.target_id = ord(incoming[0])
            self.checksum = ord(incoming[1])
            self.blank = ord(incoming[2])

            self.d0 = ord(incoming[3])
            self.d1 = ord(incoming[4])
            self.d2 = ord(incoming[5])
            self.d3 = ord(incoming[6])
            self.d4 = ord(incoming[7])
            self.d5 = ord(incoming[8])
            self.d6 = ord(incoming[9])

    def __set_checksum__(self):
        self.checksum = 0

    def to_byte_array(self):
        self.__set_checksum__()
        list = [self.target_id, self.checksum, self.blank, self.d0, self.d1, self.d2, self.d3, self.d4, self.d5,
                self.d6]
        return bytearray(list)

my_id = 0
count = 0
t_id = 1

while True:

    write_message = Message()

    write_message.target_id = t_id
    write_message.d0 = count

    port.write(write_message.to_byte_array())

    rx_raw = port.read(10)

    read_message = Message(rx_raw)

    if read_message.target_id is my_id:
        print "Slave ID: " + str(read_message.d0) + " Button State: " + str(read_message.d1) + " Pot State: " + str(
            read_message.d2)

    count += 17

    if count > 255:
        count = 0

        if t_id == 1:
            t_id = 2
        else:
            t_id = 1



