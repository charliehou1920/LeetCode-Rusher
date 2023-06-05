def confusingNumber(n):
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

def main():
    n = 9
    if(confusingNumber(n)):
        print("It is a Confusing Number!")
    else:
        print("It is not a Confusing Number!")
        

if __name__ == "__main__":
    main()