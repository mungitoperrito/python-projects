import crypt        # crypt is deprecated in 3.12

def crack_password(encrypted_password, cleartext_list):
    # Extract salt
    salt = encrypted_password[0:2]
    encrypted_word = encrypted_password[2:]

    # Runs the whole cleartext list for a single word
    with open(cleartext_list, 'r') as clear_list:
        for word in clear_list.readlines():
            word = word.rstrip('\n')
            encrypted_test_word = crypt.crypt(word, salt)
            print(f"DB02 word: {word}   salt: {salt} enc: {encrypted_test_word}")

def main():
    cleartext_list = "list_cleartext.txt"
    # password_list = "list_passwords_crypt.txt"
    password_list = ["one", "two", "three"]

    for pwd in password_list:
        crack_password(pwd, cleartext_list)

if __name__ == "__main__":
    import sys

    print(sys.version)
    main()