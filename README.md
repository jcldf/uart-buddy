# M5Stack UART Communication Interface

This project is a Python script designed to run on an M5Stack device, providing an interactive UART communication interface. The script includes user-friendly features for managing UART baud rates, sending commands, receiving data, and logging information to an SD card.

## Features

- **Adjustable Baud Rate**: Cycle through common UART baud rates with a single button press, including 9600, 115200, 230400, and up to 921600. The current baud rate is dynamically displayed on the screen.
- **Send Commands Easily**: Send a "help" command to the UART-connected device by pressing a designated button. The button label temporarily changes color as visual feedback.
- **Live Data Display**: Monitor incoming UART data on the M5Stack’s LCD screen. The screen refreshes periodically to maintain readability.
- **Data Logging**: All received UART data is logged to an SD card for future analysis. (not implemented yet)
- **Battery Status Monitoring**: The screen title displays the M5Stack battery level, helping users keep track of power status during operation.

## Usage

1. **Button B (Help Command)**: Pressing Button B will send a predefined "help" command to the connected UART device. This is useful for quickly retrieving device information or assistance commands.
2. **Button C (Baud Rate Cycling)**: Pressing Button C cycles through different baud rates, allowing users to communicate with devices using various speeds. Each press changes the baud rate and updates the display with the new rate.
3. **Data Reception and Display**: The M5Stack continuously listens for incoming UART data and displays it on the screen. After a certain number of lines, the display clears to ensure a clean and organized view.
4. **SD Card Logging**: Each received data entry is saved to an SD card, providing a persistent log that can be analyzed later.

## Interface Preview

The script initializes a clean and user-friendly interface on the M5Stack screen, with designated areas for:
- **Current Baud Rate**
- **Received Data Log**
- **Battery Level Indicator**

The layout is designed to make UART interaction seamless and intuitive, even for users new to M5Stack and UART communication.

## Code Summary

The main code blocks include:
- **Initialization**: Sets up UART communication, button controls, and the LCD interface.
- **Button Press Handlers**: Manages Button B (for sending the help command) and Button C (for baud rate adjustments).
- **Data Processing**: Reads data from the UART interface, displays it, and logs it to the SD card.
- **Battery Monitoring**: Periodically checks and displays the battery level on the screen title.

## Requirements

- **M5Stack Device**: Tested on M5Stack Core, compatible with M5Stack modules.
- **MicroSD Card**: For data logging.
- **M5Stack Libraries**: Required libraries for UART and LCD screen control.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/m5stack-uart-interface.git
