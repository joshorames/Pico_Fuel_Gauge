# Pico_Fuel_Gauge
Reads remainder of gas left from float fuel level sensor
![image](https://github.com/user-attachments/assets/cb341faa-c642-4bf2-a70f-6777314df0eb)

Fuel Sending Unit

One terminal goes to ground.

The other terminal connects to a voltage divider circuit (signal wire).

Voltage Divider Circuit

A 10KΩ resistor is connected between 3.3V and the fuel sender signal.

The signal wire is then connected to the MCP3008 ADC (CH0).

The MCP3008 converts the analog voltage into a digital value.

MCP3008 to Raspberry Pi

Uses SPI communication to send data to the Raspberry Pi.
