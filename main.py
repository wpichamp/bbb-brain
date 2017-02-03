from core.easyRS485.easyRS485 import Network, Module
from core.easyRS485.commands import GetStatus
from dsupport.standard_uart import port

network = Network(port)

left_arduino = Module(network, 1)
right_arduino = Module(network, 2)

print "Starting Handshake"

while True:

    left_response_message = left_arduino.send_message(GetStatus())
    right_response_message = right_arduino.send_message(GetStatus())

    print "L: " + "b: " + str(left_response_message.d0) + " p: " + str(left_response_message.d1) + " R: " + "b: " + str(right_response_message.d0) + " p: " + str(right_response_message.d1)
