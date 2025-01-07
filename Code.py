def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
choice = input("Type 'E' to encrypt or 'D' to decrypt: ").upper()

if choice == 'E':
    result = caesar_cipher_encrypt(message, shift)
elif choice == 'D':
    result = caesar_cipher_decrypt(message, shift)
else:
    result = "Invalid choice."

print("Result:", result)
