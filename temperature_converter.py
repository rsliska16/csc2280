# temperature_converter.py
# Convert temperature in Celsius to Fahrenheit.
#
# This simple script demonstrates the following skills:
#   - using a 'main' function
#   - prompting the user for numeric input
#   - processing input using common mathematical operations
#   - printing output for the user to see

def main():
    # Prompt the user to provide an input temperature in Celsius
    celsius = int(input("Enter a temperature in Celsius: "))

    # Process the input, converting it to Fahrenheit
    fahrenheit = (9 / 5) * celsius + 32

    # Print the output for the user
    print("That is equivalent to", fahrenheit, "degrees Fahrenheit")


main()
