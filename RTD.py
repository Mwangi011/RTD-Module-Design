#assuming raspberry pi

import spidev
import time
import math

class RTDReader:
    PT100 = 100
    PT1000 = 1000

    def __init__(self, rtd_type=PT1000):
        self.rtd_type = rtd_type
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)  # SPI0, CS0
        self.spi.max_speed_hz = 500000
        self.init_sensor()

    def write_register(self, reg_addr, value):
        self.spi.xfer2([reg_addr & 0x7F, value])

    def read_register(self, reg_addr, length=1):
        result = self.spi.xfer2([reg_addr | 0x80] + [0x00]*length)
        return result[1:]  # skip first byte (address)

    def init_sensor(self):
        # Configuration: Vbias on, auto conversion off, 3-wire, 50/60 Hz filter
        config_byte = 0b11000010
        self.write_register(0x00, config_byte)

    def read_raw(self):
        # Trigger one-shot conversion
        config = self.read_register(0x00)[0]
        self.write_register(0x00, config | 0x20)
        time.sleep(0.1)

        raw = self.read_register(0x01, 2)
        msb, lsb = raw[0], raw[1]
        rtd_data = ((msb << 8) | lsb) >> 1
        return rtd_data

    def convert_to_temperature(self, raw_code):
        Rref = 430.0 if self.rtd_type == self.PT100 else 4300.0
        Rt = (raw_code / 32768.0) * Rref
        A, B = 3.9083e-3, -5.775e-7
        try:
            temp = (-A + (A**2 - 4 * B * (1 - Rt / self.rtd_type))**0.5) / (2 * B)
        except:
            temp = -999.0  # Error code
        return temp

    def read_temperature(self):
        raw = self.read_raw()
        return self.convert_to_temperature(raw)

    def set_rtd_type(self, rtd_type):
        if rtd_type in [self.PT100, self.PT1000]:
            self.rtd_type = rtd_type

# Example usage
rtd = RTDReader(rtd_type=RTDReader.PT100)
temperature = rtd.read_temperature()
print(f"Temperature: {temperature:.2f} °C")
