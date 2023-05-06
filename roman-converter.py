def roman_to_decimal(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    prev_val = 0
    for i in reversed(range(len(roman_numeral))):
        curr_val = roman_dict[roman_numeral[i]]
        if curr_val < prev_val:
            decimal_num -= curr_val
        else:
            decimal_num += curr_val
        prev_val = curr_val
    return decimal_num

while True:
    roman_numeral = input("Enter a Roman numeral between 1 and 3999: ").upper()
    decimal_num = roman_to_decimal(roman_numeral)
    print(f"The decimal equivalent of {roman_numeral} is {decimal_num}")
