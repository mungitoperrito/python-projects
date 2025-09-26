# Encrypt some test words using: crypt
# NOTE: crypt is deprecated in 3.12

import crypt

words_to_encrypt = ["tech", "betty"]
encrypted_words = []
salt = "SL"

encrypted_words = [crypt.crypt(w, salt) for w in words_to_encrypt]

with open("list_passwords_crypt.txt", 'w') as f_out:
    for ew in encrypted_words:
        f_out.write(f"{ew}\n")

