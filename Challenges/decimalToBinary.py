# Created by Bhushan Udupa at 11:05 AM 7/3/2024 using PyCharm
def decimal_to_binary(num):
    if num >= 1:
        decimal_to_binary(num // 2)
    print(num % 2, end='')


if __name__ == "__main__":
    num = int(input('Enter a decimal number: '))
    decimal_to_binary(num)
