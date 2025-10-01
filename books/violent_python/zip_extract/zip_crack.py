import zipfile

# Only returns password it it is correct. Otherwise returns nothing
def extract_file(zip_file, password):
    try:
        # Python3 needs to encode pwd as byte string
        zip_file.extractall(pwd=password.encode())
        return password
    except Exception as e:
        return


def main():
    try:
        zip_file = zipfile.ZipFile('zipped_file.zip', 'r')
    except Exception as e:
        print(f"Can't get zip_file: {e}")
        exit()

    with open('password_file.txt') as password_file:
        for line in password_file.readlines():
            password = line.rstrip('\n')
            guess = extract_file(zip_file, password)
            if guess:
                print(f"PWD: {password}")
                exit(0)


if __name__ == '__main__':
    main()