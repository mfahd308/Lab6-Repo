def main():
    option = 0

    while option != 3:
        print_menu()
        option = int(input('Please enter an option: '))

        if option == 1:
            original = input('Please enter your password to encode: ')
            encoded = encode(original)
            print('Your password has been encoded and stored!')
            print()

        if option == 2:
            decoded = decode(encoded)
            print(f'The encoded password is {encoded}, and the original password is {decoded}.')
            print()

def print_menu():
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()

def encode(password):
    encoded = ''

    for num in password:
        encoded_num = int(num) + 3
        encoded += str(encoded_num)

    return encoded

def decode(encoded_password: str) -> str:
    if len(encoded_password) != 8 or not encoded_password.isdigit():
        raise ValueError("The encoded password must be an 8-digit integer string.")

    decoded_password = ''.join([str((int(digit) - 3) % 10) for digit in encoded_password])
    return decoded_password

if __name__ == '__main__':
    main()
