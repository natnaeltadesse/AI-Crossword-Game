def roman_to_decimal(roman):
  # Create a dictionary that maps each Roman numeral to its corresponding decimal value.
  roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
  }

  # Initialize the result to 0.
  decimal = 0

  # Iterate over the Roman numeral from left to right.
  for i in range(len(roman)):
    # Get the current Roman numeral and its decimal value.
    current_roman_numeral = roman[i]
    current_decimal_value = roman_numerals[current_roman_numeral]

    # If the current Roman numeral is less than or equal to the previous Roman numeral, add its value to the result.
    if current_decimal_value <= roman_numerals[roman[i]]:
      decimal += current_decimal_value
      i += 1

    # Otherwise, subtract its value from the result.
    else:
      decimal -= current_decimal_value
      i += 2

  return decimal

while True:
    # Get the Roman numeral from the user.
    roman = input("Enter a Roman numeral: ").upper()

    # Convert the Roman numeral to its decimal equivalent.
    decimal = roman_to_decimal(roman)

    # Print the decimal equivalent of the Roman numeral.
    print("The decimal equivalent of \"{}\" is {}".format(roman, decimal))
