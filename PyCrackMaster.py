import time
import sys

def obfuscate(char):
    return chr(ord(char) ^ 0x5F)

def deobfuscate(char):
    return chr(ord(char) ^ 0x5F)

def get_correct_password():
    obfuscated = [obfuscate(c) for c in "SecurePass123"]
    return ''.join(obfuscated)

def check_password(input_password):
    correct_password = get_correct_password()
    return input_password == correct_password

def main():
    print("Вітаємо у PyCrackMaster!")
    user_input = input("Будь ласка, введіть пароль активації: ")

    # Невелика затримка для ускладнення аналізу
    time.sleep(0.5)

    if check_password(user_input):
        print("Вітаємо! Ви розбили PyCrackMaster.")
    else:
        print("Пароль невірний. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
