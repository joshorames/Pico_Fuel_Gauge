import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 1350000

def read_adc(channel):
    """Reads SPI data from the MCP3008, 8 channels (0-7)"""
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def fuel_percentage(adc_value):
    """Convert ADC value to fuel percentage"""
    max_adc = 1023  # 10-bit ADC
    empty_resistance = 90  # Ohms
    full_resistance = 3  # Ohms

    # Map ADC value to resistance (approximate linearization)
    resistance = empty_resistance - (adc_value / max_adc) * (empty_resistance - full_resistance)

    # Convert resistance to fuel level percentage
    percentage = ((empty_resistance - resistance) / (empty_resistance - full_resistance)) * 100
    return max(0, min(100, percentage))  # Clamp to 0-100%

while True:
    adc_value = read_adc(0)  # Read from channel 0
    fuel_level = fuel_percentage(adc_value)
    print(f"Fuel Level: {fuel_level:.2f}%")
    time.sleep(1)
