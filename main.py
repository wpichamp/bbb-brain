from core.easyRS485.easyRS485 import Network, Module
from core.easyRS485.commands import GetStatus
from dsupport.standard_uart import port

network = Network(port)

left_arduino = Module(network, 1)
right_arduino = Module(network, 2)




left_arduino.send_message()