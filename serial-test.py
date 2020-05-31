#!/bin/env python3
import logging
import serial
import time

class leoPhi():


    def __init__(self, device):
        logging.debug("Connecting to {0}".format(device))
        self.port = serial.Serial(device)

    def _read(self):
        message = self.port.readline()
        # Convert from binary back to string
        message = message.decode()
        return(message.rstrip('\r\n'))

    def _write(self, command):
        logging.debug("Sending {0}".format(command))
        self.port.write(command.encode())
        pass


    # LeopHi commands
    # C - Continous Read Mode: Dump readings and data every second
    # R - Single pH reading: response "pH: XX.XX" where XX.XX is the pH
    # E - Exit continous read mode
    # S - set pH7 Calibration point
    # F - set pH4 Calibration point: also relalcs probe slope and saves settings to EEPROM
    # T - set pH10 Calibration point: also recalcs probe slope and saves settings to EEPROM
    # X - restore settings to default and idela probe conditions


    def reset(self):
        logging.debug("Resetting serial")
        self._write("X")
        message = self._read()
        logging.debug("Got {0}".format(message))

    def read_ph(self):
        logging.debug("Getting pH value")
        self._write("R")
        ph_value = self._read()
        logging.debug("Got {0}".format(ph_value))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    ph = leoPhi("/dev/ttyACM0")
    ph.reset()
    while True:
        ph.read_ph()
        time.sleep(10)
