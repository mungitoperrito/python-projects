# Use the crypt library and a cleartext list to decrypt passwords

# NOTE: crypt is deprecated in 3.12
# Comment to see depreciation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import crypt

DEBUG = False

def crack_password(encrypted_password, cleartext_list):
    # Extract salt
    salt = encrypted_password[0:2]
    encrypted_word = encrypted_password[2:]

    # Runs the whole cleartext list for a single word
    with open(cleartext_list, 'r') as clear_list:
        for word in clear_list.readlines():
            word = word.rstrip('\n')
            encrypted_test_word = crypt.crypt(word, salt)

            if encrypted_test_word == encrypted_password:
                print(f"{encrypted_password}: {word}")
                return
        print(f"{encrypted_password} is not in the dictionary list")

def main():
    cleartext_list = "list_cleartext.txt"
    password_list = "list_passwords_crypt.txt"

    with open(password_list, 'r') as pwd_list:
        for pwd in pwd_list:
            crack_password(pwd.rstrip('\n'), cleartext_list)

if __name__ == "__main__":
    if DEBUG:
        import sys
        print(sys.version)

    main()