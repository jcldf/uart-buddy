# uart-buddy
m5stack uart terminal
This script is designed for an M5Stack device to facilitate UART communication and to provide a user-friendly interface for modifying UART baud rates. The code initializes a user interface with text labels and buttons, which allows interaction with the UART module of the M5Stack.

Button B is configured to send a "help" command via UART when pressed, and provides a visual indication by changing the label color temporarily.

Button C cycles through different baud rates for UART communication. Starting from 9600, it changes to other rates including 115200, 230400, up to 921600. Each change updates the displayed baud rate value on the screen.

The code also reads incoming data from the UART interface and displays it on the M5Stack's LCD screen, while logging the data to an SD card. It periodically checks if the UART module has received any data, and prints it to the display while managing screen space by clearing the display after a certain number of lines. Additionally, the battery level of the M5Stack is shown on the screen title, providing insight into the power status of the device.

This script makes it easier for users to interact with UART-connected devices, change baud rates on the fly, and log communication data for further analysis.
