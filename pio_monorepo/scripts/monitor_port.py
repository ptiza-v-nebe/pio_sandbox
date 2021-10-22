from serial.tools.list_ports import comports
import sys

serial_number="003700373438510934313939"

for i in comports():
    if i.serial_number==serial_number:
        sys.stdout.write(i.device)