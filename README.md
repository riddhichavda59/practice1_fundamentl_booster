# Interactive Personal Data Collector

A simple Python script that collects basic personal information from the user via the command line, displays it back with type and memory address details, and estimates the user's birth year.

## What It Does

The script asks the user to enter four pieces of information: their name, age, height in meters, and favourite number. Once collected, it prints each value back to the screen along with its Python data type and its memory address. It then calculates an approximate birth year using a fixed current year of 2026 minus the entered age, and prints a closing thank-you message.

## Requirements

Python 3.x is required. The script uses only Python's built-in functions, so no external libraries need to be installed.

## How to Run

Run the script from a terminal using Python 3. You will be prompted to enter your name, age, height, and favourite number one at a time, in that order.

## Example Session

When run, the script first greets the user with a welcome message. It then asks for a name, age, height, and favourite number, one at a time. After all values are entered, it prints each one back along with its type and memory address, followed by an approximate birth year, and finally a goodbye message.

## Notes and Known Issues

There is no input validation in the script. If a user enters non-numeric text where a number is expected, such as for age, height, or favourite number, the program will crash with an error.

The birth year message contains a hardcoded phrase that always says "based on your age of 18," regardless of what age was actually entered. This appears to be leftover text that doesn't reflect the real input and should be corrected.

The calculated birth year is only approximate, since it doesn't account for whether the person's birthday has already occurred earlier in the current year.

The memory addresses shown using Python's id function are implementation details of the Python interpreter. These values will vary between different runs and different machines, and are included here mainly for educational purposes rather than practical use.

## License

This script is free to use and modify for personal or educational purposes.
 connect with me
 linkdin = www.linkedin.com/in/riddhi-chavda-2baba6414
 email = riddhichavda59@gmail.com
