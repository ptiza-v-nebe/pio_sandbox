from serial.tools.list_ports import comports
from platformio.commands.device import helpers as device_helpers
import sys

project_options = device_helpers.get_project_options(sys.argv[1])
serial_number = project_options["custom_hla_serial"]

for i in comports():
    if i.serial_number == serial_number:
        sys.stdout.write(i.device)