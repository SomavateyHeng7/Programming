def binary_to_decimal(binary_str):
    # Check that input is valid
    if binary_str[0] == '0':
        return None, False
    # Convert binary string to decimal 
    else:
        decimal_num = 0
        power = len(binary_str) - 1
        CheckValidation = True
        for num in binary_str:
            if num not in ('1', '0'):
                CheckValidation = False
            else:
                decimal_num += int(num)*2**power
                power -= 1
        return decimal_num, CheckValidation

binary_str = input("Enter Binary Number:")
number , CheckValidation = binary_to_decimal(binary_str)

if CheckValidation:
    print(f'Decimal Number: {number}')
else:
    if number is None:
        print(f'The binary number input cannot start with 0!!!!')
    else:
        print('Invalid Input!!!')
    
