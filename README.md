# Cross Platform Logitech F510 RumblePad Driver using PyUSB
Basic Device driver for Logitech Rumblepad F510 using PyUSB

This implements a basic driver for the specified gamepad in direct input mode, using PyUSB interrupt communication mode. Since the functionality is implemented using a user-level library (PyUSB, which itself is a wrapper of LibUSB), this driver is cross platform.

The abstracted procedure in the development and functioning of this process is:

1. Identify the hardware device using Vendor and Product IDs
2. If the kernel drivers are active, detach them
3. Select the appropriate configuration to launch the Device with
4. Select the appropriate endpoint from which to send/recieve USB signals in the form of bytearrays
5. (By trial and error) Identify which buttons cause what changes in the bytearray sent received by the program
6. In an infinite loop effectively implementing a busy wait, query the device for any state changes.
7. Process the bytearray and perform predefined actions (In this case display which key was pressed)
8. A signal handler exists by which to exit the process loop safely and terminate the program.

## Dependencies:
1. **Python3**
2. **PyUSB**
Install from pip using
```sh
pip3 install pyusb --user
```
3. **LibUSB**
The dependency for PyUSB, the prepackaged binaries will be easily accessible for all widely used distributions of GNU/Linux, Windows as well as MacOS.
