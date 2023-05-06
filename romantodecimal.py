def roman_to_decimal(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    prev_num = 0
    
    for i in range(len(roman_numeral) - 1, -1, -1):
        curr_num = roman_dict[roman_numeral[i]]
        if curr_num < prev_num:
            decimal_num -= curr_num
        else:
            decimal_num += curr_num
        prev_num = curr_num
    
    return decimal_num

roman_numeral = input("Enter a Roman numeral: ")
decimal_num = roman_to_decimal(roman_numeral)
print("The decimal equivalent of", roman_numeral, "is", decimal_num)
