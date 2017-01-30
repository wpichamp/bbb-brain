from modules import bbbgpio
from modules.standard_uart import port

from time import sleep


def clean_bytes(incoming_bytes):
    cleaned = []

    for byte in bytes:
        cleaned.append(ord(byte))

    return cleaned


class Info(object):

    def __init__(self, bytes):

        bytes = clean_bytes(bytes)

        self.m_id = bytes[0]
        self.m_size = bytes[1]


if __name__ == "__main__":

    target_id = 2
    my_id = 0

    count = 50

    while True:

        tx_data = [target_id, 3, count]

        print "Writing Out Data: " + str(tx_data)
        port.write(bytearray(tx_data))

        info = Info(port.read(2))

        if info.m_id is my_id:
            message = clean_bytes(port.read(info.m_size))

        print "Target: " + str(target_id) +  " Pot: " + str(message[0]) + " Button: " + str(message[1])

        count += 50

        if count > 100:
            count = 50

        print "Switching Target"

        if target_id == 1:
            target_id = 2
        else:
            target_id = 1
