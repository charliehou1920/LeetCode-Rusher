def confusingNumber(self, n: int) -> bool:
    valid_digits = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    num_str = str(n)
    reverse_num = ''

    for digit in num_str:
        print('digit:',digit)
        if digit not in valid_digits:
            return False
        reverse_num = valid_digits[digit] + reverse_num
        print('reverse_num:', reverse_num)

    return reverse_num != num_str
        

