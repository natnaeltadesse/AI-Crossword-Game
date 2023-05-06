def roman_to_decimal(roman_num):
    """
    Converts a Roman numeral to a decimal integer
    :param roman_num: str, the Roman numeral to be converted
    :return: int, the decimal integer equivalent of the Roman numeral
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    for i in range(len(roman_num)):
        if roman_num[i] not in roman_dict:
            print("Error: Invalid Roman numeral")
            return None
        if i > 0 and roman_dict[roman_num[i]] > roman_dict[roman_num[i-1]]:
            decimal_num += roman_dict[roman_num[i]] - 2 * roman_dict[roman_num[i-1]]
        else:
            decimal_num += roman_dict[roman_num[i]]
    return decimal_num

# Prompt the user to enter a Roman numeral
roman_numeral = input("Enter a Roman numeral between 1 and 3999: ")

# Call the function to convert the Roman numeral to a decimal integer
decimal_integer = roman_to_decimal(roman_numeral)

# If the conversion was successful, print the result
if decimal_integer is not None:
    print(f"The Roman numeral {roman_numeral} is equal to {decimal_integer} in decimal.")