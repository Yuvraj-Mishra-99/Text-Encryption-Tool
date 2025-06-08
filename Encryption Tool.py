
# CIPHER PROGRAM!!! 🔐
# Made by Yuvraj Mishra 
# This program can encrypt and decrypt text using different cipher algorithms!

print("=" * 50)
print("🔐 CIPHER PROGRAM! 🔐")
print("=" * 50)
print()

def caesar_cipher(text, shift, mode):
    """Caesar cipher function - shifts letters by a number!"""
    result = ""

    for char in text:
        if char.isalpha():  
            if char.isupper():
                if mode == "encrypt":
                    shifted = ord(char) + shift
                    if shifted > ord('Z'):
                        shifted = shifted - 26
                else: 
                    shifted = ord(char) - shift
                    if shifted < ord('A'):
                        shifted = shifted + 26
                result += chr(shifted)
            else:
                if mode == "encrypt":
                    shifted = ord(char) + shift
                    if shifted > ord('z'):
                        shifted = shifted - 26
                else:  
                    shifted = ord(char) - shift
                    if shifted < ord('a'):
                        shifted = shifted + 26
                result += chr(shifted)
        else:
            result += char

    return result

def substitution_cipher(text, mode):
    """Simple substitution cipher - replaces each letter with another!"""
    normal_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"  

    result = ""

    for char in text:
        if char.isalpha():
            
            char_upper = char.upper()

            if mode == "encrypt":
              
                if char_upper in normal_alphabet:
                    index = normal_alphabet.index(char_upper)
                    new_char = cipher_alphabet[index]
                    
                    if char.islower():
                        new_char = new_char.lower()
                    result += new_char
                else:
                    result += char
            else:  
                if char_upper in cipher_alphabet:
                    index = cipher_alphabet.index(char_upper)
                    new_char = normal_alphabet[index]
                    if char.islower():
                        new_char = new_char.lower()
                    result += new_char
                else:
                    result += char
        else:
            
            result += char

    return result

def simple_shift_cipher(text, password, mode):
    """Super simple cipher using a password!"""
    result = ""

    
    key_numbers = []
    for char in password:
        key_numbers.append(ord(char))

    for i, char in enumerate(text):
        if char.isalpha():
            key_num = key_numbers[i % len(key_numbers)]
            shift = key_num % 26  

            if char.isupper():
                if mode == "encrypt":
                    shifted = ord(char) + shift
                    if shifted > ord('Z'):
                        shifted = shifted - 26
                else:  
                    shifted = ord(char) - shift
                    if shifted < ord('A'):
                        shifted = shifted + 26
                result += chr(shifted)
            else:
                if mode == "encrypt":
                    shifted = ord(char) + shift
                    if shifted > ord('z'):
                        shifted = shifted - 26
                else: 
                    shifted = ord(char) - shift
                    if shifted < ord('a'):
                        shifted = shifted + 26
                result += chr(shifted)
        else:
            result += char

    return result

def main():
    while True:
        print("\n🌟 Choose your cipher Style! 🌟")
        print("1. Caesar Cipher (shift letters by a number)")
        print("2. Substitution Cipher (replace letters with secret alphabet)")
        print("3. Password Cipher (use a password to encrypt)")
        print("4. Exit")

        choice = input("\nWhat do you want to do? (1-4): ")

        if choice == "1":
            print("\n🏛️ CAESAR CIPHER TIME! 🏛️")
            mode = input("Do you want to encrypt or decrypt? ").lower()

            if mode in ['e', 'encrypt']:
                text = input("Enter your secret message: ")
                shift = int(input("Enter shift number (1-25): "))
                result = caesar_cipher(text, shift, "encrypt")
                print(f"\n🔐 Encrypted message: {result}")

            elif mode in ['d', 'decrypt']:
                text = input("Enter the encrypted message: ")
                shift = int(input("Enter the shift number used: "))
                result = caesar_cipher(text, shift, "decrypt")
                print(f"\n📖 Decrypted message: {result}")
            else:
                print("❌ Invalid choice!")

        elif choice == "2":
            print("\n🔤 SUBSTITUTION CIPHER TIME! 🔤")
            mode = input("Do you want to encrypt or decrypt? ").lower()

            if mode in ['e', 'encrypt']:
                text = input("Enter your secret message: ")
                result = substitution_cipher(text, "encrypt")
                print(f"\n🔐 Encrypted message: {result}")

            elif mode in ['d', 'decrypt']:
                text = input("Enter the encrypted message: ")
                result = substitution_cipher(text, "decrypt")
                print(f"\n📖 Decrypted message: {result}")
            else:
                print("❌ Invalid choice!")

        elif choice == "3":
            print("\n🔑 PASSWORD CIPHER TIME! 🔑")
            mode = input("Do you want to encrypt or decrypt? ").lower()

            if mode in ['e', 'encrypt']:
                text = input("Enter your secret message: ")
                password = input("Enter your secret password: ")
                result = simple_shift_cipher(text, password, "encrypt")
                print(f"\n🔐 Encrypted message: {result}")

            elif mode in ['d', 'decrypt']:
                text = input("Enter the encrypted message: ")
                password = input("Enter the secret password: ")
                result = simple_shift_cipher(text, password, "decrypt")
                print(f"\n📖 Decrypted message: {result}")
            else:
                print("❌ Invalid choice!")

        elif choice == "4":
            print("\n👋 Thanks for using my cipher program! Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice! Please try again.")

        continue_choice = input("\nDo you want to try another cipher? (y/n): ").lower()
        if continue_choice not in ['y', 'yes']:
            print("\n👋 Thanks for using my cipher program! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
